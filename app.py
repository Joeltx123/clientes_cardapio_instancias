import os
import json
from fastapi import FastAPI, Request, Query, Form
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sisyten import pedidos, cardapio, analise, backup, json_core, configuracao, delivery, pagamento
import digital

app = FastAPI(title="Sistema Cardápio Instâncias")
templates = Jinja2Templates(directory="templates")

app.include_router(digital.router)

@app.get("/", response_class=HTMLResponse)
def raiz(request: Request):
    return templates.TemplateResponse(request, "index.html", {})

@app.get("/pedidos", response_class=HTMLResponse)
def rota_pedidos(request: Request):
    try:
        dados = pedidos.consultar_pedidos_e_mesas()
        return templates.TemplateResponse(request, "pedidos.html", {"dados": dados})
    except Exception as e:
        return templates.TemplateResponse(request, "pedidos.html", {"dados": {"mesas": []}})

@app.post("/liberar-mesa")
def liberar_mesa(mesa: int = Form(...)):
    try:
        payload = {"acao": "liberar_mesa", "mesa": mesa}
        pedidos.processar_requisicao(json.dumps(payload))
    except Exception as e:
        print(f"Erro ao liberar mesa: {e}")
    return RedirectResponse(url="/pedidos", status_code=303)

@app.get("/cardapio", response_class=HTMLResponse)
def rota_cardapio(request: Request):
    try:
        itens = cardapio.listar_cardapio()
        return templates.TemplateResponse(request, "cardapio.html", {"cardapio": itens})
    except Exception as e:
        return templates.TemplateResponse(request, "cardapio.html", {"cardapio": []})

@app.post("/cardapio/cadastrar")
def cadastrar_produto(
    nome: str = Form(...),
    preco: float = Form(...),
    categoria: str = Form(...),
    foto_url: str = Form(None),
    descricao: str = Form(None),
    slug: str = Form("estabelecimento")
):
    try:
        itens = cardapio.listar_cardapio()
        novo_id = max([p.get("id", 0) for p in itens], default=0) + 1
        
        novo_produto = {
            "id": novo_id,
            "nome": nome,
            "preco": preco,
            "categoria": categoria,
            "foto_url": foto_url or "",
            "descricao": descricao or "",
            "visivel": True,
            "arquivado": False,
            "slug": slug
        }
        
        itens.append(novo_produto)
        cardapio.salvar_cardapio(itens)
    except Exception as e:
        print(f"Erro ao salvar produto: {e}")
        
    return RedirectResponse(url="/cardapio", status_code=303)

@app.post("/cardapio/visibilidade")
def alterar_visibilidade(id: int = Form(...), visivel: str = Form(...)):
    try:
        itens = cardapio.listar_cardapio()
        novo_status = True if visivel.lower() == "true" else False
        for p in itens:
            if p.get("id") == id:
                p["visivel"] = novo_status
        cardapio.salvar_cardapio(itens)
    except Exception as e:
        print(f"Erro ao alterar visibilidade: {e}")
        
    return RedirectResponse(url="/cardapio", status_code=303)

@app.post("/cardapio/arquivar")
def arquivar_produto(id: int = Form(...)):
    try:
        itens = cardapio.listar_cardapio()
        for p in itens:
            if p.get("id") == id:
                p["arquivado"] = True
                p["visivel"] = False
        cardapio.salvar_cardapio(itens)
    except Exception as e:
        print(f"Erro ao arquivar produto: {e}")
        
    return RedirectResponse(url="/cardapio", status_code=303)

@app.get("/cardapio/arquivados", response_class=HTMLResponse)
def cardapio_arquivados(request: Request):
    try:
        itens = cardapio.listar_cardapio()
        arquivados = [p for p in itens if p.get("arquivado")]
        return templates.TemplateResponse(request, "cardapio_arquivados.html", {"cardapio": arquivados})
    except Exception:
        return templates.TemplateResponse(request, "cardapio_arquivados.html", {"cardapio": []})

@app.post("/cardapio/desarquivar")
def desarquivar_produto(id: int = Form(...)):
    try:
        itens = cardapio.listar_cardapio()
        for p in itens:
            if p.get("id") == id:
                p["arquivado"] = False
                p["visivel"] = True
        cardapio.salvar_cardapio(itens)
    except Exception as e:
        print(f"Erro ao desarquivar produto: {e}")
    return RedirectResponse(url="/cardapio/arquivados", status_code=303)

