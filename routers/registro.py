from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

# Rota principal do painel de registro de caixa
@router.get("/{slug}/registro", response_class=HTMLResponse)
def registro_page(request: Request, slug: str):
    config_data = {"quantidade_mesas": 10, "nome": "Cardápio Pro"}
    tenant_ativo = slug

    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM configuracao LIMIT 1;")
        res_config = cursor.fetchone()
        if res_config:
            row_dict = dict(res_config) if hasattr(res_config, "keys") else {}
            if "nome" in row_dict and row_dict["nome"]:
                config_data["nome"] = row_dict["nome"]
            if "slug" in row_dict and row_dict["slug"]:
                tenant_ativo = row_dict["slug"]
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"[ERRO SQL CONFIG REGISTRO] {str(e)}")

    return templates.TemplateResponse(
        request,
        "registro.html",
        {
            "slug": tenant_ativo,
            "tenant": tenant_ativo,
            "config": config_data,
            "nome_estabelecimento": config_data.get("nome", "Cardápio Pro")
        }
    )

# Rota legída/alternativa que lista os pedidos (do antigo registros.py)
@router.get("/{slug}/registros", response_class=HTMLResponse)
def listar_registros(request: Request, slug: str):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM pedidos ORDER BY criado_em DESC LIMIT 100")
        transacoes = cursor.fetchall()
        cursor.close()
        db.close()
    except Exception as e:
        print(f"[ERRO SQL REGISTROS LEGACY] {str(e)}")
        transacoes = []

    return templates.TemplateResponse(
        request, 
        "registros.html", 
        {
            "request": request,
            "slug": slug,
            "transacoes": transacoes
        }
    )

# API de registros de caixa consolidados
@router.get("/{slug}/api/registros-caixa")
async def api_registros_caixa(slug: str):
    try:
        db = get_db()
        cursor = db.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS registros_caixa (
                id SERIAL PRIMARY KEY,
                tenant VARCHAR(100),
                mesa INT,
                forma_pagamento VARCHAR(150),
                total NUMERIC(10, 2),
                troco NUMERIC(10, 2) DEFAULT 0.00,
                horario TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        db.commit()

        cursor.execute(
            """
            SELECT id, mesa, forma_pagamento, total, troco, horario
            FROM registros_caixa
            WHERE tenant = %s OR tenant IS NOT NULL
            ORDER BY id DESC
            LIMIT 50
            """,
            (slug,)
        )
        linhas = cursor.fetchall()
        cursor.close()
        db.close()

        registros = []
        for l in linhas:
            registros.append({
                "id": l["id"] if isinstance(l, dict) else l[0],
                "mesa": l["mesa"] if isinstance(l, dict) else l[1],
                "forma_pagamento": l["forma_pagamento"] if isinstance(l, dict) else l[2],
                "total": float(l["total"] if isinstance(l, dict) else l[3]),
                "troco": float(l["troco"] if isinstance(l, dict) else l[4] or 0.0),
                "horario": str(l["horario"] if isinstance(l, dict) else l[5])
            })

        return JSONResponse({"status": "sucesso", "registros": registros})
    except Exception as e:
        print(f"[ERRO API REGISTROS] {str(e)}")
        return JSONResponse({"status": "erro", "detalhe": str(e), "registros": []})
