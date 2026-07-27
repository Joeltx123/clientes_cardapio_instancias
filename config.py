from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/config")
def ver_config(request: Request):
    configuracoes = {} # Substitua pela sua lógica/banco
    return templates.TemplateResponse("config.html", {
        "request": request, 
        "config": configuracoes
    })
