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

@app.get("/api/configuracao")
async def api_configuracao_get():
    res = configuracao.processar_requisicao(json.dumps({"acao": "consultar", "dados": {"slug": "estabelecimento"}}))
    return json.loads(res)

@app.post("/api/configuracao")
async def api_configuracao_post(request: Request):
    body = await request.json()
    res = configuracao.processar_requisicao(json.dumps({"acao": "salvar", "dados": body}))
    return json.loads(res)

@app.get("/api/cardapio")
async def api_cardapio():
    res = cardapio.processar_requisicao(json.dumps({"acao": "listar", "dados": {"slug": "estabelecimento"}}))
    return json.loads(res)

@app.get("/api/pedidos")
async def api_pedidos():
    res = pedidos.processar_requisicao(json.dumps({"acao": "listar", "dados": {"slug": "estabelecimento"}}))
    return json.loads(res)

@app.get("/api/delivery")
async def api_delivery():
    res = delivery.processar_requisicao(json.dumps({"acao": "listar", "dados": {"slug": "estabelecimento"}}))
    return json.loads(res)

@app.get("/api/pagamento")
async def api_pagamento():
    res = pagamento.processar_requisicao(json.dumps({"acao": "listar", "dados": {"slug": "estabelecimento"}}))
    return json.loads(res)

@app.get("/api/analise")
async def api_analise():
    res = analise.processar_requisicao(json.dumps({"acao": "gerar_analise", "dados": {"slug": "estabelecimento", "filtro_tipo": "geral"}}))
    return json.loads(res)

@app.get("/api/qrcode")
async def api_qrcode():
    res = qr_code.processar_requisicao(json.dumps({"acao": "gerar", "dados": {"slug": "estabelecimento"}}))
    return json.loads(res)

@app.get("/api/backup")
async def api_backup():
    res = backup.processar_requisicao(json.dumps({"acao": "gerar_backup", "dados": {"slug": "estabelecimento"}}))
    return json.loads(res)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
