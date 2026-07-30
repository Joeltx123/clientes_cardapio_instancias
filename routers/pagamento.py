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

@router.get("/{slug}/api/pagamentos-pendentes")
async def api_pagamentos_pendentes(slug: str):
    try:
        db = get_db()
        cursor = db.cursor()

        # 1. Mesas (tabela pedidos adaptada para ler com segurança)
        mesas = []
        try:
            cursor.execute("""
                SELECT id, mesa, total, 
                       COALESCE(forma_pagamento, 'Dinheiro') as forma_pagamento, 
                       COALESCE(status, 'pendente') as status
                FROM pedidos
                WHERE (status IS NULL OR status != 'pago')
                ORDER BY id DESC;
            """)
            mesas_rows = cursor.fetchall()
            for m in mesas_rows:
                if isinstance(m, dict):
                    mesas.append({
                        "id": m.get("id"),
                        "mesa": m.get("mesa", 1),
                        "total": float(m.get("total", 0.0)),
                        "forma_pagamento": m.get("forma_pagamento", "Dinheiro"),
                        "status": m.get("status", "pendente")
                    })
                else:
                    mesas.append({
                        "id": m[0],
                        "mesa": m[1] if len(m) > 1 else 1,
                        "total": float(m[2]) if len(m) > 2 and m[2] is not None else 0.0,
                        "forma_pagamento": m[3] if len(m) > 3 and m[3] else "Dinheiro",
                        "status": m[4] if len(m) > 4 and m[4] else "pendente"
                    })
        except Exception as e:
            print(f"[ERRO QUERY PEDIDOS MESAS] {e}")

        # 2. Delivery (tabela pedidos_delivery)
        entregas = []
        try:
            cursor.execute("""
                SELECT id, cliente_nome, endereco_entrega, bairro, total, forma_pagamento, status
                FROM pedidos_delivery
                WHERE tenant = %s AND status != 'entregue'
                ORDER BY id DESC;
            """, (slug,))
            delivery_rows = cursor.fetchall()
            for d in delivery_rows:
                if isinstance(d, dict):
                    entregas.append({
                        "id": d.get("id"),
                        "cliente_nome": d.get("cliente_nome", ""),
                        "endereco": f"{d.get('endereco_entrega', '')} ({d.get('bairro', '')})",
                        "total": float(d.get("total", 0.0)),
                        "forma_pagamento": d.get("forma_pagamento", ""),
                        "status": d.get("status", "")
                    })
                else:
                    entregas.append({
                        "id": d[0],
                        "cliente_nome": d[1] if len(d) > 1 else "",
                        "endereco": f"{d[2] if len(d) > 2 else ''} ({d[3] if len(d) > 3 else ''})",
                        "total": float(d[4]) if len(d) > 4 and d[4] is not None else 0.0,
                        "forma_pagamento": d[5] if len(d) > 5 else "",
                        "status": d[6] if len(d) > 6 else ""
                    })
        except Exception as e:
            print(f"[ERRO QUERY DELIVERY] {e}")

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

@router.post("/{slug}/api/delivery-liberar-pagamento/{pedido_id}")
async def api_delivery_liberar_pagamento(slug: str, pedido_id: int):
    try:
        db = get_db()
        cursor = db.cursor()
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

@router.post("/{slug}/api/delivery-pedido-rota/{pedido_id}")
async def api_delivery_pedido_rota(slug: str, pedido_id: int):
    try:
        db = get_db()
        cursor = db.cursor()
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
