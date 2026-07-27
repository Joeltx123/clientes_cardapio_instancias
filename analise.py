from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/analise")
def ver_analise(request: Request):
    dados_analise = {} # Substitua pela sua lógica/banco
    return templates.TemplateResponse("analise.html", {
        "request": request, 
        "analise": dados_analise
    })