@app.post("/cardapio/excluir")
def excluir_produto(id: int = Form(...)):
    try:
        itens = cardapio.listar_cardapio()
        itens = [p for p in itens if p.get("id") != id]
        cardapio.salvar_cardapio(itens)
    except Exception as e:
        print(f"Erro ao excluir produto: {e}")
    return RedirectResponse(url="/cardapio/arquivados", status_code=303)

@app.get("/delivery", response_class=HTMLResponse)
def rota_delivery(request: Request):
    return templates.TemplateResponse(request, "delivery.html", {})

@app.post("/api/delivery", response_class=JSONResponse)
async def api_delivery(request: Request):
    try:
        body = await request.json()
        bairro = body.get("bairro", "")
        taxa = delivery.calcular_taxa_delivery(bairro)
        return {"status": "sucesso", "taxa": taxa}
    except Exception as e:
        return {"status": "erro", "mensagem": str(e)}

@app.get("/configuracao", response_class=HTMLResponse)
def rota_configuracao(request: Request):
    cfg = json_core.ler_json_seguro("dados/configuracao.json", {})
    return templates.TemplateResponse(request, "configuracao.html", {"config": cfg})

@app.post("/configuracao")
async def salvar_configuracao(request: Request):
    form_data = await request.form()
    dados = dict(form_data)
    configuracao.salvar_ou_atualizar_configuracao(dados)
    return RedirectResponse(url="/configuracao", status_code=303)

@app.get("/pagamento", response_class=HTMLResponse)
def rota_pagamento(request: Request):
    return templates.TemplateResponse(request, "pagamento.html", {})

@app.post("/api/pagamento", response_class=JSONResponse)
async def api_pagamento(request: Request):
    try:
        body = await request.json()
        resultado = pagamento.processar_requisicao(body)
        return resultado
    except Exception as e:
        return {"status": "erro", "mensagem": str(e)}

@app.get("/backup", response_class=HTMLResponse)
def rota_backup(request: Request):
    return templates.TemplateResponse(request, "backup.html", {})

@app.post("/backup/gerar", response_class=JSONResponse)
def executar_backup(slug: str = Form(...)):
    payload = {
        "acao": "gerar_backup",
        "dados": {
            "slug": slug,
            "pasta_destino": os.path.expanduser("~/Downloads")
        }
    }
    resultado_str = backup.processar_requisicao(json.dumps(payload))
    return json.loads(resultado_str)

@app.get("/qrcode", response_class=HTMLResponse)
def rota_qrcode(request: Request):
    base_url = str(request.base_url).rstrip("/")
    config = json_core.ler_json_seguro("dados/configuracao.json", {
        "nome_estabelecimento": "Meu Estabelecimento",
        "mesas": 5
    })

    nome_est = config.get("nome_estabelecimento", "Meu Estabelecimento")
    mesas_raw = config.get("mesas", 5)
    lista_mesas_processada = []

    if isinstance(mesas_raw, int):
        range_mesas = range(1, mesas_raw + 1)
    elif isinstance(mesas_raw, list):
        range_mesas = mesas_raw
    else:
        range_mesas = range(1, 6)

    for item in range_mesas:
        num_mesa = item.get("mesa") if isinstance(item, dict) else item
        link_mesa = f"{base_url}/mesa/cardapio?mesa={num_mesa}"
        lista_mesas_processada.append({
            "mesa": num_mesa,
            "link_acesso": link_mesa
        })

    dados_contexto = {
        "status": "sucesso",
        "nome_estabelecimento": nome_est,
        "link_geral": f"{base_url}/mesa/cardapio?mesa=1",
        "mesas": lista_mesas_processada
    }

    return templates.TemplateResponse(request, "qr_code.html", {"dados": dados_contexto})

@app.get("/analise", response_class=HTMLResponse)
def rota_analise(request: Request, periodo: str = Query("todos")):
    relatorio = analise.gerar_relatorio_vendas(filtro_periodo=periodo)
    return templates.TemplateResponse(request, "analise.html", {"analise": relatorio, "periodo_atual": periodo})
