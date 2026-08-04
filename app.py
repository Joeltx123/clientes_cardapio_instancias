from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json

from sisyten import configuracao, qr_code, pedidos, cardapio, delivery, pagamento, analise, backup

app = FastAPI(title="Cardápio Pro - Sisyten", version="1.0")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request, "base.html", {})

@app.get("/configuracao", response_class=HTMLResponse)
async def tela_configuracao(request: Request):
    try:
        res = json.loads(configuracao.processar_requisicao(json.dumps({"acao": "consultar", "dados": {"slug": "estabelecimento"}})))
        dados = res.get("dados", {})
    except Exception:
        dados = {}
    return templates.TemplateResponse(request, "configuracao.html", {"dados": dados})



@app.post("/configuracao", response_class=HTMLResponse)
async def salvar_configuracao(request: Request):
    form = await request.form()
    dados_form = dict(form)
    
    payload = {
        "acao": "salvar",
        "dados": dados_form
    }
    
    try:
        resposta_json = configuracao.processar_requisicao(json.dumps(payload))
        res = json.loads(resposta_json)
        mensagem = res.get("mensagem", "Operação realizada.")
    except Exception as e:
        mensagem = f"Erro ao processar: {str(e)}"
        res = {"status": "erro"}

    try:
        res_cons = json.loads(configuracao.processar_requisicao(json.dumps({"acao": "consultar", "dados": {"slug": "estabelecimento"}})))
        dados = res_cons.get("dados", {})
    except Exception:
        dados = {}

    return templates.TemplateResponse(request, "configuracao.html", {"dados": dados, "mensagem": mensagem})



@app.get("/cardapio", response_class=HTMLResponse)
async def tela_cardapio(request: Request):
    try:
        res_json = cardapio.processar_requisicao(json.dumps({"acao": "consultar", "dados": {}}))
        res = json.loads(res_json)
        produtos = res.get("produtos", []) if isinstance(res, dict) else []
    except Exception as e:
        print("Erro ao carregar cardapio:", e)
        produtos = []

    return templates.TemplateResponse(request, "cardapio.html", {"produtos": produtos, "slug": "estabelecimento"})
@app.get("/pedidos", response_class=HTMLResponse)
async def tela_pedidos(request: Request):
    try:
        res = json.loads(pedidos.processar_requisicao(json.dumps({"acao": "consultar_painel"})))
        dados = res if res.get("status") == "sucesso" else {}
    except Exception:
        dados = {}
    return templates.TemplateResponse(request, "pedidos.html", {"dados": dados})

@app.get("/delivery", response_class=HTMLResponse)
async def tela_delivery(request: Request):
    return templates.TemplateResponse(request, "delivery.html", {})

@app.post("/api/delivery")
async def api_delivery(request: Request):
    body = await request.json()
    resposta_json = delivery.processar_requisicao(body)
    return json.loads(resposta_json)


@app.get("/pagamento", response_class=HTMLResponse)
async def tela_pagamento(request: Request):
    return templates.TemplateResponse(request, "pagamento.html", {})


@app.post("/api/analise")
async def api_analise(request: Request):
    body = await request.json()
    resposta_json = analise.processar_requisicao(body)
    return json.loads(resposta_json)

@app.post("/api/pagamento")
async def api_pagamento(request: Request):
    body = await request.json()
    resposta_json = pagamento.processar_requisicao(body)
    return json.loads(resposta_json)


@app.get("/analise", response_class=HTMLResponse)
async def tela_analise(request: Request):
    return templates.TemplateResponse(request, "analise.html", {})


@app.get("/backup", response_class=HTMLResponse)
async def tela_backup(request: Request):
    return templates.TemplateResponse(request, "backup.html", {})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

# --- ROTAS DO CARDÁPIO (Integradas com cardapio.py) ---
from fastapi import Request, Form
from fastapi.responses import RedirectResponse
from sisyten.cardapio import (
    consultar_cardapio,
    listar_arquivados,
    cadastrar_produto,
    alterar_visibilidade,
    arquivar_ou_desarquivar,
    excluir_produto_definitivamente
)

SLUG_PADRAO = "estabelecimento"


@app.get("/cardapio", response_class=HTMLResponse)
async def tela_cardapio(request: Request):
    try:
        res_json = cardapio.processar_requisicao(json.dumps({"acao": "consultar", "dados": {}}))
        res = json.loads(res_json)
        produtos = res.get("produtos", []) if isinstance(res, dict) else []
    except Exception as e:
        print("Erro ao carregar cardapio:", e)
        produtos = []

    return templates.TemplateResponse(request, "cardapio.html", {"produtos": produtos, "slug": "estabelecimento"})
@app.post("/cardapio/cadastrar")
def rota_cadastrar(slug: str = Form(...), categoria: str = Form(...), nome: str = Form(...), preco: float = Form(...), foto_url: str = Form(None), descricao: str = Form(None)):
    dados = {
        "slug": slug,
        "categoria": categoria,
        "nome": nome,
        "preco": preco,
        "foto_url": foto_url,
        "descricao": descricao
    }
    cadastrar_produto(dados)
    return RedirectResponse(url="/cardapio", status_code=303)

@app.post("/cardapio/visibilidade")
def rota_visibilidade(id: int = Form(...), visivel: bool = Form(...)):
    alterar_visibilidade({"id": id, "visivel": visivel})
    return RedirectResponse(url="/cardapio", status_code=303)

@app.get("/cardapio/arquivados")
def ver_arquivados(request: Request):
    resposta = listar_arquivados({"slug": SLUG_PADRAO})
    produtos = resposta.get("produtos_arquivados", []) if resposta.get("status") == "sucesso" else []
    return templates.TemplateResponse(request, "cardapio_arquivados.html", {"produtos": produtos, "slug": SLUG_PADRAO})

@app.post("/cardapio/desarquivar")
def rota_desarquivar(id: int = Form(...)):
    arquivar_ou_desarquivar({"id": id, "arquivado": False})
    return RedirectResponse(url="/cardapio/arquivados", status_code=303)

@app.post("/cardapio/excluir")
def rota_excluir(id: int = Form(...)):
    excluir_produto_definitivamente({"id": id})
    return RedirectResponse(url="/cardapio/arquivados", status_code=303)


@app.get("/qrcode", response_class=HTMLResponse)
@app.get("/qr-code", response_class=HTMLResponse)
async def tela_qr_code(request: Request):
    try:
        res = json.loads(qr_code.processar_requisicao(json.dumps({"acao": "consultar"})))
        # Ajusta para pegar a estrutura correta retornada pelo modulo qr_code
        if isinstance(res, dict) and "dados" in res:
            dados = res["dados"]
        else:
            dados = res if isinstance(res, dict) else {}
    except Exception as e:
        dados = {"status": "erro", "mensagem": str(e)}
    return templates.TemplateResponse(request, "qr_code.html", {"dados": dados})

@app.post("/cardapio/arquivar")
async def cardapio_arquivar(
    id: int = Form(...),
    arquivado: str = Form(...)
):
    # Converte a string do form para booleano real
    arq_bool = True if str(arquivado).lower() == "true" else False
    payload = {
        "acao": "arquivar",
        "dados": {
            "id": id,
            "arquivado": arq_bool
        }
    }
    cardapio.processar_requisicao(json.dumps(payload))
    return RedirectResponse(url="/cardapio", status_code=303)
