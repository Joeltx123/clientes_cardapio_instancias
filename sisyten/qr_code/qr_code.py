import psycopg2
from psycopg2.extras import RealDictCursor
import json
import urllib.parse

def consultar_qr_code(request_host="0.0.0.0:8000"):
    try:
        conn = psycopg2.connect(dbname="cardapio_pro", user="postgres", password="", host="localhost", port="5432")
        cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute("SELECT nome, mesas FROM administracao ORDER BY id DESC LIMIT 1;")
        admin = cur.fetchone()

        cur.close()
        conn.close()

        nome_est = admin["nome"] if admin and admin["nome"] else "Joel"
        qtd_mesas = int(admin["mesas"]) if admin and admin["mesas"] else 5

        # Aponta o link geral/delivery para o cardápio digital de delivery
        link_geral = f"http://localhost:8000/delivery/cardapio"
        q_geral = urllib.parse.quote(link_geral)
        qrcode_geral_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={q_geral}"

        lista_mesas = []
        for i in range(1, qtd_mesas + 1):
            link_mesa = f"http://localhost:8000/mesa/cardapio?mesa={i}"
            q_mesa = urllib.parse.quote(link_mesa)
            qrcode_mesa_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={q_mesa}"

            lista_mesas.append({
                "mesa": i,
                "link_acesso": link_mesa,
                "qrcode_imagem_url": qrcode_mesa_url
            })

        return {
            "status": "sucesso",
            "dados": {
                "nome_estabelecimento": nome_est,
                "slug": "estabelecimento",
                "mesas_totais": qtd_mesas,
                "link_geral": link_geral,
                "qrcode_geral_imagem_url": qrcode_geral_url,
                "mesas": lista_mesas
            }
        }
    except Exception as e:
        link_geral = "http://localhost:8000/delivery/cardapio"
        q_geral = urllib.parse.quote(link_geral)
        qrcode_geral_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={q_geral}"

        lista_mesas = []
        for i in range(1, 6):
            link_mesa = f"http://localhost:8000/mesa/cardapio?mesa={i}"
            q_mesa = urllib.parse.quote(link_mesa)
            lista_mesas.append({
                "mesa": i,
                "link_acesso": link_mesa,
                "qrcode_imagem_url": f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={q_mesa}"
            })

        return {
            "status": "sucesso",
            "dados": {
                "nome_estabelecimento": "Joel",
                "slug": "estabelecimento",
                "mesas_totais": 5,
                "link_geral": link_geral,
                "qrcode_geral_imagem_url": qrcode_geral_url,
                "mesas": lista_mesas
            }
        }

def processar_requisicao(requisicao_json):
    return json.dumps(consultar_qr_code())
