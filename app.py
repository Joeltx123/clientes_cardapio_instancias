import os
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import banco
import inspetor

app = FastAPI(title="Cardápio Pro API - PostgreSQL")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.middleware("http")
async def middleware_global(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        if 'inspetor' in globals() and hasattr(inspetor, 'capturar_erro'):
            inspetor.capturar_erro(e)
        raise e

# Redireciona a raiz para o caminho completo correto
@app.get("/")
def index():
    return RedirectResponse(url="/admin/joel-burguer/cardapio", status_code=303)

# Registro dos routers
try:
    from routers.configuracao import router as config_bp
    app.include_router(config_bp)
except ImportError:
    pass

try:
    from routers.cardapio import router as cardapio_bp
    app.include_router(cardapio_bp)
except ImportError:
    pass

try:
    from routers.pedidos import router as pedidos_bp
    app.include_router(pedidos_bp)
except ImportError:
    pass

try:
    from routers.analise import router as analise_bp
    app.include_router(analise_bp)
except ImportError:
    pass

try:
    from routers.pagamento import router as pagamento_bp
    app.include_router(pagamento_bp)
except ImportError:
    pass

try:
    from routers.registro import router as registro_bp
    app.include_router(registro_bp)
except ImportError:
    pass

try:
    from routers.backup import router as backup_bp
    app.include_router(backup_bp)
except ImportError:
    pass

try:
    from routers.delivery import router as delivery_bp
    app.include_router(delivery_bp)
except ImportError:
    pass

try:
    from routers.qr_code import router as qr_code_bp
    app.include_router(qr_code_bp)
except ImportError:
    pass

try:
    from routers.cliente import router as cliente_bp
    app.include_router(cliente_bp)
except ImportError:
    pass

if __name__ == '__main__':
    import uvicorn
    porta_dinamica = int(os.environ.get('PORT', 5003))
    uvicorn.run("app:app", host="0.0.0.0", port=porta_dinamica, reload=True)
