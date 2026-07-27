from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/backup", response_class=HTMLResponse)
def painel_backup(request: Request):
    return templates.TemplateResponse(request, "backup.html", {})

@router.get("/backup/exportar")
def exportar_dados():
    db = get_db()
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM configuracao")
    config = cursor.fetchall()
    
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    
    cursor.execute("SELECT * FROM pedidos")
    pedidos = cursor.fetchall()
    
    cursor.close()
    db.close()
    
    dados_backup = {
        "configuracao": config,
        "produtos": produtos,
        "pedidos": pedidos
    }
    
    return JSONResponse(content=dados_backup, headers={"Content-Disposition": "attachment; filename=backup_cardapio_pro.json"})
