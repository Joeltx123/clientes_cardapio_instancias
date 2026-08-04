import json
import psycopg2
import pandas as pd

DB_CONFIG = {
    "dbname": "cardapio_pro",
    "user": "postgres",
    "password": "",
    "host": "localhost",
    "port": "5432"
}

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)

def gerar_analise_e_relatorio(dados):
    slug = dados.get("slug")
    filtro_tipo = dados.get("filtro_tipo", "geral")
    data_inicio = dados.get("data_inicio")
    data_fim = dados.get("data_fim")

    if not slug:
        return {"status": "erro", "mensagem": "O campo 'slug' é obrigatório para gerar a análise."}

    try:
        conn = get_db_connection()
        
        # Lê a tabela transacoes diretamente para um DataFrame do pandas
        query = """
            SELECT id, slug, tipo_pedido, referencia_id, nome_cliente,
                   forma_pagamento, detalhes_pagamento, valor_total, criado_em
            FROM transacoes
            WHERE slug = %s
        """
        params = [slug]

        if data_inicio and data_fim:
            query += " AND criado_em::date BETWEEN %s AND %s"
            params.extend([data_inicio, data_fim])

        query += " ORDER BY criado_em DESC;"

        df = pd.read_sql(query, conn, params=params)
        
        # Fecha a conexão com o banco
        conn.close()

        if df.empty:
            relatorio_conteudo = {
                "slug": slug,
                "filtro_aplicado": filtro_tipo,
                "periodo": {"data_inicio": data_inicio, "data_fim": data_fim},
                "cards_rendimento": {"total_geral": 0.0, "pix": 0.0, "cartao": 0.0, "dinheiro": 0.0},
                "extrato_detalhado": [],
            }
            return {"status": "sucesso", "mensagem": "Nenhuma transação encontrada.", "dados": relatorio_conteudo}

        # Tratamento de valores com pandas
        df["valor_total"] = pd.to_numeric(df["valor_total"], errors="fillna").fillna(0.0)
        df["forma_pagamento"] = df["forma_pagamento"].fillna("").str.lower()

        total_geral = float(df["valor_total"].sum())
        
        # Agrupamentos rápidos usando pandas
        rendimento_pix = float(df[df["forma_pagamento"].str.contains("pix", na=False)]["valor_total"].sum())
        rendimento_cartao = float(df[df["forma_pagamento"].str.contains("cartao|débito|crédito", na=False, regex=True)]["valor_total"].sum())
        rendimento_dinheiro = float(df[df["forma_pagamento"].str.contains("dinheiro", na=False)]["valor_total"].sum())

        # Monta o extrato detalhado formatado
        extrato_organizado = []
        for _, t in df.iterrows():
            extrato_organizado.append({
                "id_transacao": int(t["id"]),
                "tipo_pedido": str(t["tipo_pedido"]),
                "referencia": str(t["referencia_id"]),
                "nome_cliente": str(t["nome_cliente"] or "-"),
                "forma_pagamento": str(t["forma_pagamento"]),
                "detalhes": str(t["detalhes_pagamento"] or ""),
                "valor": float(t["valor_total"]),
                "data_hora": str(t["criado_em"])
            })

        relatorio_conteudo = {
            "slug": slug,
            "filtro_aplicado": filtro_tipo,
            "periodo": {"data_inicio": data_inicio, "data_fim": data_fim},
            "cards_rendimento": {
                "total_geral": round(total_geral, 2),
                "pix": round(rendimento_pix, 2),
                "cartao": round(rendimento_cartao, 2),
                "dinheiro": round(rendimento_dinheiro, 2)
            },
            "extrato_detalhado": extrato_organizado
        }

        # Salva o relatório consolidado na base de dados
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO relatorio (slug, tipo_filtro, periodo_referencia, dados_consolidados)
            VALUES (%s, %s, %s, %s)
            RETURNING id, criado_em;
        """, (slug, filtro_tipo, f"{data_inicio or 'inicio'} ate {data_fim or 'hoje'}", json.dumps(relatorio_conteudo)))

        salvo = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        relatorio_conteudo["relatorio_id"] = salvo[0]
        relatorio_conteudo["gerado_em"] = str(salvo[1])

        return {
            "status": "sucesso",
            "mensagem": "Análise gerada com pandas e salva com sucesso.",
            "dados": relatorio_conteudo
        }

    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao gerar análise com pandas: {str(e)}"}

def processar_requisicao(json_requisicao):
    try:
        req = json.loads(json_requisicao) if isinstance(json_requisicao, str) else json_requisicao
        acao = req.get("acao")
        dados = req.get("dados", {})

        if acao in ["gerar_analise", "consultar_relatorio"]:
            resposta = gerar_analise_e_relatorio(dados)
        else:
            resposta = {"status": "erro", "mensagem": f"Ação '{acao}' não reconhecida no menu Análise."}

        return json.dumps(resposta, ensure_ascii=False)

    except Exception as e:
        return json.dumps({"status": "erro", "mensagem": f"Erro no processamento JSON do menu Análise: {str(e)}"}, ensure_ascii=False)
