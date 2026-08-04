import psycopg2
from psycopg2.extras import RealDictCursor
import json
import pandas as pd
from sisyten import json_core

def consultar_pedidos_e_mesas():
    try:
        conn = psycopg2.connect(dbname="cardapio_pro", user="postgres", password="", host="localhost", port="5432")
        
        # Consultas usando pandas para alto desempenho na leitura do banco
        admin_df = pd.read_sql("SELECT nome, mesas FROM administracao ORDER BY id DESC LIMIT 1;", conn)
        pedidos_df = pd.read_sql("SELECT * FROM pedidos_mesas ORDER BY id DESC;", conn)
        
        conn.close()

        # Extração de configurações com pandas/fallback
        nome_est = "Joel"
        qtd_mesas = 5
        if not admin_df.empty:
            nome_est = admin_df.iloc[0].get("nome") or "Joel"
            qtd_mesas = int(admin_df.iloc[0].get("mesas") or 5)

        lista_mesas = []
        for i in range(1, qtd_mesas + 1):
            # Filtra pedidos da mesa atual usando pandas se houver registros
            pedido_mesa = None
            if not pedidos_df.empty:
                match = pedidos_df[
                    (pedidos_df.get("mesa") == i) | (pedidos_df.get("numero_mesa") == i)
                ]
                if not match.empty:
                    pedido_mesa = match.iloc[0].to_dict()

            lista_mesas.append({
                "mesa": i,
                "status": pedido_mesa.get("status", "livre") if pedido_mesa else "livre",
                "criado_em": str(pedido_mesa.get("criado_em", "")) if pedido_mesa and pd.notna(pedido_mesa.get("criado_em")) else ""
            })

        resultado = {
            "status": "sucesso",
            "nome_estabelecimento": nome_est,
            "slug": "estabelecimento",
            "mesas": lista_mesas
        }
        return resultado

    except Exception as e:
        print(f"[AVISO] Erro ao consultar banco em pedidos.py: {e}. Usando dados padrão.")
        return {
            "status": "sucesso",
            "nome_estabelecimento": "Joel",
            "slug": "estabelecimento",
            "mesas": [{"mesa": i, "status": "livre", "criado_em": ""} for i in range(1, 6)]
        }

def processar_requisicao(requisicao_json):
    res = consultar_pedidos_e_mesas()
    
    # Utiliza a conversão padronizada do json_core para garantir logs e segurança
    df_res = pd.DataFrame([res])
    json_str = json_core.dataframe_para_json(df_res)
    
    # Retorna o formato esperado pelo app.py convertido via json_core
    dados_finais = json_core.json_para_dataframe(json_str).iloc[0].to_dict()
    # Como as 'mesas' precisam retornar como lista, garantimos o formato estruturado
    dados_finais["mesas"] = res["mesas"]
    
    return json.dumps(dados_finais, ensure_ascii=False)
