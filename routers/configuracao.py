from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/configuracoes", response_class=HTMLResponse)
def config_get(request: Request):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM configuracao LIMIT 1")
    config = cursor.fetchone()
    cursor.close()
    db.close()
    
    return templates.TemplateResponse(request, "configuracao.html", {"config": config})

@router.post("/configuracoes")
def config_post(nome_restaurante: str = Form(...), quantidade_mesas: int = Form(...)):
    db = get_db()
    cursor = db.cursor()
    
    cursor.execute("DELETE FROM configuracao")
    cursor.execute(
        "INSERT INTO configuracao (nome_restaurante, quantidade_mesas) VALUES (%s, %s)",
        (nome_restaurante, quantidade_mesas)
    )
    db.commit()
    cursor.close()
    db.close()
    
    return RedirectResponse(url="/admin/configuracoes?sucesso=true", status_code=303)
