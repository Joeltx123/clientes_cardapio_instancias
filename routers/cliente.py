from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/mesa/{numero_mesa}", response_class=HTMLResponse)
def cardapio_mesa(request: Request, numero_mesa: int):
    db = get_db()
    cursor = db.cursor()
    
    cursor.execute("SELECT nome_restaurante FROM configuracao LIMIT 1")
    config = cursor.fetchone()
    nome_restaurante = config['nome_restaurante'] if config else 'Cardápio Pro'
    
    cursor.execute("SELECT * FROM produtos WHERE arquivado = FALSE ORDER BY categoria, nome")
    produtos = cursor.fetchall()
    
    cursor.close()
    db.close()
    
    return templates.TemplateResponse(
        request,
        "cardapio_cliente.html",
        {
            "mesa": numero_mesa,
            "nome_restaurante": nome_restaurante,
            "produtos": produtos
        }
    )

@router.post("/mesa/{numero_mesa}/pedir")
def fazer_pedido(
    numero_mesa: int,
    itens_pedido: str = Form(...),
    total: float = Form(...),
    forma_pagamento: str = Form(...)
):
    if not itens_pedido or total <= 0:
        return RedirectResponse(url=f"/mesa/{numero_mesa}", status_code=303)
        
    db = get_db()
    cursor = db.cursor()
    
    cursor.execute(
        "INSERT INTO pedidos (mesa, itens, total, forma_pagamento, status) VALUES (%s, %s, %s, %s, 'Pendente')",
        (numero_mesa, itens_pedido, total, forma_pagamento)
    )
    db.commit()
    cursor.close()
    db.close()
    
    return RedirectResponse(url=f"/mesa/{numero_mesa}?sucesso=true", status_code=303)
