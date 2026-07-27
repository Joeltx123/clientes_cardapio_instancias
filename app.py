import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import inspetor
from banco import conectar
from controle_sistema import checar_bloqueio_requisicao

# Importando os routers (blueprints adaptados)
from routes.config import config_bp
from routes.cardapio import cardapio_bp
from routes.pedidos import pedidos_bp
from routes.qrcode import qrcode_bp
from routes.pagamento import pagamento_bp
from routes.analise import analise_bp
from routes.controle_sistema import controle_bp
from routes.alerta_mesa import alerta_mesa_bp
from routes.backup import backup_bp

app = FastAPI(title="Cardápio Pro API")

# Middleware global para capturar erros e checar bloqueio de sistema
@app.middleware("http")
async def middleware_global(request: Request, call_next):
    # 1. Verifica bloqueio do sistema vindo da matriz
    resposta_bloqueio = checar_bloqueio_requisicao(request.url.path)
    if resposta_bloqueio:
        return resposta_bloqueio
    
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        inspetor.capturar_erro(e)
        raise e

# Registrando os routers (equivalentes aos Blueprints do Flask)
app.include_router(config_bp)
app.include_router(cardapio_bp)
app.include_router(pedidos_bp)
app.include_router(qrcode_bp)
app.include_router(pagamento_bp)
app.include_router(analise_bp)
app.include_router(controle_bp)
app.include_router(alerta_mesa_bp)
app.include_router(backup_bp)

# Rota principal (redireciona para configurações)
@app.get("/")
def index():
    return RedirectResponse(url="/configuracoes") # Ajustado para a rota padrão de config

# Painel de Análise
@app.post("/analise")
@app.get("/analise")
def painel_analise(
    ano: str = Form(default=""),
    mes: str = Form(default=""),
    data_inicio: str = Form(default=""),
    data_fim: str = Form(default="")
):
    conn = conectar()
    cur = conn.cursor()

    where_clauses = ["p.status IN ('pago', 'finalizado')", "p.data_finalizacao IS NOT NULL"]
    params = []

    if data_inicio and data_fim:
        where_clauses.append("p.data_finalizacao::date BETWEEN %s AND %s")
        params.extend([data_inicio, data_fim])
    elif ano and mes:
        where_clauses.append("EXTRACT(YEAR FROM p.data_finalizacao) = %s AND EXTRACT(MONTH FROM p.data_finalizacao) = %s")
        params.extend([int(ano), int(mes)])
    elif ano:
        where_clauses.append("EXTRACT(YEAR FROM p.data_finalizacao) = %s")
        params.append(int(ano))

    where_sql = " WHERE " + " AND ".join(where_clauses)

    cur.execute(f"""
        SELECT SUM(i.preco)
        FROM pedidos p
        JOIN itens_pedido ip ON p.id = ip.pedido_id
        JOIN itens i ON ip.item_id = i.id
        {where_sql}
    """, tuple(params))
    res_fat = cur.fetchone()
    faturamento_total = float(res_fat[0]) if res_fat and res_fat[0] else 0.0

    cur.execute(f"""
        SELECT p.forma_pagamento, SUM(i.preco)
        FROM pedidos p
        JOIN itens_pedido ip ON p.id = ip.pedido_id
        JOIN itens i ON ip.item_id = i.id
        {where_sql}
        GROUP BY p.forma_pagamento
    """, tuple(params))
    brutos_forma = cur.fetchall()

    por_forma = {'pix': 0.0, 'cartao': 0.0, 'dinheiro': 0.0}
    for row in brutos_forma:
        nome_pgto = (row[0] or "").lower()
        val = float(row[1]) if row[1] is not None else 0.0
        if 'pix' in nome_pgto:
            por_forma['pix'] += val
        elif 'cartao' in nome_pgto:
            por_forma['cartao'] += val
        elif 'dinheiro' in nome_pgto:
            por_forma['dinheiro'] += val

    cur.execute(f"""
        SELECT TO_CHAR(p.data_finalizacao, 'DD/MM/YYYY') as dia, SUM(i.preco)
        FROM pedidos p
        JOIN itens_pedido ip ON p.id = ip.pedido_id
        JOIN itens i ON ip.item_id = i.id
        {where_sql}
        GROUP BY dia
        ORDER BY MIN(p.data_finalizacao) DESC
    """, tuple(params))
    faturamento_por_dia = cur.fetchall()

    cur.execute(f"""
        SELECT TO_CHAR(p.data_finalizacao, 'MM/YYYY') as mes, SUM(i.preco)
        FROM pedidos p
        JOIN itens_pedido ip ON p.id = ip.pedido_id
        JOIN itens i ON ip.item_id = i.id
        {where_sql}
        GROUP BY mes
        ORDER BY MIN(p.data_finalizacao) DESC
    """, tuple(params))
    faturamento_por_mes = cur.fetchall()

    cur.execute(f"""
        SELECT TO_CHAR(p.data_finalizacao, 'YYYY') as ano, SUM(i.preco)
        FROM pedidos p
        JOIN itens_pedido ip ON p.id = ip.pedido_id
        JOIN itens i ON ip.item_id = i.id
        {where_sql}
        GROUP BY ano
        ORDER BY ano DESC
    """, tuple(params))
    faturamento_por_ano = cur.fetchall()

    cur.close()
    conn.close()

    # Retorno estruturado (ajuste para templates se utilizar Jinja2 nativo)
    return {
        "faturamento_total": faturamento_total,
        "por_forma": por_forma,
        "faturamento_por_dia": faturamento_por_dia,
        "faturamento_por_mes": faturamento_por_mes,
        "faturamento_por_ano": faturamento_por_ano
    }

# Painel de Registros
@app.get("/registros")
def painel_registros():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT p.mesa, p.forma_pagamento, SUM(i.preco) as total, p.troco, p.data_finalizacao, p.id
        FROM pedidos p
        JOIN itens_pedido ip ON p.id = ip.pedido_id
        JOIN itens i ON ip.item_id = i.id
        WHERE p.status IN ('pago', 'finalizado')
        GROUP BY p.mesa, p.forma_pagamento, p.troco, p.data_finalizacao, p.id
        ORDER BY p.id DESC
    """)
    bruto_historico = cur.fetchall()

    historico = []
    for row in bruto_historico:
        mesa = row[0]
        forma = row[1] or 'Não informada'
        total = float(row[2]) if row[2] is not None else 0.0
        troco = float(row[3]) if row[3] is not None else 0.0

        data_obj = row[4]
        if data_obj:
            try:
                data_formatada = data_obj.strftime('%d/%m/%Y %H:%M')
            except AttributeError:
                data_formatada = str(data_obj)
        else:
            data_formatada = 'Não registrada'

        historico.append((data_formatada, mesa, forma, total, troco))

    cur.execute("""
        SELECT SUM(i.preco)
        FROM pedidos p
        JOIN itens_pedido ip ON p.id = ip.pedido_id
        JOIN itens i ON ip.item_id = i.id
        WHERE p.status IN ('pago', 'finalizado')
    """)
    res_faturamento = cur.fetchone()
    faturamento_total = float(res_faturamento[0]) if res_faturamento and res_faturamento[0] else 0.0

    cur.close()
    conn.close()

    return {
        "historico": historico,
        "faturamento_total": faturamento_total
    }

@app.get("/admin/delivery")
def painel_delivery():
    return {"status": "Painel delivery ativo"}

if __name__ == '__main__':
    import uvicorn
    porta_dinamica = int(os.environ.get('PORT', 5003))
    uvicorn.run("main:app", host="0.0.0.0", port=porta_dinamica, reload=True)


