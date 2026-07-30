from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/{slug}/pagamento", response_class=HTMLResponse)
def pagamento_page(request: Request, slug: str):
    config_data = {"quantidade_mesas": 0, "nome": "Cardápio Pro"}
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT quantidade_mesas, nome FROM configuracao LIMIT 1;")
        res = cursor.fetchone()
        if res:
            config_data["quantidade_mesas"] = res[0] if res[0] is not None else 0
            config_data["nome"] = res[1] if res[1] is not None else "Cardápio Pro"
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"[ERRO CONFIG PAGAMENTO] {str(e)}")

    return templates.TemplateResponse(
        request,
        "pagamento.html",
        {
            "request": request,
            "slug": slug,
            "config": config_data
        }
    )

# API para buscar pagamentos pendentes (Mesas e Delivery separados)
@router.get("/{slug}/api/pagamentos-pendentes")
async def api_pagamentos_pendentes(slug: str):
    try:
        db = get_db()
        cursor = db.cursor()

        # 1. Mesas (tabela pedidos tradicional)
        cursor.execute("""
            SELECT id, mesa, total, forma_pagamento, status
            FROM pedidos
            WHERE tenant = %s AND (status IS NULL OR status != 'pago')
            ORDER BY id DESC;
        """, (slug,))
        mesas_rows = cursor.fetchall()

        mesas = []
        for m in mesas_rows:
            mesas.append({
                "id": m[0],
                "mesa": m[1],
                "total": float(m[2]),
                "forma_pagamento": m[3],
                "status": m[4] or "pendente"
            })

        # 2. Delivery (tabela pedidos_delivery com fluxo de clique e rota)
        cursor.execute("""
            SELECT id, cliente_nome, endereco_entrega, bairro, total, forma_pagamento, status
            FROM pedidos_delivery
            WHERE tenant = %s AND status != 'entregue'
            ORDER BY id DESC;
        """, (slug,))
        delivery_rows = cursor.fetchall()

        entregas = []
        for d in delivery_rows:
            entregas.append({
                "id": d[0],
                "cliente_nome": d[1],
                "endereco": f"{d[2]} ({d[3]})",
                "total": float(d[4]),
                "forma_pagamento": d[5],
                "status": d[6]
            })

        cursor.close()
        db.close()

        return JSONResponse({
            "status": "sucesso",
            "mesas": mesas,
            "delivery": entregas
        })
    except Exception as e:
        print(f"[ERRO API PAGAMENTOS PENDENTES] {str(e)}")
        return JSONResponse({"status": "erro", "mesas": [], "delivery": []})

# API para Funcionário liberar pagamento por clique (Delivery)
@router.post("/{slug}/api/delivery-liberar-pagamento/{pedido_id}")
async def api_delivery_liberar_pagamento(slug: str, pedido_id: int):
    try:
        db = get_db()
        cursor = db.cursor()
        # Atualiza status para pago e aguardando rota
        cursor.execute("""
            UPDATE pedidos_delivery
            SET status = 'pago_aguardando_rota'
            WHERE id = %s AND tenant = %s;
        """, (pedido_id, slug))
        db.commit()
        cursor.close()
        db.close()
        return JSONResponse({"status": "sucesso", "mensagem": "Pagamento liberado com sucesso!"})
    except Exception as e:
        return JSONResponse({"status": "erro", "detalhe": str(e)})

# API para Funcionário acionar o botão 'Pedido em Rota' (libera o cliente para novo pedido)
@router.post("/{slug}/api/delivery-pedido-rota/{pedido_id}")
async def api_delivery_pedido_rota(slug: str, pedido_id: int):
    try:
        db = get_db()
        cursor = db.cursor()
        # Atualiza status para em_rota ou entregue
        cursor.execute("""
            UPDATE pedidos_delivery
            SET status = 'em_rota'
            WHERE id = %s AND tenant = %s;
        """, (pedido_id, slug))
        db.commit()
        cursor.close()
        db.close()
        return JSONResponse({"status": "sucesso", "mensagem": "Pedido colocado em rota de entrega!"})
    except Exception as e:
        return JSONResponse({"status": "erro", "detalhe": str(e)})
