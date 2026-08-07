from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sisyten.configuracao import rota_configuracao
from sisyten.cardapio import rota_cardapio
from sisyten.pedido import rota_pedido
from sisyten.delivery import rota_delivery
from sisyten.pagamento import rota_pagamento
from sisyten.analise import rota_analise
from sisyten.qr_code import rota_qr_code
from sisyten.backup import rota_backup
from sisyten.digital import rota_digital

app = FastAPI(title="Sistema Cardápio Instâncias")

# Configuração do Jinja2 para abranger a raiz e todos os diretórios dos módulos
templates = Jinja2Templates(directory=[
    "templates", 
    "sisyten/configuracao", 
    "sisyten/cardapio", 
    "sisyten/pedido", 
    "sisyten/delivery",
    "sisyten/pagamento",
    "sisyten/analise",
    "sisyten/qr_code",
    "sisyten/backup",
    "sisyten/digital"
])
app.state.templates = templates

# Registro de todas as rotas dos módulos
app.include_router(rota_configuracao.router)
app.include_router(rota_cardapio.router)
app.include_router(rota_pedido.router)
app.include_router(rota_delivery.router)
app.include_router(rota_pagamento.router)
app.include_router(rota_analise.router)
app.include_router(rota_qr_code.router)
app.include_router(rota_backup.router)
app.include_router(rota_digital.router)

@app.get("/", response_class=HTMLResponse)
def raiz(request: Request):
    return templates.TemplateResponse(request, "index.html", {"request": request})
