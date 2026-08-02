from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

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

@router.get("/{slug}/registros", response_class=HTMLResponse)
def listar_registros(request: Request, slug: str):
    return templates.TemplateResponse(
        request,
        "registros.html",
        {
            "request": request,
            "slug": slug
        }
    )

@router.get("/{slug}/api/registros-caixa")
async def api_registros_caixa(slug: str):
    try:
        db = get_db()
        cursor = db.cursor()

        # Lê diretamente da tabela unificada registros_caixa filtrando pelo tenant ativo
        cursor.execute("""
            SELECT id, mesa, forma_pagamento, total, troco, horario
            FROM registros_caixa
            WHERE tenant = %s
            ORDER BY id DESC;
        """, (slug,))
        rows = cursor.fetchall()
        cursor.close()
        db.close()

        registros = []
        for r in rows:
            if isinstance(r, dict):
                reg_id = r.get("id")
                mesa_num = r.get("mesa")
                fp = r.get("forma_pagamento")
                total = r.get("total", 0.0)
                troco = r.get("troco", 0.0)
                horario = r.get("horario", "")
            else:
                reg_id = r[0] if len(r) > 0 else 0
                mesa_num = r[1] if len(r) > 1 else 1
                fp = r[2] if len(r) > 2 else "Dinheiro"
                total = r[3] if len(r) > 3 else 0.0
                troco = r[4] if len(r) > 4 and r[4] is not None else 0.0
                horario = r[5] if len(r) > 5 else ""

            registros.append({
                "id": reg_id,
                "mesa": str(mesa_num),
                "tipo": "Caixa",
                "forma_pagamento": fp or "Dinheiro",
                "total": float(total) if total else 0.0,
                "troco": float(troco) if troco else 0.0,
                "horario": str(horario) if horario else ""
            })

        return JSONResponse({"status": "sucesso", "registros": registros})
    except Exception as e:
        print(f"[ERRO API REGISTROS CAIXA] {str(e)}")
        return JSONResponse({"status": "erro", "detalhe": str(e), "registros": []}, status_code=400)
