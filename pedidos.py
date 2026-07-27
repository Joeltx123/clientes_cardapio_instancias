from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/pedidos")
def ver_pedidos(request: Request):
    # Insira aqui a sua consulta real ao banco de dados se necessário
    pedidos_do_banco = [
        {"id": 101, "cliente": "Carlos Silva", "status": "Pendente", "total": "70,00"},
        {"id": 102, "cliente": "Ana Souza", "status": "Em preparo", "total": "25,00"}
    ]
    return templates.TemplateResponse("pedidos.html", {
        "request": request, 
        "pedidos": pedidos_do_banco
    })
