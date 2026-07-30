import json
from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Rota chamada pelo cardápio para registrar o pedido no PostgreSQL
@router.post("/cardapio/{tenant}/fazer-pedido")
async def fazer_pedido(tenant: str, mesa: int = Form(...), itens: str = Form(...), total: float = Form(...), forma_pagamento: str = Form("Não informada")):
    try:
        conn = get_db()
        cursor = conn.cursor()
        
        cursor.execute(
            """
            INSERT INTO pedidos (tenant, mesa, itens, total, forma_pagamento, status) 
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (tenant, mesa, itens, total, forma_pagamento, 'Pendente')
        )
        conn.commit()
        cursor.close()
        conn.close()
        
        return JSONResponse({"status": "sucesso", "mensagem": "Pedido enviado para a cozinha com sucesso!"})
    except Exception as e:
        print(f"[ERRO SQL PEDIDO] {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Rota do Painel Admin para listar e agrupar os pedidos por mesa
@router.get("/admin/{tenant}/pedidos", response_class=HTMLResponse)
def listar_pedidos(request: Request, tenant: str):
    pedidos_por_mesa = {}
    config_data = {"quantidade_mesas": 10}
    
    try:
        conn = get_db()
        cursor = conn.cursor()
        
        # Busca a configuração de quantidade de mesas do estabelecimento ou padrão
        cursor.execute("SELECT quantidade_mesas FROM estabelecimentos WHERE slug = %s;", (tenant,))
        res_config = cursor.fetchone()
        if res_config:
            if isinstance(res_config, dict):
                config_data["quantidade_mesas"] = res_config.get("quantidade_mesas", 10)
            else:
                config_data["quantidade_mesas"] = res_config[0]
        
        # Busca apenas pedidos pendentes ou ativos do tenant
        cursor.execute(
            "SELECT id, mesa, itens, total, forma_pagamento, status, criado_em FROM pedidos WHERE tenant = %s AND status != 'Finalizado' ORDER BY id DESC;",
            (tenant,)
        )
        rows = cursor.fetchall()
        
        for r in rows:
            row_dict = dict(r) if hasattr(r, "keys") else {
                "id": r[0], "mesa": r[1], "itens": r[2], "total": r[3], 
                "forma_pagamento": r[4], "status": r[5], "criado_em": r[6]
            }
            
            num_mesa = int(row_dict["mesa"])
            
            try:
                itens_parsed = json.loads(row_dict["itens"])
            except Exception:
                itens_parsed = [{"nome": row_dict["itens"], "quantidade": 1, "obs": ""}]

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
            "slug": tenant,
            "tenant": tenant,
            "config": config_data,
            "pedidos_por_mesa": pedidos_por_mesa
        }
    )

# Rota para liberar a mesa (marcar pedidos como finalizados)
@router.post("/admin/{tenant}/pedidos/liberar/{mesa}")
async def liberar_mesa(tenant: str, mesa: int):
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE pedidos SET status = 'Finalizado' WHERE tenant = %s AND mesa = %s AND status != 'Finalizado';",
            (tenant, mesa)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return JSONResponse({"status": "sucesso"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
