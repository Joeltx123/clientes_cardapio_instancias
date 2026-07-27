from fastapi import APIRouter, Request, HTTPException, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import get_db_connection

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return RedirectResponse(url="/configuracoes", status_code=303)

@router.get("/configuracoes", response_class=HTMLResponse)
async def configuracoes(request: Request):
    conn = get_db_connection()
    config = None
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM configuracoes ORDER BY id DESC LIMIT 1")
            config = cursor.fetchone()
        except Exception:
            pass
        finally:
            cursor.close()
            conn.close()
    return templates.TemplateResponse(request, "configuracoes.html", {"config": config})

@router.post("/configuracoes")
async def salvar_configuracoes(request: Request, nome: str = Form(...), mesas: int = Form(10)):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM configuracoes")
            count = cursor.fetchone()[0]
            if count > 0:
                cursor.execute("UPDATE configuracoes SET nome_estabelecimento = %s", (nome,))
            else:
                cursor.execute("INSERT INTO configuracoes (nome_estabelecimento) VALUES (%s)", (nome,))
            
            cursor.execute("DELETE FROM mesas")
            for i in range(1, int(mesas) + 1):
                cursor.execute("INSERT INTO mesas (numero, status) VALUES (%s, 'livre')", (str(i),))

            conn.commit()
        except Exception:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
    return RedirectResponse(url="/pedidos", status_code=303)

@router.get("/admin/cardapio", response_class=HTMLResponse)
async def admin_cardapio(request: Request):
    conn = get_db_connection()
    produtos = []
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM itens ORDER BY categoria, nome")
            produtos = cursor.fetchall()
        except Exception:
            pass
        finally:
            cursor.close()
            conn.close()
    return templates.TemplateResponse(request, "admin_cardapio.html", {"produtos": produtos})

@router.get("/pedidos", response_class=HTMLResponse)
async def pedidos(request: Request):
    conn = get_db_connection()
    mesas = []
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT id, numero, status FROM mesas ORDER BY numero::integer")
            mesas = cursor.fetchall()
        except Exception:
            pass
        finally:
            cursor.close()
            conn.close()
    return templates.TemplateResponse(request, "pedidos.html", {"mesas": mesas})

@router.get("/admin/analise", response_class=HTMLResponse)
async def analise(request: Request):
    conn = get_db_connection()
    faturamento_total = 0
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT SUM(i.preco) FROM pedidos p JOIN itens_pedido ip ON p.id = ip.pedido_id JOIN itens i ON ip.item_id = i.id WHERE p.status IN ('pago', 'finalizado')")
            res = cursor.fetchone()
            if res and res[0]:
                faturamento_total = float(res[0])
        except Exception:
            pass
        finally:
            cursor.close()
            conn.close()

    return templates.TemplateResponse(request, "analise.html", {"faturamento_total": faturamento_total})

@router.get("/registros", response_class=HTMLResponse)
async def registros(request: Request):
    conn = get_db_connection()
    historico = []
    faturamento_total = 0
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT p.mesa, p.forma_pagamento, SUM(i.preco) as total, p.troco, p.data_finalizacao, p.id
                FROM pedidos p
                JOIN itens_pedido ip ON p.id = ip.pedido_id
                JOIN itens i ON ip.item_id = i.id
                WHERE p.status IN ('pago', 'finalizado')
                GROUP BY p.mesa, p.forma_pagamento, p.troco, p.data_finalizacao, p.id
                ORDER BY p.id DESC
            """)
            historico = cursor.fetchall()

            cursor.execute("SELECT SUM(i.preco) FROM pedidos p JOIN itens_pedido ip ON p.id = ip.pedido_id JOIN itens i ON ip.item_id = i.id WHERE p.status IN ('pago', 'finalizado')")
            res = cursor.fetchone()
            if res and res[0]:
                faturamento_total = float(res[0])
        except Exception:
            pass
        finally:
            cursor.close()
            conn.close()

    return templates.TemplateResponse(request, "registros.html", {"historico": historico, "faturamento_total": faturamento_total})

@router.get("/pagamento", response_class=HTMLResponse)
async def pagamento(request: Request):
    conn = get_db_connection()
    mesas_abertas = []
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT p.mesa, SUM(i.preco) as total, p.mesa::integer as num_ordem
                FROM pedidos p
                JOIN itens_pedido ip ON p.id = ip.pedido_id
                JOIN itens i ON ip.item_id = i.id
                WHERE p.status = 'cozinha'
                GROUP BY p.mesa
                ORDER BY num_ordem
            """)
            mesas_abertas = cursor.fetchall()
        except Exception:
            pass
        finally:
            cursor.close()
            conn.close()
    return templates.TemplateResponse(request, "pagamento.html", {"mesas_abertas": mesas_abertas})

@router.get("/api/status-db")
async def status_db():
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Erro de conexão com o PostgreSQL")
    cursor = conn.cursor()
    cursor.execute("SELECT current_database();")
    db_name = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return {"status": "online", "banco_atual": db_name, "framework": "FastAPI Modular"}



