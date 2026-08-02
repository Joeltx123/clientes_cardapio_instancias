import re
from pydantic import BaseModel
from fastapi import APIRouter, Request
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
        cursor.execute("SELECT quantidade_mesas FROM configuracao LIMIT 1;")
        res = cursor.fetchone()
        if res and res[0] is not None:
            config_data["quantidade_mesas"] = res[0]
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

        # 1. Mesas
        mesas = []
        try:
            cursor.execute("""
                SELECT id, mesa, total,
                       COALESCE(forma_pagamento, 'Dinheiro') as forma_pagamento,
                       COALESCE(status, 'pendente') as status
                FROM pedidos
                WHERE (status IS NULL OR LOWER(status) != 'pago')
                ORDER BY id DESC;
            """)
            mesas_rows = cursor.fetchall()
            for m in mesas_rows:
                status_val = m[4] if not isinstance(m, dict) else m.get("status", "pendente")
                status_str = "Pendente" if status_val.lower() in ["pendente", "pend"] else status_val

                if isinstance(m, dict):
                    mesas.append({
                        "id": m.get("id"),
                        "mesa": m.get("mesa", 1),
                        "total": float(m.get("total", 0.0)),
                        "forma_pagamento": m.get("forma_pagamento", "Dinheiro"),
                        "status": status_str
                    })
                else:
                    mesas.append({
                        "id": m[0],
                        "mesa": m[1] if len(m) > 1 else 1,
                        "total": float(m[2]) if len(m) > 2 and m[2] is not None else 0.0,
                        "forma_pagamento": m[3] if len(m) > 3 and m[3] else "Dinheiro",
                        "status": status_str
                    })
        except Exception as e:
            print(f"[ERRO QUERY PEDIDOS MESAS] {e}")

        # 2. Delivery
        entregas = []
        try:
            cursor.execute("""
                SELECT id, cliente_nome, endereco_entrega, bairro, total, forma_pagamento, status
                FROM pedidos_delivery
                WHERE tenant = %s AND LOWER(status) != 'entregue'
                ORDER BY id DESC;
            """, (slug,))
            delivery_rows = cursor.fetchall()
            for d in delivery_rows:
                status_val = d[6] if not isinstance(d, dict) else d.get("status", "pendente")
                status_str = "Pendente" if status_val.lower() in ["pendente", "pend", "aguardando"] else status_val

                if isinstance(d, dict):
                    entregas.append({
                        "id": d.get("id"),
                        "cliente_nome": d.get("cliente_nome", ""),
                        "endereco": f"{d.get('endereco_entrega', '')} ({d.get('bairro', '')})",
                        "total": float(d.get("total", 0.0)),
                        "forma_pagamento": d.get("forma_pagamento", ""),
                        "status": status_str
                    })
                else:
                    entregas.append({
                        "id": d[0],
                        "cliente_nome": d[1] if len(d) > 1 else "",
                        "endereco": f"{d[2] if len(d) > 2 else ''} ({d[3] if len(d) > 3 else ''})",
                        "total": float(d[4]) if len(d) > 4 and d[4] is not None else 0.0,
                        "forma_pagamento": d[5] if len(d) > 5 else "",
                        "status": status_str
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

class PagamentoRequest(BaseModel):
    forma_pagamento: str
    parcelas: int = 1
    troco: float = 0.0
    tipo: str = "mesa"

@router.post("/{slug}/api/pagamento-concluir/{pedido_id}")
async def api_pagamento_concluir(slug: str, pedido_id: int, payload: PagamentoRequest):
    try:
        db = get_db()
        cursor = db.cursor()

        forma_final = f"{payload.forma_pagamento} ({payload.parcelas}x)" if payload.forma_pagamento == "Cartão de Crédito" and payload.parcelas > 1 else payload.forma_pagamento

        total_pedido = 0.0
        mesa_inteiro = 0

        if payload.tipo == "delivery":
            cursor.execute("""
                UPDATE pedidos_delivery
                SET status = 'entregue', forma_pagamento = %s
                WHERE id = %s AND tenant = %s
                RETURNING total, cliente_nome;
            """, (forma_final, pedido_id, slug))
            res_del = cursor.fetchone()
            if res_del:
                total_pedido = float(res_del[0] if isinstance(res_del, tuple) else res_del["total"])
                cliente_nome = res_del[1] if isinstance(res_del, tuple) else res_del.get("cliente_nome", "Delivery")
                # Se a coluna mesa aceitar string ou int, para delivery podemos mandar 0 ou ID
                mesa_inteiro = 0 
        else:
            cursor.execute("SELECT mesa, total FROM pedidos WHERE id = %s;", (pedido_id,))
            p_info = cursor.fetchone()
            if p_info:
                mesa_val = p_info[0] if isinstance(p_info, tuple) else p_info["mesa"]
                # Extrai apenas números caso venha string como "Mesa 3"
                if isinstance(mesa_val, str):
                    nums = re.findall(r'\d+', mesa_val)
                    mesa_inteiro = int(nums[0]) if nums else 1
                else:
                    mesa_inteiro = int(mesa_val) if mesa_val else 1

                total_pedido = float(p_info[1] if isinstance(p_info, tuple) else p_info["total"])

            cursor.execute("""
                UPDATE pedidos
                SET status = 'pago', forma_pagamento = %s, troco = %s
                WHERE id = %s;
            """, (forma_final, payload.troco, pedido_id))

        # Salva na tabela registros_caixa com mesa sendo inteiro
        cursor.execute("""
            INSERT INTO registros_caixa (tenant, mesa, forma_pagamento, total, troco, horario)
            VALUES (%s, %s, %s, %s, %s, NOW());
        """, (slug, mesa_inteiro, forma_final, total_pedido, payload.troco))

        db.commit()
        cursor.close()
        db.close()
        return JSONResponse({"status": "sucesso", "mensagem": "Pagamento concluído e salvo com sucesso!"})
    except Exception as e:
        if db:
            db.rollback()
        print(f"[ERRO PAGAMENTO CONCLUIR] {str(e)}")
        return JSONResponse({"status": "erro", "detalhe": str(e)}, status_code=400)
