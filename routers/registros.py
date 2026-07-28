from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/{slug}/registros", response_class=HTMLResponse)
def listar_registros(request: Request):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM pedidos ORDER BY criado_em DESC")
    transacoes = cursor.fetchall()
    cursor.close()
    db.close()
    
    return templates.TemplateResponse(request, "registros.html", {"transacoes": transacoes})
