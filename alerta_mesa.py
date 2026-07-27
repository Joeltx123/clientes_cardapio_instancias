from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/alerta-mesa")
def ver_alerta_mesa(request: Request):
    alertas = [] # Substitua pela sua lógica/banco
    return templates.TemplateResponse("alerta_mesa.html", {
        "request": request, 
        "alertas": alertas
    })
