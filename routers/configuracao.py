import os
import re
import unicodedata
from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

def gerar_slug(texto: str) -> str:
    nfkd = unicodedata.normalize('NFKD', texto)
    palavra_sem_acento = "".join([c for c in nfkd if not unicodedata.combining(c)])
    slug = re.sub(r'[^a-zA-Z0-9\s]', '', palavra_sem_acento).strip().lower()
    return re.sub(r'\s+', '-', slug)

@router.get("/{slug}/configuracoes", response_class=HTMLResponse)
def config_get(slug: str, request: Request):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM configuracao LIMIT 1")
    config = cursor.fetchone()

    cursor.execute("SELECT * FROM estabelecimentos WHERE slug = %s", (slug,))
    estabelecimento = cursor.fetchone()

    cursor.close()
    db.close()

    return templates.TemplateResponse(request, "configuracao.html", {
        "config": config, 
        "estabelecimento": estabelecimento,
        "slug": slug, 
        "tenant": slug
    })

@router.post("/{slug}/configuracoes")
def config_post(slug: str, nome_restaurante: str = Form(...), quantidade_mesas: int = Form(...)):
    db = get_db()
    cursor = db.cursor()

    # Gera o novo slug com base no novo nome digitado
    novo_slug = gerar_slug(nome_restaurante)

    # Atualiza tanto o nome quanto o slug na tabela estabelecimentos
    cursor.execute(
        "UPDATE estabelecimentos SET nome = %s, slug = %s WHERE slug = %s",
        (nome_restaurante, novo_slug, slug)
    )

    # Atualiza a tabela configuracao
    cursor.execute("DELETE FROM configuracao")
    cursor.execute(
        "INSERT INTO configuracao (nome_restaurante, quantidade_mesas) VALUES (%s, %s)",
        (nome_restaurante, quantidade_mesas)
    )

    db.commit()
    cursor.close()
    db.close()

    # Redireciona automaticamente para a nova URL com o novo slug
    return RedirectResponse(url=f"/admin/{novo_slug}/configuracoes?sucesso=true", status_code=303)
