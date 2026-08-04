import psycopg2
import psycopg2.extras

def obter_dados_qrcode():
    """Busca o nome e a quantidade de mesas da administração para gerar os QR codes."""
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
        "nome_estabelecimento": nome_estab,
        "quantidade_mesas": total_mesas
    }
