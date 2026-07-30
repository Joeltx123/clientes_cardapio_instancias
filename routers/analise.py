from fastapi import APIRouter, Request, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from database import get_db
from datetime import datetime, date

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/{slug}/analise", response_class=HTMLResponse)
async def analise_get(request: Request, slug: str):
    config_data = {"nome": "Cardápio Pro"}
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
        print(f"[ERRO SQL CONFIG ANALISE] {str(e)}")

    return templates.TemplateResponse(
        request, 
        "analise.html", 
        {
            "request": request,
            "slug": tenant_ativo,
            "tenant": tenant_ativo,
            "nome_estabelecimento": config_data.get("nome", "Cardápio Pro")
        }
    )

@router.get("/{slug}/api/analise-dados")
async def api_analise_dados(
    slug: str,
    ano: int = Query(None),
    mes: int = Query(None),
    data_inicio: str = Query(None),
    data_fim: str = Query(None)
):
    try:
        db = get_db()
        cursor = db.cursor()

        # Montagem dinâmica de filtros SQL baseados nas escolhas do usuário
        where_clauses = ["(tenant = %s OR tenant IS NOT NULL)"]
        params = [slug]

        if ano:
            where_clauses.append("EXTRACT(YEAR FROM horario) = %s")
            params.append(ano)
        
        if mes:
            where_clauses.append("EXTRACT(MONTH FROM horario) = %s")
            params.append(mes)

        if data_inicio:
            where_clauses.append("horario >= %s")
            params.append(f"{data_inicio} 00:00:00")

        if data_fim:
            where_clauses.append("horario <= %s")
            params.append(f"{data_fim} 23:59:59")

        where_sql = " WHERE " + " AND ".join(where_clauses)

        # 1. Resumo Principal
        query_resumo = f"""
            SELECT 
                COALESCE(SUM(total), 0.0) as faturamento,
                COUNT(*) as total_pedidos,
                COALESCE(AVG(total), 0.0) as ticket_medio,
                COALESCE(SUM(troco), 0.0) as total_troco
            FROM registros_caixa
            {where_sql};
        """
        cursor.execute(query_resumo, tuple(params))
        resumo_db = cursor.fetchone()

        faturamento = float(resumo_db[0] if isinstance(resumo_db, tuple) else resumo_db["faturamento"])
        total_pedidos = int(resumo_db[1] if isinstance(resumo_db, tuple) else resumo_db["total_pedidos"])
        ticket_medio = float(resumo_db[2] if isinstance(resumo_db, tuple) else resumo_db["ticket_medio"])
        total_troco = float(resumo_db[3] if isinstance(resumo_db, tuple) else resumo_db["total_troco"])

        # 2. Ganhos por Forma de Pagamento (Pix, Cartão, Dinheiro, etc.)
        query_pagamentos = f"""
            SELECT 
                LOWER(forma_pagamento) as forma, 
                COUNT(*) as qtd, 
                COALESCE(SUM(total), 0.0) as valor
            FROM registros_caixa
            {where_sql}
            GROUP BY LOWER(forma_pagamento)
            ORDER BY valor DESC;
        """
        cursor.execute(query_pagamentos, tuple(params))
        pagamentos_rows = cursor.fetchall()
        
        pagamentos = []
        pix_total = 0.0
        cartao_total = 0.0
        dinheiro_total = 0.0

        for p in pagamentos_rows:
            forma = p[0] if isinstance(p, tuple) else p["forma"]
            qtd = p[1] if isinstance(p, tuple) else p["qtd"]
            valor = float(p[2] if isinstance(p, tuple) else p["valor"])

            pagamentos.append({"forma": forma, "quantidade": qtd, "valor": valor})

            if "pix" in forma:
                pix_total += valor
            elif "cartao" in forma or "débito" in forma or "crédito" in forma:
                cartao_total += valor
            elif "dinheiro" in forma or "especie" in forma:
                dinheiro_total += valor

        cursor.close()
        db.close()

        return JSONResponse({
            "status": "sucesso",
            "resumo": {
                "faturamento_total": faturamento,
                "total_pedidos": total_pedidos,
                "ticket_medio": ticket_medio,
                "troco_retirado": total_troco,
                "pix": pix_total,
                "cartao": cartao_total,
                "dinheiro": dinheiro_total
            },
            "pagamentos_detalhado": pagamentos
        })
    except Exception as e:
        print(f"[ERRO API ANALISE] {str(e)}")
        return JSONResponse({
            "status": "erro",
            "detalhe": str(e),
            "resumo": {"faturamento_total": 0.0, "total_pedidos": 0, "ticket_medio": 0.0, "troco_retirado": 0.0, "pix": 0.0, "cartao": 0.0, "dinheiro": 0.0},
            "pagamentos_detalhado": []
        })
