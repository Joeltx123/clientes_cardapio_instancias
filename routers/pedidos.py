from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/pedidos", response_class=HTMLResponse)
def listar_pedidos(request: Request):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM pedidos ORDER BY criado_em DESC")
    pedidos = cursor.fetchall()
    cursor.close()
    db.close()
    
    return templates.TemplateResponse(request, "pedidos_admin.html", {"pedidos": pedidos})

@router.post("/pedidos/status/{id}")
def atualizar_status(id: int, status: str = Form(...)):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE pedidos SET status = %s WHERE id = %s", (status, id))
    db.commit()
    cursor.close()
    db.close()
    
    return RedirectResponse(url="/admin/pedidos", status_code=303)
