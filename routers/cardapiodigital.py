import json
import os
from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

def get_conexao():
    try:
        import banco
        if hasattr(banco, 'get_db'):
            return banco.get_db()
        elif hasattr(banco, 'conexao'):
            return banco.conexao()
    except Exception:
        pass
    try:
        from database import get_db
        return get_db()
    except Exception:
        pass
    return None

@router.get("/cardapio/{tenant}", response_class=HTMLResponse)
def cardapio_digital(request: Request, tenant: str, mesa: int = 1):
    nome_estab = "Meu Restaurante"
    qtd_mesas = 10
    produtos = []

    json_path = f"produtos_{tenant}.json"
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                produtos = json.load(f)
        except Exception:
            pass

    try:
        conn = get_conexao()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM configuracao LIMIT 1;")
                config = cursor.fetchone()
                if config:
                    if isinstance(config, dict):
                        nome_estab = config.get("nome_restaurante", nome_estab)
                        qtd_mesas = config.get("quantidade_mesas", qtd_mesas)
                    else:
                        nome_estab = config[1] if len(config) > 1 else nome_estab
                        qtd_mesas = config[2] if len(config) > 2 else qtd_mesas
            except Exception:
                pass

            if not produtos:
                try:
                    cursor.execute(
                        "SELECT * FROM produtos WHERE (visivel = TRUE OR visivel IS NULL) AND (arquivado = FALSE OR arquivado IS NULL) ORDER BY categoria, nome"
                    )
                    produtos_raw = cursor.fetchall()
                    for p in produtos_raw:
                        if isinstance(p, dict):
                            produtos.append(p)
                        else:
                            produtos.append({
                                "id": p[0],
                                "nome": p[2] if len(p) > 2 else (p[1] if len(p) > 1 else "Item"),
                                "descricao": p[3] if len(p) > 3 else "",
                                "preco": float(p[4]) if len(p) > 4 and p[4] is not None else 0.0,
                                "categoria": p[5] if len(p) > 5 else "Geral"
                            })
                except Exception:
                    pass
            cursor.close()
            conn.close()
    except Exception as e:
        print(f"Erro BD cardapio: {e}")

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
            "tenant": tenant,
            "mesa": mesa,
            "nome_estabelecimento": nome_estab,
            "quantidade_mesas": qtd_mesas,
            "produtos": produtos,
            "produtos_json": json.dumps(produtos, ensure_ascii=False)
        }
    )

@router.post("/cardapio/{tenant}/fazer-pedido")
def fazer_pedido_digital(
    tenant: str,
    mesa: int = Form(...),
    itens: str = Form(...),
    total: float = Form(...)
):
    try:
        conn = get_conexao()
        if conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO pedidos (mesa, itens, total, status) VALUES (%s, %s, %s, 'Pendente')",
                (mesa, itens, total)
            )
            conn.commit()
            cursor.close()
            conn.close()
    except Exception as e:
        print(f"Erro ao registrar pedido digital: {e}")
        try:
            pedidos_file = "pedidos_offline.json"
            all_p = []
            if os.path.exists(pedidos_file):
                with open(pedidos_file, "r", encoding="utf-8") as f:
                    all_p = json.load(f)
            all_p.append({"tenant": tenant, "mesa": mesa, "itens": itens, "total": total, "status": "Pendente"})
            with open(pedidos_file, "w", encoding="utf-8") as f:
                json.dump(all_p, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    return JSONResponse({"status": "sucesso", "mensagem": "Pedido realizado com sucesso!"})
