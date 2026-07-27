from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/cardapio", response_class=HTMLResponse)
def listar_cardapio(request: Request):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produtos ORDER BY categoria, nome")
    produtos = cursor.fetchall()
    cursor.close()
    db.close()
    
    return templates.TemplateResponse(request, "cardapio_admin.html", {"produtos": produtos})

@router.post("/cardapio/adicionar")
def adicionar_produto(
    nome: str = Form(...),
    descricao: str = Form(""),
    preco: float = Form(...),
    categoria: str = Form(...)
):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, descricao, preco, categoria, arquivado) VALUES (%s, %s, %s, %s, FALSE)",
        (nome, descricao, preco, categoria)
    )
    db.commit()
    cursor.close()
    db.close()
    
    return RedirectResponse(url="/admin/cardapio", status_code=303)

@router.post("/cardapio/arquivar/{id}")
def arquivar_produto(id: int):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE produtos SET arquivado = NOT arquivado WHERE id = %s", (id,))
    db.commit()
    cursor.close()
    db.close()
    
    return RedirectResponse(url="/admin/cardapio", status_code=303)
