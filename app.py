import psycopg2
import psycopg2.extras
import os
import json
from fastapi import FastAPI, Request, Query, Form
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sisyten import pedidos, cardapio, analise, backup, json_core, configuracao, delivery, pagamento
import digital

app = FastAPI(title="Sistema Cardápio Instâncias")
templates = Jinja2Templates(directory="templates")

app.include_router(digital.router)

@app.get("/", response_class=HTMLResponse)
def raiz(request: Request):
    return templates.TemplateResponse(request, "index.html", {})

@app.get("/pedidos", response_class=HTMLResponse)
def rota_pedidos(request: Request):
    try:
        dados = pedidos.obter_dados()
        return templates.TemplateResponse(request, "pedidos.html", {"dados": dados})
    except Exception as e:
        return templates.TemplateResponse(request, "pedidos.html", {"dados": {"mesas": []}})

@app.post("/liberar-mesa")
def liberar_mesa(mesa: int = Form(...)):
    try:
        payload = {"acao": "liberar_mesa", "mesa": mesa}
        pedidos.processar_requisicao(json.dumps(payload))
    except Exception as e:
        print(f"Erro ao liberar mesa: {e}")
    return RedirectResponse(url="/pedidos", status_code=303)

@app.get("/cardapio", response_class=HTMLResponse)
def rota_cardapio(request: Request):
    try:
        itens = cardapio.listar_cardapio()
        return templates.TemplateResponse(request, "cardapio.html", {"produtos": itens})
    except Exception as e:
        print(f"Erro: {e}")
        return templates.TemplateResponse(request, "cardapio.html", {"produtos": []})

@app.get("/delivery", response_class=HTMLResponse)
def rota_delivery(request: Request):
    return templates.TemplateResponse(request, "delivery.html", {})


def rota_configuracao_get(request: Request):
    return templates.TemplateResponse(request, "configuracao.html", {"mensagem": None})

async def rota_configuracao_post(request: Request):
    form = await request.form()
    # Aqui você pode processar os dados salvos se necessário
    return templates.TemplateResponse(request, "configuracao.html", {"mensagem": "Configurações salvas com sucesso!"})


def rota_configuracao_get(request: Request):
    conn = psycopg2.connect(dbname="cardapio_pro", user="postgres")
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT * FROM administracao LIMIT 1;")
    config = cur.fetchone()
    cur.close()
    conn.close()
    return templates.TemplateResponse(request, "configuracao.html", {"config": config, "mensagem": None})

async def rota_configuracao_post(request: Request):
    form = await request.form()
    nome = form.get("nome") or form.get("nome_estabelecimento")
    mesas = form.get("mesas") or form.get("quantidade_mesas")
    
    conn = psycopg2.connect(dbname="cardapio_pro", user="postgres")
    cur = conn.cursor()
    try:
        # Atualiza ou insere na tabela administracao
        cur.execute("UPDATE administracao SET nome = %s, mesas = %s WHERE id = 1;", (nome, int(mesas) if mesas else 0))
        if cur.rowcount == 0:
            cur.execute("INSERT INTO administracao (id, nome, mesas) VALUES (1, %s, %s);", (nome, int(mesas) if mesas else 0))
        conn.commit()
        mensagem = "Configurações salvas no banco com sucesso!"
    except Exception as e:
        conn.rollback()
        mensagem = f"Erro ao salvar: {e}"
    finally:
        cur.close()
        conn.close()

    conn = psycopg2.connect(dbname="cardapio_pro", user="postgres")
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT * FROM administracao LIMIT 1;")
    config = cur.fetchone()
    cur.close()
    conn.close()

    return templates.TemplateResponse(request, "configuracao.html", {"config": config, "mensagem": mensagem})


@app.get("/configuracao", response_class=HTMLResponse)
def rota_configuracao_get(request: Request):
    conn = psycopg2.connect(dbname="cardapio_pro", user="postgres")
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT * FROM administracao LIMIT 1;")
    row = cur.fetchone()
    cur.close()
    conn.close()
    
    # Adapta para o formato que o template espera (dados.nome e dados.quantidade_mesas)
    dados = {
        "nome": row["nome"] if row else "",
        "quantidade_mesas": row["mesas"] if row else 5,
        "slug": "estabelecimento"
    }
    return templates.TemplateResponse(request, "configuracao.html", {"dados": dados, "mensagem": None})

@app.post("/configuracao", response_class=HTMLResponse)
async def rota_configuracao_post(request: Request):
    form = await request.form()
    nome = form.get("nome_estabelecimento")
    mesas = form.get("quantidade_mesas")
    
    conn = psycopg2.connect(dbname="cardapio_pro", user="postgres")
    cur = conn.cursor()
    try:
        cur.execute("UPDATE administracao SET nome = %s, mesas = %s WHERE id = 1;", (nome, int(mesas) if mesas else 5))
        if cur.rowcount == 0:
            cur.execute("INSERT INTO administracao (id, nome, mesas) VALUES (1, %s, %s);", (nome, int(mesas) if mesas else 5))
        conn.commit()
        mensagem = "Configurações salvas com sucesso!"
    except Exception as e:
        conn.rollback()
        mensagem = f"Erro ao salvar: {e}"
    finally:
        cur.close()
        conn.close()

    dados = {
        "nome": nome,
        "quantidade_mesas": int(mesas) if mesas else 5,
        "slug": "estabelecimento"
    }
    return templates.TemplateResponse(request, "configuracao.html", {"dados": dados, "mensagem": mensagem})


