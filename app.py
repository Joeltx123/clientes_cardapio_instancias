import os
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import banco
import inspetor
from atualizar_ip import salvar_ip_json

# Atualiza o IP real assim que o servidor inicia
salvar_ip_json()

app = FastAPI(title="Cardápio Pro API - PostgreSQL")

# Importa e registra todos os roteadores modulares do sistema
from routers import (
    analise, backup, cardapio, cardapiodigital, 
    cliente, configuracao, delivery, pagamento, 
    pedidos, qr_code, registro
)

app.include_router(analise.router)
app.include_router(backup.router)
app.include_router(cardapio.router)
app.include_router(cardapiodigital.router)
app.include_router(cliente.router)
app.include_router(configuracao.router)
app.include_router(delivery.router)
app.include_router(pagamento.router)
app.include_router(pedidos.router)
app.include_router(qr_code.router)
app.include_router(registro.router)


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Alterado para cair direto na página de Configurações
@app.get("/")
def raiz():
    return RedirectResponse(url="/admin/teste/configuracoes")

@app.middleware("http")
async def middleware_global(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        if 'inspetor' in globals() and hasattr(inspetor, 'capturar_erro'):
            inspetor.capturar_erro(e)
        raise e

from routers import cardapio_digital_delivery
app.include_router(cardapio_digital_delivery.router)
