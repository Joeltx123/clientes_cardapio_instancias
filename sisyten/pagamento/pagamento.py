import json
import psycopg2

def get_db_connection():
    return psycopg2.connect(dbname="cardapio_pro", user="postgres", password="", host="localhost", port="5432")

def consultar_painel_pagamento():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, referencia_id, forma_pagamento, valor_total, criado_em FROM transacoes ORDER BY id DESC LIMIT 50;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        
        transacoes = []
        for r in rows:
            transacoes.append({
                "id": r[0],
                "referencia": r[1],
                "forma_pagamento": r[2],
                "valor": float(r[3]) if r[3] else 0.0,
                "criado_em": str(r[4]) if r[4] else ""
            })
        return {"status": "sucesso", "transacoes": transacoes}
    except Exception as e:
        return {"status": "erro", "mensagem": str(e), "transacoes": []}

def processar_requisicao(payload):
    if isinstance(payload, str):
        try:
            payload = json.loads(payload)
        except:
            return json.dumps({"status": "erro", "mensagem": "JSON inválido"})
            
    acao = payload.get("acao")
    
    if acao == "consultar_painel":
        resultado = consultar_painel_pagamento()
        return json.dumps(resultado)
    else:
        return json.dumps({"status": "erro", "mensagem": "Ação desconhecida"})
