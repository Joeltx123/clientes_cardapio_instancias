import os
from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

def obter_estabelecimento_por_slug(cursor, slug: str):
    cursor.execute("SELECT id FROM estabelecimentos WHERE slug = %s", (slug,))
    est = cursor.fetchone()
    if not est:
        raise HTTPException(status_code=404, detail="Estabelecimento não encontrado")
    return est['id']

@router.get("/{slug}/configuracoes", response_class=HTMLResponse)
def config_get(slug: str, request: Request):
    db = get_db()
    cursor = db.cursor()
    est_id = obter_estabelecimento_por_slug(cursor, slug)
    
    cursor.execute("SELECT * FROM configuracao WHERE estabelecimento_id = %s LIMIT 1", (est_id,))
    config = cursor.fetchone()
    cursor.close()
    db.close()

    return templates.TemplateResponse(request, "configuracao.html", {"config": config, "slug": slug})

@router.post("/{slug}/configuracoes")
def config_post(slug: str, nome_restaurante: str = Form(...), quantidade_mesas: int = Form(...)):
    db = get_db()
    cursor = db.cursor()
    est_id = obter_estabelecimento_por_slug(cursor, slug)

    cursor.execute("DELETE FROM configuracao WHERE estabelecimento_id = %s", (est_id,))
    cursor.execute(
        "INSERT INTO configuracao (estabelecimento_id, nome_restaurante, quantidade_mesas) VALUES (%s, %s, %s)",
        (est_id, nome_restaurante, quantidade_mesas)
    )
    db.commit()
    cursor.close()
    db.close()

    return RedirectResponse(url=f"/admin/{slug}/configuracoes?sucesso=true", status_code=303)
