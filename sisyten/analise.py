import json
import psycopg2
from psycopg2.extras import RealDictCursor

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
    """
    Lê a tabela 'transacoes' (que contém mesas e delivery), calcula os rendimentos
    por forma de pagamento (Pix, Cartão, Dinheiro), organiza o extrato por dia, mês e ano,
    permite filtro por período (data_inicio e data_fim) e salva o resultado reorganizado na tabela 'relatorio'.
    Payload: {
      "slug": "nome-do-estabelecimento",
      "filtro_tipo": "periodo", # 'geral', 'diario', 'mensal', 'anual', 'periodo'
      "data_inicio": "2026-01-01", # Opcional para filtro de a até b
      "data_fim": "2026-12-31"     # Opcional para filtro de a até b
    }
    """
    slug = dados.get("slug")
    filtro_tipo = dados.get("filtro_tipo", "geral")
    data_inicio = dados.get("data_inicio")
    data_fim = dados.get("data_fim")

    if not slug:
        return {"status": "erro", "mensagem": "O campo 'slug' é obrigatório para gerar a análise."}

    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        # Monta a query com filtros opcionais de data (de x a y)
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

        cur.execute(query, tuple(params))
        transacoes = cur.fetchall()

        # Estruturas para consolidação
        total_geral = 0.0
        rendimento_pix = 0.0
        rendimento_cartao = 0.0
        rendimento_dinheiro = 0.0

        extrato_organizado = []

        for t in transacoes:
            valor = float(t["valor_total"] or 0.0)
            total_geral += valor
            forma = (t["forma_pagamento"] or "").lower()

            if "pix" in forma:
                rendimento_pix += valor
            elif "cartao" in forma or "débito" in forma or "crédito" in forma:
                rendimento_cartao += valor
            elif "dinheiro" in forma:
                rendimento_dinheiro += valor

            criado_em_str = str(t["criado_em"])
            
            extrato_organizado.append({
                "id_transacao": t["id"],
                "tipo_pedido": t["tipo_pedido"], # 'mesa' ou 'delivery'
                "referencia": t["referencia_id"],
                "nome_cliente": t["nome_cliente"],
                "forma_pagamento": t["forma_pagamento"],
                "detalhes": t["detalhes_pagamento"],
                "valor": valor,
                "data_hora": criado_em_str
            })

        # Monta o pacote consolidado para os cards e relatório
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
            "extrato_detalhado": extrato_organizado,
            "acoes_interface": {
                "botao_imprimir": "imprimir_relatorio_extrato"
            }
        }

        # Salva todas as informações reorganizadas na tabela 'relatorio'
        cur.execute("""
            INSERT INTO relatorio (slug, tipo_filtro, periodo_referencia, dados_consolidados)
            VALUES (%s, %s, %s, %s)
            RETURNING id, criado_em;
        """, (slug, filtro_tipo, f"{data_inicio or 'inicio'} ate {data_fim or 'hoje'}", json.dumps(relatorio_conteudo)))

        salvo = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        relatorio_conteudo["relatorio_id"] = salvo["id"]
        relatorio_conteudo["gerado_em"] = str(salvo["criado_em"])

        return {
            "status": "sucesso",
            "mensagem": "Análise gerada com sucesso e salva na tabela relatório.",
            "dados": relatorio_conteudo
        }

    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao gerar análise e relatório: {str(e)}"}

def processar_requisicao(json_requisicao):
    """Ponto de entrada do menu Análise que recebe e devolve estritamente JSON."""
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
