from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cardapio")
def ver_cardapio(request: Request):
    # Insira aqui a sua consulta real ao banco de dados se necessário
    itens_do_banco = [
        {"nome": "Hambúrguer Clássico", "descricao": "Pão, carne e queijo", "preco": "25,00"},
        {"nome": "Pizza Margherita", "descricao": "Molho, mussarela e manjericão", "preco": "45,00"}
    ]
    return templates.TemplateResponse("cardapio.html", {
        "request": request, 
        "itens": itens_do_banco
    })
