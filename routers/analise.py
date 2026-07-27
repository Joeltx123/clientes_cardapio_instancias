from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/analise", response_class=HTMLResponse)
def relatorio_analise(request: Request):
    db = get_db()
    cursor = db.cursor()
    
    # Total faturado e quantidade total de pedidos
    cursor.execute("SELECT COALESCE(SUM(total), 0) as faturamento_total, COUNT(*) as total_pedidos FROM pedidos")
    resumo = cursor.fetchone()
    
    # Vendas agrupadas por forma de pagamento
    cursor.execute("SELECT forma_pagamento, COALESCE(SUM(total), 0) as total, COUNT(*) as qtd FROM pedidos GROUP BY forma_pagamento")
    por_pagamento = cursor.fetchall()
    
    cursor.close()
    db.close()
    
    return templates.TemplateResponse(
        request, 
        "analise.html", 
        {
            "resumo": resumo,
            "por_pagamento": por_pagamento
        }
    )
