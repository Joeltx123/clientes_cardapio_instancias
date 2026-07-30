import json
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/delivery")
templates = Jinja2Templates(directory="templates")

def get_conexao():
    try:
        from database import get_db
        return get_db()
    except Exception:
        pass
    return None

def garantir_tabela_delivery():
    try:
        conn = get_conexao()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS pedidos_delivery (
                    id SERIAL PRIMARY KEY,
                    tenant TEXT,
                    cliente_nome TEXT,
                    cliente_telefone TEXT,
                    endereco_entrega TEXT,
                    bairro TEXT,
                    itens TEXT,
                    total NUMERIC(10,2),
                    forma_pagamento TEXT,
                    status TEXT DEFAULT 'Pendente'
                );
            """)
            conn.commit()
            cursor.close()
            conn.close()
    except Exception as e:
        print(f"[ERRO TABELA DELIVERY] {e}")

@router.get("/{tenant}", response_class=HTMLResponse)
def cardapio_digital_delivery_page(request: Request, tenant: str):
    nome_estab = "Cardápio Delivery"
    produtos = []

    try:
        conn = get_conexao()
        if conn:
            cursor = conn.cursor()

            try:
                cursor.execute("SELECT nome_restaurante FROM configuracao LIMIT 1;")
                cfg = cursor.fetchone()
                if cfg:
                    if isinstance(cfg, dict):
                        nome_estab = cfg.get("nome_restaurante", nome_estab)
                    elif len(cfg) > 0 and cfg[0]:
                        nome_estab = cfg[0]
            except Exception:
                pass

            try:
                cursor.execute("SELECT id, nome, descricao, preco, categoria, foto FROM produtos;")
                rows = cursor.fetchall()
                if rows:
                    for p in rows:
                        if isinstance(p, dict):
                            p_id = p.get("id")
                            p_nome = p.get("nome", "Item")
                            p_desc = p.get("descricao", "")
                            p_preco = p.get("preco", 0.0)
                            p_cat = p.get("categoria", "Geral")
                            p_foto = p.get("foto", "")
                        else:
                            p_id = p[0] if len(p) > 0 else 1
                            p_nome = p[1] if len(p) > 1 and p[1] else "Item"
                            p_desc = p[2] if len(p) > 2 and p[2] else ""
                            p_preco = p[3] if len(p) > 3 and p[3] is not None else 0.0
                            p_cat = p.get("categoria", "Geral") if isinstance(p, dict) else (p[4] if len(p) > 4 and p[4] else "Geral")
                            p_foto = p[5] if len(p) > 5 and p[5] else ""

                        produtos.append({
                            "id": p_id,
                            "nome": str(p_nome),
                            "descricao": str(p_desc),
                            "preco": float(p_preco),
                            "categoria": str(p_cat),
                            "foto": str(p_foto)
                        })
            except Exception as e:
                print(f"Erro ao buscar produtos do banco para delivery: {e}")

            cursor.close()
            conn.close()
    except Exception as e:
        print(f"Erro de conexão com o banco no delivery: {e}")

    return templates.TemplateResponse(
        request,
        "cardapio_digital.html",
        {
            "tenant": tenant,
            "mesa": 0,
            "nome_estabelecimento": nome_estab,
            "produtos": produtos,
            "produtos_json": json.dumps(produtos, ensure_ascii=False),
            "modo_delivery": True
        }
    )

@router.post("/{tenant}/fazer-pedido-delivery")
def fazer_pedido_delivery_oficial(
    tenant: str, 
    cliente_nome: str = Form(...), 
    telefone: str = Form(""), 
    endereco: str = Form(""), 
    bairro: str = Form(""), 
    forma_pagamento: str = Form("Dinheiro"), 
    itens: str = Form(...), 
    total: float = Form(...)
):
    garantir_tabela_delivery()
    try:
        conn = get_conexao()
        if conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO pedidos_delivery 
                (tenant, cliente_nome, cliente_telefone, endereco_entrega, bairro, itens, total, forma_pagamento, status) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 'Pendente')
                """,
                (tenant, cliente_nome, telefone, endereco, bairro, itens, total, forma_pagamento)
            )
            conn.commit()
            cursor.close()
            conn.close()
            return JSONResponse({"status": "sucesso", "mensagem": "Pedido de delivery realizado com sucesso!"})
    except Exception as e:
        print(f"Erro pedido delivery: {e}")
        return JSONResponse({"status": "erro", "mensagem": str(e)}, status_code=500)
    
    return JSONResponse({"status": "erro", "mensagem": "Erro de conexão"}, status_code=500)
