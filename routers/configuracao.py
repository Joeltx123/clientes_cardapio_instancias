import re
import unicodedata
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

class ConfigUpdateModel(BaseModel):
    nome_restaurante: str
    quantidade_mesas: int

def gerar_slug(texto: str) -> str:
    nfkd = unicodedata.normalize('NFKD', texto)
    palavra_sem_acento = "".join([c for c in nfkd if not unicodedata.combining(c)])
    slug = re.sub(r'[^a-zA-Z0-9\s]', '', palavra_sem_acento).strip().lower()
    return re.sub(r'\s+', '-', slug)

@router.get("/{slug}/configuracoes", response_class=HTMLResponse)
def config_get(slug: str, request: Request):
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT * FROM configuracao LIMIT 1")
        config = cursor.fetchone()
        
        cursor.execute("SELECT * FROM estabelecimentos WHERE slug = %s", (slug,))
        estabelecimento = cursor.fetchone()
    except Exception:
        config = None
        estabelecimento = None
    finally:
        cursor.close()
        db.close()

    return templates.TemplateResponse(request, "configuracao.html", {
        "config": config,
        "estabelecimento": estabelecimento,
        "slug": slug,
        "tenant": slug
    })

@router.post("/{slug}/api/configuracoes-salvar")
async def api_config_salvar(slug: str, dados: ConfigUpdateModel):
    db = get_db()
    cursor = db.cursor()
    try:
        novo_slug = gerar_slug(dados.nome_restaurante)

        cursor.execute(
            "UPDATE estabelecimentos SET nome = %s, slug = %s, quantidade_mesas = %s WHERE slug = %s",
            (dados.nome_restaurante, novo_slug, dados.quantidade_mesas, slug)
        )

        cursor.execute("DELETE FROM configuracao")
        cursor.execute(
            "INSERT INTO configuracao (nome_restaurante, quantidade_mesas) VALUES (%s, %s)",
            (dados.nome_restaurante, dados.quantidade_mesas)
        )

        db.commit()
        cursor.close()
        db.close()

        return JSONResponse({
            "status": "sucesso",
            "mensagem": "Configurações atualizadas com sucesso via JSON!",
            "novo_slug": novo_slug
        })
    except Exception as e:
        if db:
            db.rollback()
        return JSONResponse({
            "status": "erro",
            "detalhe": str(e)
        }, status_code=500)
