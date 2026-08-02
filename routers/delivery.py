import json
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/{tenant}/delivery", response_class=HTMLResponse)
def painel_delivery(request: Request, tenant: str):
    return templates.TemplateResponse(
        request,
        "delivery.html",
        {
            "request": request,
            "tenant": tenant,
            "slug": tenant
        }
    )

@router.get("/admin/{tenant}/api/delivery-pedidos")
async def api_delivery_pedidos(tenant: str):
    try:
        db = get_db()
        cursor = db.cursor()

        cursor.execute("""
            SELECT id, tenant, cliente_nome, cliente_telefone, endereco_entrega, bairro, itens, total, forma_pagamento, status, horario 
            FROM pedidos_delivery 
            WHERE tenant = %s 
            ORDER BY id DESC;
        """, (tenant,))
        rows = cursor.fetchall()
        cursor.close()
        db.close()

        pedidos = []
        for r in rows:
            # Tratamento seguro caso os itens venham como string JSON ou lista
            itens_val = r["itens"] if isinstance(r, dict) else (r[6] if len(r) > 6 else [])
            if isinstance(itens_val, str):
                try:
                    itens_val = json.loads(itens_val)
                except:
                    itens_val = []

            pedidos.append({
                "id": r["id"] if isinstance(r, dict) else r[0],
                "cliente_nome": r["cliente_nome"] if isinstance(r, dict) else (r[2] if len(r) > 2 else "Cliente"),
                "telefone": r["cliente_telefone"] if isinstance(r, dict) else (r[3] if len(r) > 3 else ""),
                "endereco_entrega": r["endereco_entrega"] if isinstance(r, dict) else (r[4] if len(r) > 4 else ""),
                "bairro": r["bairro"] if isinstance(r, dict) else (r[5] if len(r) > 5 else ""),
                "itens": itens_val,
                "total": float(r["total"]) if (isinstance(r, dict) and r["total"] is not None) or (not isinstance(r, dict) and len(r) > 7 and r[7] is not None) else 0.0,
                "forma_pagamento": r["forma_pagamento"] if isinstance(r, dict) else (r[8] if len(r) > 8 else "Dinheiro"),
                "status": r["status"] if isinstance(r, dict) else (r[9] if len(r) > 9 else "Pendente"),
                "horario": str(r["horario"] if isinstance(r, dict) else (r[10] if len(r) > 10 else ""))
            })

        return JSONResponse({"status": "sucesso", "pedidos": pedidos})
    except Exception as e:
        print(f"[ERRO API DELIVERY] {str(e)}")
        return JSONResponse({"status": "erro", "detalhe": str(e), "pedidos": []}, status_code=400)

class StatusUpdate(BaseModel):
    status: str

@router.post("/admin/{tenant}/api/delivery-status/{pedido_id}")
async def api_delivery_status(tenant: str, pedido_id: int, payload: StatusUpdate):
    try:
        db = get_db()
        cursor = db.cursor()
        
        cursor.execute("""
            UPDATE pedidos_delivery
            SET status = %s
            WHERE id = %s AND tenant = %s;
        """, (payload.status, pedido_id, tenant))
        
        db.commit()
        cursor.close()
        db.close()
        return JSONResponse({"status": "sucesso", "mensagem": "Status do delivery atualizado com sucesso!"})
    except Exception as e:
        if db:
            db.rollback()
        print(f"[ERRO ATUALIZAR STATUS DELIVERY] {str(e)}")
        return JSONResponse({"status": "erro", "detalhe": str(e)}, status_code=400)
