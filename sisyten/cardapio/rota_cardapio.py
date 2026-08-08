from fastapi import APIRouter, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from sisyten.cardapio import cardapio

router = APIRouter()

@router.get("/cardapio", response_class=HTMLResponse)
def rota_cardapio_get(request: Request):
    produtos = cardapio.listar_cardapio(apenas_ativos=False)
    return request.app.state.templates.TemplateResponse(
        request, "cardapio.html", {"request": request, "produtos": produtos}
    )

@router.get("/cardapio/arquivados", response_class=HTMLResponse)
def rota_cardapio_arquivados_get(request: Request):
    produtos = cardapio.listar_arquivados() if hasattr(cardapio, 'listar_arquivados') else []
    return request.app.state.templates.TemplateResponse(
        request, "cardapio_arquivados.html", {"request": request, "produtos": produtos}
    )

@router.post("/cardapio/cadastrar")
def rota_cadastrar(
    nome: str = Form(...), 
    preco: float = Form(...), 
    categoria: str = Form(...), 
    descricao: str = Form(""), 
    foto_url: str = Form(""),
    foto_arquivo: UploadFile = File(None)
):
    cardapio.salvar_produto(nome, preco, categoria, descricao, foto_url, foto_arquivo)
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

@router.post("/cardapio/desarquivar")
def rota_desarquivar(id: int = Form(...)):
    if hasattr(cardapio, 'desarquivar_produto'):
        cardapio.desarquivar_produto(id)
    return RedirectResponse(url="/cardapio/arquivados", status_code=303)

@router.post("/cardapio/excluir")
def rota_excluir(id: int = Form(...)):
    if hasattr(cardapio, 'excluir_produto'):
        cardapio.excluir_produto(id)
    return RedirectResponse(url="/cardapio/arquivados", status_code=303)

from fastapi import UploadFile, File, Form
from fastapi.responses import RedirectResponse
from sisyten.cardapio import cardapio

@router.post("/cardapio/foto/{produto_id}")
async def alterar_foto_rota(produto_id: int, foto_arquivo: UploadFile = File(None), remover: bool = Form(False)):
    cardapio.atualizar_foto_produto(produto_id, foto_arquivo=foto_arquivo, remover=remover)
    return RedirectResponse(url="/cardapio", status_code=303)
