import os
import json
from fastapi import FastAPI, Request, Query, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sisyten import pedidos, cardapio, analise, backup, json_core

app = FastAPI(title="Sistema Cardápio Instâncias")
templates = Jinja2Templates(directory="templates")

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

@app.get("/cardapio", response_class=HTMLResponse)
def rota_cardapio(request: Request):
    try:
        itens = cardapio.listar_cardapio()
        return templates.TemplateResponse(request, "cardapio.html", {"cardapio": itens})
    except Exception as e:
        return templates.TemplateResponse(request, "cardapio.html", {"cardapio": []})

@app.get("/delivery", response_class=HTMLResponse)
def rota_delivery(request: Request):
    return templates.TemplateResponse(request, "delivery.html", {})

@app.get("/configuracao", response_class=HTMLResponse)
def rota_configuracao(request: Request):
    return templates.TemplateResponse(request, "configuracao.html", {})

@app.get("/pagamento", response_class=HTMLResponse)
def rota_pagamento(request: Request):
    return templates.TemplateResponse(request, "pagamento.html", {})

@app.get("/backup", response_class=HTMLResponse)
def rota_backup(request: Request):
    return templates.TemplateResponse(request, "backup.html", {})

@app.get("/qrcode", response_class=HTMLResponse)
def rota_qrcode(request: Request):
    base_url = str(request.base_url).rstrip("/")
    config = json_core.ler_json_seguro("dados/configuracao.json", {
        "nome_estabelecimento": "Meu Estabelecimento",
        "mesas": 5
    })
    
    nome_est = config.get("nome_estabelecimento", "Meu Estabelecimento")
    
    # Processa as mesas independentemente de virem como número, lista de inteiros ou lista de dicionários
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
        link_mesa = f"{base_url}/cardapio?mesa={num_mesa}"
        lista_mesas_processada.append({
            "mesa": num_mesa,
            "link_acesso": link_mesa
        })

    dados_contexto = {
        "status": "sucesso",
        "nome_estabelecimento": nome_est,
        "link_geral": f"{base_url}/cardapio",
        "mesas": lista_mesas_processada
    }

    return templates.TemplateResponse(request, "qr_code.html", {"dados": dados_contexto})

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

@app.get("/analise", response_class=HTMLResponse)
def rota_analise(request: Request, periodo: str = Query("todos")):
    relatorio = analise.gerar_relatorio_vendas(filtro_periodo=periodo)
    return templates.TemplateResponse(request, "analise.html", {"analise": relatorio, "periodo_atual": periodo})
