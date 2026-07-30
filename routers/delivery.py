from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/{tenant}/delivery", response_class=HTMLResponse)
def painel_delivery(request: Request, tenant: str):
    db = get_db()
    cursor = db.cursor()
    
    pedidos = []
    try:
        cursor.execute("SELECT id, tenant, cliente_nome, cliente_telefone, endereco_entrega, bairro, itens, total, forma_pagamento, status, horario FROM pedidos_delivery WHERE tenant = %s ORDER BY id DESC;", (tenant,))
        rows = cursor.fetchall()
        for r in rows:
            # Como o psycopg2 retorna RealDictRow ou dicionários, extraímos diretamente pelas chaves reais
            pedidos.append({
                "id": r["id"] if isinstance(r, dict) else r[0],
                "cliente_nome": r["cliente_nome"] if isinstance(r, dict) else (r[2] if len(r) > 2 else "Cliente"),
                "telefone": r["cliente_telefone"] if isinstance(r, dict) else (r[3] if len(r) > 3 else ""),
                "endereco_entrega": r["endereco_entrega"] if isinstance(r, dict) else (r[4] if len(r) > 4 else ""),
                "bairro": r["bairro"] if isinstance(r, dict) else (r[5] if len(r) > 5 else ""),
                "itens": r["itens"] if isinstance(r, dict) else (r[6] if len(r) > 6 else []),
                "total": float(r["total"]) if isinstance(r, dict) and r["total"] is not None else 0.0,
                "forma_pagamento": r["forma_pagamento"] if isinstance(r, dict) else "Dinheiro",
                "status": r["status"] if isinstance(r, dict) else "Pendente"
            })
    except Exception as e:
        print(f"Erro ao buscar pedidos delivery: {e}")
        
    cursor.close()
    db.close()
    
    return templates.TemplateResponse(
        request,
        "delivery.html",
        {
            "request": request,
            "tenant": tenant,
            "pedidos": pedidos
        }
    )
