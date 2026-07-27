from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/pagamento")
def ver_pagamento(request: Request):
    # Lógica de pagamento do seu projeto
    dados_pagamento = {"status": "Aguardando pagamento"}
    return templates.TemplateResponse("pagamento.html", {
        "request": request, 
        "pagamento": dados_pagamento
    })
