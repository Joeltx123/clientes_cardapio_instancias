import os
import shutil
from fastapi import APIRouter, Request, Form, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def obter_estabelecimento_por_slug(cursor, slug: str):
    cursor.execute("SELECT id FROM estabelecimentos WHERE slug = %s", (slug,))
    est = cursor.fetchone()
    if not est:
        raise HTTPException(status_code=404, detail="Estabelecimento não encontrado")
    return est['id']

@router.get("/{slug}/cardapio", response_class=HTMLResponse)
def listar_cardapio(slug: str, request: Request, tab: str = "ativos"):
    db = get_db()
    cursor = db.cursor()
    
    est_id = obter_estabelecimento_por_slug(cursor, slug)
    
    if tab == "arquivados":
        cursor.execute("SELECT * FROM produtos WHERE estabelecimento_id = %s AND arquivado = TRUE ORDER BY categoria, nome", (est_id,))
    else:
        cursor.execute("SELECT * FROM produtos WHERE estabelecimento_id = %s AND (arquivado = FALSE OR arquivado IS NULL) ORDER BY categoria, nome", (est_id,))

    produtos = cursor.fetchall()
    cursor.close()
    db.close()
    
    return templates.TemplateResponse(request, "cardapio_admin.html", {"produtos": produtos, "tab": tab, "slug": slug})

@router.post("/{slug}/cardapio/adicionar")
async def adicionar_produto(
    slug: str,
    nome: str = Form(...),
    descricao: str = Form(""),
    preco: float = Form(...),
    categoria: str = Form(...),
    foto_url: str = Form(""),
    foto_arquivo: UploadFile = File(None)
):
    foto_final = foto_url.strip()
    if foto_arquivo and foto_arquivo.filename:
        file_path = os.path.join(UPLOAD_DIR, foto_arquivo.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(foto_arquivo.file, buffer)
        foto_final = f"/{file_path}"
        
    db = get_db()
    cursor = db.cursor()
    est_id = obter_estabelecimento_por_slug(cursor, slug)
    
    cursor.execute(
        "INSERT INTO produtos (estabelecimento_id, nome, descricao, preco, categoria, foto, arquivado, visivel) VALUES (%s, %s, %s, %s, %s, %s, FALSE, TRUE)",
        (est_id, nome, descricao, preco, categoria, foto_final)
    )
    db.commit()
    cursor.close()
    db.close()

    return RedirectResponse(url=f"/admin/{slug}/cardapio?tab=ativos", status_code=303)

@router.post("/{slug}/cardapio/arquivar/{id}")
def arquivar_produto(slug: str, id: int):
    db = get_db()
    cursor = db.cursor()
    est_id = obter_estabelecimento_por_slug(cursor, slug)
    cursor.execute("UPDATE produtos SET arquivado = TRUE WHERE id = %s AND estabelecimento_id = %s", (id, est_id))
    db.commit()
    cursor.close()
    db.close()

    return RedirectResponse(url=f"/admin/{slug}/cardapio?tab=ativos", status_code=303)

@router.post("/{slug}/cardapio/desarquivar/{id}")
def desarquivar_produto(slug: str, id: int):
    db = get_db()
    cursor = db.cursor()
    est_id = obter_estabelecimento_por_slug(cursor, slug)
    cursor.execute("UPDATE produtos SET arquivado = FALSE WHERE id = %s AND estabelecimento_id = %s", (id, est_id))
    db.commit()
    cursor.close()
    db.close()

    return RedirectResponse(url=f"/admin/{slug}/cardapio?tab=arquivados", status_code=303)

@router.post("/{slug}/cardapio/toggle_visibilidade/{id}")
def toggle_visibilidade(slug: str, id: int):
    db = get_db()
    cursor = db.cursor()
    est_id = obter_estabelecimento_por_slug(cursor, slug)
    cursor.execute("UPDATE produtos SET visivel = NOT visivel WHERE id = %s AND estabelecimento_id = %s", (id, est_id))
    db.commit()
    cursor.close()
    db.close()

    return RedirectResponse(url=f"/admin/{slug}/cardapio?tab=ativos", status_code=303)

@router.post("/{slug}/cardapio/excluir/{id}")
def excluir_produto(slug: str, id: int):
    db = get_db()
    cursor = db.cursor()
    est_id = obter_estabelecimento_por_slug(cursor, slug)
    cursor.execute("DELETE FROM produtos WHERE id = %s AND estabelecimento_id = %s", (id, est_id))
    db.commit()
    cursor.close()
    db.close()

    return RedirectResponse(url=f"/admin/{slug}/cardapio?tab=arquivados", status_code=303)
