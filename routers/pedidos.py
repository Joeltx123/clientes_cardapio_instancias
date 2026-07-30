import json
from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/{tenant}/pedidos", response_class=HTMLResponse)
def listar_pedidos(request: Request, tenant: str):
    pedidos_por_mesa = {}
    config_data = {"quantidade_mesas": 10, "nome": "Cardápio"}
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
        
        # Busca todos os pedidos pendentes
        cursor.execute(
            "SELECT id, mesa, itens, total, forma_pagamento, status, criado_em FROM pedidos WHERE status != 'Finalizado' ORDER BY id DESC;"
        )
        rows = cursor.fetchall()
        
        for r in rows:
            row_dict_p = dict(r) if hasattr(r, "keys") else {
                "id": r[0], "mesa": r[1], "itens": r[2], "total": r[3], 
                "forma_pagamento": r[4], "status": r[5], "criado_em": r[6]
            }
            
            num_mesa = int(row_dict_p["mesa"])
            
            try:
                itens_parsed = json.loads(row_dict_p["itens"])
            except Exception:
                itens_parsed = [{"nome": row_dict_p["itens"], "quantidade": 1, "obs": ""}]

            if num_mesa not in pedidos_por_mesa:
                pedidos_por_mesa[num_mesa] = []

            if isinstance(itens_parsed, list):
                for item in itens_parsed:
                    pedidos_por_mesa[num_mesa].append({
                        "nome": item.get("nome", "Item"),
                        "quantidade": item.get("quantidade", 1),
                        "obs": item.get("obs", "")
                    })
            else:
                pedidos_por_mesa[num_mesa].append({
                    "nome": str(itens_parsed),
                    "quantidade": 1,
                    "obs": ""
                })
            
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"[ERRO SQL LISTAR PEDIDOS] {str(e)}")

    return templates.TemplateResponse(
        request,
        "pedidos.html",
        {
            "slug": tenant_ativo,
            "tenant": tenant_ativo,
            "config": config_data,
            "pedidos_por_mesa": pedidos_por_mesa
        }
    )

@router.post("/admin/{tenant}/pedidos/liberar/{mesa}")
async def liberar_mesa(tenant: str, mesa: int):
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE pedidos SET status = 'Finalizado' WHERE mesa = %s AND status != 'Finalizado';",
            (mesa,)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return JSONResponse({"status": "sucesso"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
