from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sisyten.cardapio import cardapio

router = APIRouter()

@router.get("/cardapio", response_class=HTMLResponse)
def rota_cardapio_get(request: Request):
    produtos = cardapio.listar_cardapio(apenas_ativos=False)
    return request.app.state.templates.TemplateResponse(
        request, "cardapio.html", {"request": request, "produtos": produtos}
    )

@router.post("/cardapio/cadastrar")
def rota_cadastrar(nome: str = Form(...), preco: float = Form(...), categoria: str = Form(...), descricao: str = Form(""), foto_url: str = Form("")):
    cardapio.salvar_produto(nome, preco, categoria, descricao, foto_url)
    return RedirectResponse(url="/cardapio", status_code=303)

@router.post("/cardapio/visibilidade")
def rota_visibilidade(id: int = Form(...), visivel: str = Form(...)):
    novo_status = True if visivel == 'true' else False
    cardapio.alterar_visibilidade(id, novo_status)
    return RedirectResponse(url="/cardapio", status_code=303)

@router.post("/cardapio/arquivar")
def rota_arquivar(id: int = Form(...)):
    cardapio.arquivar_produto(id)
    return RedirectResponse(url="/cardapio", status_code=303)
