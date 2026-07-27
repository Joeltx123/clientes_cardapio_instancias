from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database import init_db
from routers import configuracao, cardapio, qr_code, pedidos, cliente, registros, analise, backup

app = FastAPI(title="Cardápio Pro", version="2.0")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
def startup_event():
    init_db()

app.include_router(configuracao.router)
app.include_router(cardapio.router)
app.include_router(qr_code.router)
app.include_router(pedidos.router)
app.include_router(cliente.router)
app.include_router(registros.router)
app.include_router(analise.router)
app.include_router(backup.router)

from fastapi import Request
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(request, "painel.html")
def root():
    return {"message": "API FastAPI do Cardápio Pro rodando com PostgreSQL!"}


templates = Jinja2Templates(directory="templates")

from fastapi import Request
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(request, "painel.html")
def read_root(request: Request):
    return templates.TemplateResponse(request, "painel.html")
