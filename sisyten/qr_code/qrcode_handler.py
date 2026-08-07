import psycopg2
import psycopg2.extras
import json
import os

def obter_ip_atual():
    """Lê o IP atual salvo pelo script de captura."""
    caminhos_possiveis = ["dados/ip_atual.json", "ip_atual.json", "ip.json"]
    for caminho in caminhos_possiveis:
        if os.path.exists(caminho):
            try:
                with open(caminho, "r", encoding="utf-8") as f:
                    dados = json.load(f)
                    return dados.get("ip", "127.0.0.1")
            except Exception:
                pass
    return "127.0.0.1"

def obter_dados_qrcode():
    """Busca o IP, nome e quantidade de mesas para gerar os QR codes dinamicamente."""
    ip_atual = obter_ip_atual()
    
    try:
        conn = psycopg2.connect(dbname="cardapio_pro", user="postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        cur.execute("SELECT * FROM administracao LIMIT 1;")
        admin = cur.fetchone()

        total_mesas = admin["mesas"] if admin and "mesas" in admin else 5
        nome_estab = admin["nome"] if admin and "nome" in admin else "Estabelecimento"

        cur.close()
        conn.close()
    except Exception as e:
        print(f"Erro ao buscar dados para QR code: {e}")
        total_mesas = 5
        nome_estab = "Estabelecimento"

    return {
        "ip": ip_atual,
        "nome_estabelecimento": nome_estab,
        "quantidade_mesas": total_mesas
    }
