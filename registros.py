from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/registros")
def ver_registros(request: Request):
    lista_registros = [] # Substitua pela sua lógica/banco
    return templates.TemplateResponse("registros.html", {
        "request": request, 
        "registros": lista_registros
    })
