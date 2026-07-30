import json
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

def garantir_tabela_delivery():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pedidos_delivery (
                id SERIAL PRIMARY KEY,
                tenant VARCHAR(100),
                cliente_nome VARCHAR(150),
                cliente_telefone VARCHAR(50),
                endereco_entrega TEXT,
                bairro VARCHAR(100),
                itens JSONB,
                total NUMERIC(10, 2),
                forma_pagamento VARCHAR(100),
                status VARCHAR(50) DEFAULT 'pendente_pagamento',
                horario TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        db.commit()
        cursor.close()
        db.close()
    except Exception as e:
        print(f"[ERRO TABELA DELIVERY] {str(e)}")

@router.get("/{slug}/delivery", response_class=HTMLResponse)
def delivery_admin_page(request: Request, slug: str):
    garantir_tabela_delivery()
    config_data = {"nome": "Cardápio Pro"}
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT nome_restaurante FROM configuracao LIMIT 1;")
        res = cursor.fetchone()
        if res:
            config_data["nome"] = res[0] if isinstance(res, tuple) else res["nome_restaurante"]
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"[ERRO NOME CONFIG DELIVERY] {str(e)}")

    return templates.TemplateResponse(
        request,
        "delivery_admin.html",
        {
            "request": request,
            "slug": slug,
            "tenant": slug,
            "nome_estabelecimento": config_data["nome"]
        }
    )

@router.get("/{slug}/delivery-pedido", response_class=HTMLResponse)
def delivery_cliente_page(request: Request, slug: str):
    garantir_tabela_delivery()
    
    nome_estab = "Delivery"
    produtos = []

    try:
        conn = get_db()
        cursor = conn.cursor()
        
        # Busca o nome do estabelecimento
        try:
            cursor.execute("SELECT nome_restaurante FROM configuracao LIMIT 1;")
            config = cursor.fetchone()
            if config:
                nome_estab = config[0] if isinstance(config, (list, tuple)) else config.get("nome_restaurante", "Delivery")
        except Exception:
            pass

        # Busca os produtos da tabela produtos
        try:
            cursor.execute("SELECT id, nome, descricao, preco, categoria FROM produtos WHERE (arquivado = FALSE OR arquivado IS NULL) ORDER BY categoria, nome;")
            produtos_raw = cursor.fetchall()
            for p in produtos_raw:
                if isinstance(p, dict):
                    produtos.append(p)
                else:
                    produtos.append({
                        "id": p[0],
                        "nome": p[1] if len(p) > 1 else "Item",
                        "descricao": p[2] if len(p) > 2 else "",
                        "preco": float(p[3]) if len(p) > 3 and p[3] is not None else 0.0,
                        "categoria": p[4] if len(p) > 4 and p[4] is not None else "Geral"
                    })
        except Exception as e:
            print(f"Erro ao buscar produtos para o delivery: {e}")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Erro BD delivery cliente: {e}")

    if not produtos:
        produtos = [
            {"id": 1, "nome": "Hambúrguer Artesanal", "descricao": "Pão, carne 160g, queijo cheddar e bacon.", "preco": 32.90, "categoria": "Lanches"},
            {"id": 2, "nome": "Batata Frita Crocante", "descricao": "Porção generosa com molho especial da casa.", "preco": 18.00, "categoria": "Porções"},
            {"id": 3, "nome": "Refrigerante Lata 350ml", "descricao": "Coca-Cola, Guaraná ou Sprite.", "preco": 6.50, "categoria": "Bebidas"}
        ]

    return templates.TemplateResponse(
        request,
        "cardapio_digital.html",
        {
            "request": request,
            "slug": slug,
            "tenant": slug,
            "mesa": 0,
            "nome_estabelecimento": nome_estab,
            "produtos": produtos,
            "produtos_json": json.dumps(produtos, ensure_ascii=False),
            "modo_delivery": True
        }
    )

@router.get("/{slug}/api/delivery-listar")
async def api_delivery_listar(slug: str):
    garantir_tabela_delivery()
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            SELECT id, cliente_nome, cliente_telefone, endereco_entrega, bairro, total, forma_pagamento, status, horario
            FROM pedidos_delivery
            WHERE tenant = %s
            ORDER BY id DESC;
        """, (slug,))
        rows = cursor.fetchall()
        cursor.close()
        db.close()

        pedidos = []
        for r in rows:
            pedidos.append({
                "id": r[0],
                "cliente_nome": r[1],
                "telefone": r[2],
                "endereco": r[3],
                "bairro": r[4],
                "total": float(r[5]),
                "forma_pagamento": r[6],
                "status": r[7],
                "horario": str(r[8])
            })
        return JSONResponse({"status": "sucesso", "pedidos": pedidos})
    except Exception as e:
        return JSONResponse({"status": "erro", "detalhe": str(e), "pedidos": []})

@router.post("/{slug}/api/cardapio-delivery-enviar")
async def api_cardapio_delivery_enviar(slug: str, data: dict):
    garantir_tabela_delivery()
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO pedidos_delivery (tenant, cliente_nome, cliente_telefone, endereco_entrega, bairro, itens, total, forma_pagamento, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 'pendente_pagamento')
            RETURNING id;
        """, (
            slug,
            data.get("cliente_nome", "Cliente Delivery"),
            data.get("telefone", ""),
            data.get("endereco", ""),
            data.get("bairro", ""),
            json.dumps(data.get("itens", [])),
            data.get("total", 0.0),
            data.get("forma_pagamento", "Pix")
        ))
        pedido_id = cursor.fetchone()[0]
        db.commit()
        cursor.close()
        db.close()
        return JSONResponse({"status": "sucesso", "pedido_id": pedido_id})
    except Exception as e:
        print(f"[ERRO CARDAPIO DELIVERY] {str(e)}")
        return JSONResponse({"status": "erro", "detalhe": str(e)})
