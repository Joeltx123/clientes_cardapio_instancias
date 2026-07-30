import json
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional
from database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")

class PagamentoRequest(BaseModel):
    mesa: int
    total: float
    forma_pagamento: str
    troco: Optional[float] = 0.00

@router.get("/admin/{tenant}/pagamento", response_class=HTMLResponse)
def pagamento_page(request: Request, tenant: str):
    config_data = {"quantidade_mesas": 10, "nome": "Cardápio Pro"}
    tenant_ativo = tenant

    try:
        conn = get_db()
        cursor = conn.cursor()

        # Busca nome e quantidade de mesas direto da tabela configuracao
        cursor.execute("SELECT * FROM configuracao LIMIT 1;")
        res_config = cursor.fetchone()
        if res_config:
            row_dict = dict(res_config) if hasattr(res_config, "keys") else {}
            if "quantidade_mesas" in row_dict and row_dict["quantidade_mesas"] is not None:
                config_data["quantidade_mesas"] = int(row_dict["quantidade_mesas"])
            if "nome" in row_dict and row_dict["nome"]:
                config_data["nome"] = row_dict["nome"]
            if "slug" in row_dict and row_dict["slug"]:
                tenant_ativo = row_dict["slug"]

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"[ERRO SQL CONFIG PAGAMENTO] {str(e)}")

    return templates.TemplateResponse(
        request,
        "pagamento.html",
        {
            "slug": tenant_ativo,
            "tenant": tenant_ativo,
            "config": config_data,
            "nome_estabelecimento": config_data.get("nome", "Cardápio Pro")
        }
    )

@router.get("/admin/{tenant}/api/pagamentos-ativos")
async def pagamentos_ativos(tenant: str):
    try:
        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            """
            SELECT mesa, id, itens, total, status, criado_em
            FROM pedidos
            WHERE LOWER(status) != 'finalizado'
            ORDER BY mesa, id DESC
            """
        )
        linhas = cursor.fetchall()
        cursor.close()
        db.close()

        mesas_dict = {}
        for linha in linhas:
            m = linha["mesa"] if isinstance(linha, dict) else linha[0]
            if m not in mesas_dict:
                mesas_dict[m] = {
                    "mesa": m,
                    "total": 0.0,
                    "itens": []
                }

            val = float(linha["total"] if isinstance(linha, dict) else linha[3])
            mesas_dict[m]["total"] += val

            raw_itens = linha["itens"] if isinstance(linha, dict) else linha[2]
            if raw_itens:
                if isinstance(raw_itens, str):
                    try:
                        raw_itens = json.loads(raw_itens)
                    except Exception:
                        raw_itens = [{"nome": "Item do Pedido", "quantidade": 1}]

                if isinstance(raw_itens, list):
                    mesas_dict[m]["itens"].extend(raw_itens)
                else:
                    mesas_dict[m]["itens"].append(raw_itens)

        resultado = list(mesas_dict.values())
        return JSONResponse({"status": "sucesso", "mesas_ativas": resultado})
    except Exception as e:
        print(f"[ERRO PAGAMENTOS ATIVOS] {str(e)}")
        return JSONResponse({"status": "erro", "detalhe": str(e), "mesas_ativas": []})

@router.post("/admin/{tenant}/api/processar-pagamento")
async def processar_pagamento(tenant: str, dados: PagamentoRequest):
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

        cursor.execute(
            """
            INSERT INTO registros_caixa (tenant, mesa, forma_pagamento, total, troco, horario)
            VALUES (%s, %s, %s, %s, %s, NOW())
            """,
            (tenant, dados.mesa, dados.forma_pagamento, dados.total, dados.troco)
        )

        cursor.execute(
            "UPDATE pedidos SET status = 'Finalizado' WHERE mesa = %s AND LOWER(status) != 'finalizado';",
            (dados.mesa,)
        )

        db.commit()
        cursor.close()
        db.close()

        return JSONResponse({"status": "sucesso", "mensagem": f"Mesa {dados.mesa} paga e liberada com sucesso!"})
    except Exception as e:
        print(f"[ERRO PROCESSAR PAGAMENTO] {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
