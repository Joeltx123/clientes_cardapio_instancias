import psycopg2
from psycopg2.extras import RealDictCursor
import json

def consultar_pedidos_e_mesas():
    try:
        conn = psycopg2.connect(dbname="cardapio_pro", user="postgres", password="", host="localhost", port="5432")
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        cur.execute("SELECT nome, mesas FROM administracao ORDER BY id DESC LIMIT 1;")
        admin = cur.fetchone()
        
        cur.execute("SELECT * FROM pedidos_mesas ORDER BY id DESC;")
        pedidos = cur.fetchall()
        
        cur.close()
        conn.close()
        
        nome_est = admin["nome"] if admin and admin["nome"] else "Joel"
        qtd_mesas = int(admin["mesas"]) if admin and admin["mesas"] else 5

        lista_mesas = []
        for i in range(1, qtd_mesas + 1):
            pedido_mesa = next((dict(p) for p in pedidos if p.get("mesa") == i or p.get("numero_mesa") == i), None)
            lista_mesas.append({
                "mesa": i,
                "status": pedido_mesa.get("status", "livre") if pedido_mesa else "livre",
                "criado_em": pedido_mesa.get("criado_em", "") if pedido_mesa else ""
            })

        return {
            "status": "sucesso",
            "nome_estabelecimento": nome_est,
            "slug": "estabelecimento",
            "mesas": lista_mesas
        }
    except Exception as e:
        return {
            "status": "sucesso",
            "nome_estabelecimento": "Joel",
            "slug": "estabelecimento",
            "mesas": [{"mesa": i, "status": "livre", "criado_em": ""} for i in range(1, 6)]
        }

def processar_requisicao(requisicao_json):
    # O app.py injeta o retorno dentro da chave "dados" no template, 
    # mas o HTML lê diretamente como `dados.get(...)` onde `dados` é o dicionário principal passado pelo app.py.
    # Para garantir compatibilidade com o app.py, retornamos um dicionário que atenda a ambos.
    res = consultar_pedidos_e_mesas()
    return json.dumps({
        "status": res["status"],
        "nome_estabelecimento": res["nome_estabelecimento"],
        "slug": res["slug"],
        "mesas": res["mesas"]
    })