def rota_qrcode(request: Request):
    import psycopg2, psycopg2.extras
    try:
        conn = psycopg2.connect(dbname="cardapio_pro", user="postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute("SELECT * FROM administracao LIMIT 1;")
        admin = cur.fetchone()
        cur.close()
        conn.close()
        
        total_mesas = admin["mesas"] if admin and "mesas" in admin else 5
        nome_estab = admin["nome"] if admin and "nome" in admin else "Estabelecimento"
    except Exception:
        total_mesas = 5
        nome_estab = "Estabelecimento"
        
    return templates.TemplateResponse(request, "qrcode.html", {
        "nome_estabelecimento": nome_estab,
        "mesas": range(1, total_mesas + 1)
    })


def rota_qrcode(request: Request):
    import psycopg2, psycopg2.extras
    try:
        conn = psycopg2.connect(dbname="cardapio_pro", user="postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute("SELECT * FROM administracao LIMIT 1;")
        admin = cur.fetchone()
        cur.close()
        conn.close()
        
        total_mesas = admin["mesas"] if admin and "mesas" in admin else 5
        nome_estab = admin["nome"] if admin and "nome" in admin else "Estabelecimento"
    except Exception:
        total_mesas = 5
        nome_estab = "Estabelecimento"
        
    dados = {
        "nome_estabelecimento": nome_estab,
        "mesas": range(1, total_mesas + 1)
    }
    return templates.TemplateResponse(request, "qrcode.html", {"request": request, "dados": dados})


def rota_qrcode(request: Request):
    import psycopg2, psycopg2.extras
    try:
        conn = psycopg2.connect(dbname="cardapio_pro", user="postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute("SELECT * FROM administracao LIMIT 1;")
        admin = cur.fetchone()
        cur.close()
        conn.close()
        
        total_mesas = admin["mesas"] if admin and "mesas" in admin else 5
        nome_estab = admin["nome"] if admin and "nome" in admin else "Estabelecimento"
    except Exception:
        total_mesas = 5
        nome_estab = "Estabelecimento"
        
    base_url = str(request.base_url).rstrip("/")
    link_geral = f"{base_url}/cardapio"
    
    lista_mesas = []
    for i in range(1, total_mesas + 1):
        lista_mesas.append({
            "mesa": i,
            "link_acesso": f"{base_url}/cardapio?mesa={i}"
        })
        
    dados = {
        "status": "sucesso",
        "nome_estabelecimento": nome_estab,
        "link_geral": link_geral,
        "mesas": lista_mesas
    }
    return templates.TemplateResponse(request, "qrcode.html", {"request": request, "dados": dados})


def rota_qrcode(request: Request):
    from sisyten.qr_code import consultar_qr_code
    resultado = consultar_qr_code()
    # Ajusta o host dinamicamente baseado na requisição real
    base_url = str(request.base_url).rstrip("/")
    
    dados = resultado.get("dados", {})
    # Atualiza para usar o host atual do cliente
    dados["link_geral"] = f"{base_url}/cardapio"
    for m in dados.get("mesas", []):
        num = m["mesa"]
        m["link_acesso"] = f"{base_url}/mesa/{num}"
        import urllib.parse
        q = urllib.parse.quote(m["link_acesso"])
        m["qrcode_imagem_url"] = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={q}"

    return templates.TemplateResponse(request, "qrcode.html", {"request": request, "dados": dados})


def rota_qrcode(request: Request):
    from sisyten.qr_code import consultar_qr_code
    resultado = consultar_qr_code()
    base_url = str(request.base_url).rstrip("/")
    
    dados = resultado.get("dados", {})
    dados["link_geral"] = f"{base_url}/cardapio"
    for m in dados.get("mesas", []):
        num = m["mesa"]
        # Usa o formato com query string /cardapio?mesa=X que já é suportado pelo app.py
        m["link_acesso"] = f"{base_url}/cardapio?mesa={num}"
        import urllib.parse
        q = urllib.parse.quote(m["link_acesso"])
        m["qrcode_imagem_url"] = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={q}"

    return templates.TemplateResponse(request, "qrcode.html", {"request": request, "dados": dados})


def rota_qrcode(request: Request):
    from sisyten.qr_code import consultar_qr_code
    resultado = consultar_qr_code()
    base_url = str(request.base_url).rstrip("/")
    
    dados = resultado.get("dados", {})
    dados["link_geral"] = f"{base_url}/mesa/cardapio"
    for m in dados.get("mesas", []):
        num = m["mesa"]
        # Aponta para a rota correta do cardápio digital do digital.py
        m["link_acesso"] = f"{base_url}/mesa/cardapio?mesa={num}"
        import urllib.parse
        q = urllib.parse.quote(m["link_acesso"])
        m["qrcode_imagem_url"] = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={q}"

    return templates.TemplateResponse(request, "qrcode.html", {"request": request, "dados": dados})


@app.get("/qrcode", response_class=HTMLResponse)
def rota_qrcode(request: Request):
    from sisyten.qr_code import consultar_qr_code
    resultado = consultar_qr_code()
    base_url = str(request.base_url).rstrip("/")
    
    dados = resultado.get("dados", {})
    # Link geral agora aponta para mesa 0 (delivery/geral)
    dados["link_geral"] = f"{base_url}/mesa/cardapio?mesa=0"
    for m in dados.get("mesas", []):
        num = m["mesa"]
        m["link_acesso"] = f"{base_url}/mesa/cardapio?mesa={num}"
        import urllib.parse
        q = urllib.parse.quote(m["link_acesso"])
        m["qrcode_imagem_url"] = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={q}"

    return templates.TemplateResponse(request, "qrcode.html", {"request": request, "dados": dados})
