import psycopg2
import psycopg2.extras

def obter_dados():
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
        print(f"Erro ao buscar dados para pedidos: {e}")
        total_mesas = 5
        nome_estab = "Estabelecimento"
    
    mesas = []
    for i in range(1, total_mesas + 1):
        mesas.append({"mesa": i, "status": "livre", "itens": [], "total": 0.0})
        
    return {
        "status": "sucesso",
        "nome_estabelecimento": nome_estab,
        "mesas": mesas
    }

def processar_requisicao(payload_json):
    import json
    dados = json.loads(payload_json)
    if dados.get("acao") == "liberar_mesa":
        pass
