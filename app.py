from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Cardápio Pro - JSON Centralizado")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def raiz(request: Request):
    # Assinatura corrigida para as versões recentes do Starlette/FastAPI
    return templates.TemplateResponse(request, "base.html", {})

@app.get("/api/configuracao")
def api_configuracao():
    return {"status": "sucesso", "modulo": "configuracao", "dados": {"empresa": "Cardápio Pro", "taxa_padrao": 5.00}}

@app.get("/api/cardapio")
def api_cardapio():
    return {"status": "sucesso", "modulo": "cardapio", "itens": [{"id": 1, "nome": "Pizza Margherita", "preco": 45.00}]}

@app.get("/api/pedidos")
def api_pedidos():
    return {"status": "sucesso", "modulo": "pedidos", "pedidos_ativos": []}

@app.get("/api/delivery")
def api_delivery():
    return {"status": "sucesso", "modulo": "delivery", "entregadores_disponiveis": 3}

@app.get("/api/pagamento")
def api_pagamento():
    return {"status": "sucesso", "modulo": "pagamento", "metodos": ["Pix", "Cartão", "Dinheiro"]}

@app.get("/api/analise")
def api_analise():
    return {"status": "sucesso", "modulo": "analise", "faturamento_dia": 1250.00}

@app.get("/api/qrcode")
def api_qrcode():
    return {"status": "sucesso", "modulo": "qrcode", "mesas_geradas": 15}

@app.get("/api/backup")
def api_backup():
    return {"status": "sucesso", "modulo": "backup", "ultimo_backup": "2026-06-06 12:00"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=5003, reload=True)
