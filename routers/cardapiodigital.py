import json
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

def get_conexao():
    try:
        from database import get_db
        return get_db()
    except Exception:
        pass
    return None

@router.get("/cardapio/{tenant}", response_class=HTMLResponse)
def cardapio_digital(request: Request, tenant: str, mesa: int = 1):
    nome_estab = "Cardápio Digital"
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
                            "preco": float(p_preco),  # Converte Decimal para float evitando o erro no JSON
                            "categoria": str(p_cat),
                            "foto": str(p_foto)
                        })
            except Exception as e:
                print(f"Erro ao buscar produtos do banco: {e}")

            cursor.close()
            conn.close()
    except Exception as e:
        print(f"Erro de conexão com o banco: {e}")

    return templates.TemplateResponse(
        request,
        "cardapio_digital.html",
        {
            "tenant": tenant,
            "mesa": mesa,
            "nome_estabelecimento": nome_estab,
            "produtos": produtos,
            "produtos_json": json.dumps(produtos, ensure_ascii=False),
            "modo_delivery": False
        }
    )

@router.post("/cardapio/{tenant}/fazer-pedido")
def fazer_pedido_digital(tenant: str, mesa: int = Form(...), itens: str = Form(...), total: float = Form(...)):
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
        print(f"Erro pedido: {e}")
    return JSONResponse({"status": "sucesso", "mensagem": "Pedido realizado!"})
