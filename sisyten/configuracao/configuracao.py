import psycopg2
from psycopg2.extras import RealDictCursor
import json

def consultar_configuracao():
    try:
        conn = psycopg2.connect(dbname="cardapio_pro", user="postgres", password="", host="localhost", port="5432")
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT id, nome, mesas FROM administracao ORDER BY id DESC LIMIT 1;")
        res = cur.fetchone()
        cur.close()
        conn.close()
        
        if res:
            return {"status": "sucesso", "dados": dict(res)}
        else:
            return {
                "status": "sucesso",
                "dados": {"nome": "Meu Estabelecimento", "mesas": 10}
            }
    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao consultar: {str(e)}"}

def salvar_ou_atualizar_configuracao(dados):
    try:
        nome = dados.get("nome", "Meu Estabelecimento")
        mesas = int(dados.get("mesas", 10) or 10)

        conn = psycopg2.connect(dbname="cardapio_pro", user="postgres", password="", host="localhost", port="5432")
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        cur.execute("SELECT id FROM administracao ORDER BY id DESC LIMIT 1;")
        res = cur.fetchone()
        
        if res:
            adm_id = res["id"]
            cur.execute("UPDATE administracao SET nome = %s, mesas = %s WHERE id = %s;", (nome, mesas, adm_id))
        else:
            cur.execute("INSERT INTO administracao (nome, mesas) VALUES (%s, %s);", (nome, mesas))
        
        conn.commit()
        cur.close()
        conn.close()
        
        return {"status": "sucesso", "mensagem": "Configurações atualizadas com sucesso."}
    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao salvar: {str(e)}"}

def processar_requisicao(requisicao_json):
    try:
        req = json.loads(requisicao_json)
        acao = req.get("acao")
        dados = req.get("dados", {})
        
        if acao == "consultar":
            return json.dumps(consultar_configuracao())
        elif acao == "salvar":
            return json.dumps(salvar_ou_atualizar_configuracao(dados))
        else:
            return json.dumps({"status": "erro", "mensagem": "Ação inválida."})
    except Exception as e:
        return json.dumps({"status": "erro", "mensagem": f"Erro interno: {str(e)}"})
