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

def consultar_painel_pagamento(dados):
    """
    Lê o slug do estabelecimento e separa em duas abas:
    - Aba 'mesas': Pega os pedidos ativos da tabela 'pedidos_mesas' (com extrato completo, preços e itens).
    - Aba 'delivery': Pega os pedidos ativos da tabela 'pedidos_delivery' (marcados com ID 0).
    Payload: {"slug": "nome-do-estabelecimento"}
    """
    slug = dados.get("slug")
    if not slug:
        return {"status": "erro", "mensagem": "O campo 'slug' é obrigatório."}

    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        # 1. Busca os pedidos de Mesas com extrato completo, preços e itens
        cur.execute("""
            SELECT id, mesa, dados_pedido, criado_em 
            FROM pedidos_mesas 
            WHERE slug = %s AND status = 'ocupada'
            ORDER BY mesa ASC;
        """, (slug,))
        
        mesas_ativas = []
        for row in cur.fetchall():
            dados_brutos = row["dados_pedido"]
            # Garante o formato de ID 1 / estrutura da mesa
            mesas_ativas.append({
                "id_pedido": row["id"],
                "tipo_origem": "mesa",
                "mesa": row["mesa"],
                "extrato_completo": dados_brutos, # Contém itens e preços
                "criado_em": str(row["criado_em"])
            })

        # 2. Busca os pedidos de Delivery (ID 0)
        cur.execute("""
            SELECT id, nome_cliente, dados_pedido, criado_em 
            FROM pedidos_delivery 
            WHERE slug = %s AND status = 'pendente'
            ORDER BY criado_em ASC;
        """, (slug,))

        delivery_ativos = []
        for row in cur.fetchall():
            dados_brutos = row["dados_pedido"]
            delivery_ativos.append({
                "id_pedido": row["id"], # Mantém referência/ID 0 ou ID real do delivery
                "identificador_id": 0,
                "tipo_origem": "delivery",
                "nome_cliente": row["nome_cliente"],
                "extrato_completo": dados_brutos,
                "criado_em": str(row["criado_em"]),
                "acao_redirecionamento": "encaminhar_para_menu_delivery"
            })

        cur.close()
        conn.close()

        return {
            "status": "sucesso",
            "slug": slug,
            "aba_mesas": mesas_ativas,
            "aba_delivery": delivery_ativos
        }

    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao consultar painel de pagamento: {str(e)}"}

def processar_pagamento_mesa(dados):
    """
    Processa o pagamento de uma mesa, calcula trocos, parcelas, 
    salva na tabela 'transacoes' e libera/desocupa a mesa.
    Payload: {
      "slug": "...",
      "mesa": 3,
      "id_pedido": 1,
      "nome_cliente": "Cliente Mesa",
      "forma_pagamento": "dinheiro", # 'pix', 'dinheiro', 'cartao_debito', 'cartao_credito'
      "valor_pedido": 120.50,
      "detalhes_pagamento": {
         "valor_pago": 150.00, # se dinheiro (calcula troco)
         "parcelas": 3        # se cartao_credito
      }
    }
    """
    slug = dados.get("slug")
    mesa = dados.get("mesa")
    id_pedido = dados.get("id_pedido")
    nome_cliente = dados.get("nome_cliente", f"Mesa {mesa}")
    forma_pagamento = dados.get("forma_pagamento")
    valor_pedido = dados.get("valor_pedido", 0.00)
    detalhes = dados.get("detalhes_pagamento", {})

    if not slug or mesa is None or not forma_pagamento:
        return {"status": "erro", "mensagem": "Campos obrigatórios ausentes para o pagamento."}

    troco = 0.00
    if forma_pagamento == "dinheiro":
        valor_pago = detalhes.get("valor_pago", valor_pedido)
        if valor_pago > valor_pedido:
            troco = round(valor_pago - valor_pedido, 2)
        detalhes["troco"] = troco

    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        # 1. Salva a transação na tabela unificada 'transacoes'
        cur.execute("""
            INSERT INTO transacoes (slug, tipo_pedido, referencia_id, nome_cliente, forma_pagamento, detalhes_pagamento, valor_total)
            VALUES (%s, 'mesa', %s, %s, %s, %s, %s)
            RETURNING id, criado_em;
        """, (slug, mesa, nome_cliente, forma_pagamento, json.dumps(detalhes), valor_pedido))
        
        transacao_criada = cur.fetchone()

        # 2. Libera/desocupa a mesa apagando o pedido ativo correspondente
        cur.execute("""
            DELETE FROM pedidos_mesas 
            WHERE slug = %s AND mesa = %s;
        """, (slug, mesa))

        conn.commit()
        cur.close()
        conn.close()

        transacao_criada["criado_em"] = str(transacao_criada["criado_em"])

        resposta_sucesso = {
            "status": "sucesso",
            "mensagem": f"Pagamento da Mesa {mesa} processado com sucesso e mesa liberada.",
            "transacao_id": transacao_criada["id"],
            "forma_pagamento": forma_pagamento,
            "valor_total": valor_pedido
        }

        if forma_pagamento == "dinheiro":
            resposta_sucesso["troco"] = troco

        return resposta_sucesso

    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao processar pagamento da mesa: {str(e)}"}

def processar_requisicao(json_requisicao):
    """Ponto de entrada do menu Pagamento que recebe e devolve estritamente JSON."""
    try:
        req = json.loads(json_requisicao) if isinstance(json_requisicao, str) else json_requisicao
        acao = req.get("acao")
        dados = req.get("dados", {})

        if acao == "consultar_painel":
            resposta = consultar_painel_pagamento(dados)
        elif acao == "pagar_mesa":
            resposta = processar_pagamento_mesa(dados)
        else:
            resposta = {"status": "erro", "mensagem": f"Ação '{acao}' não reconhecida no menu Pagamento."}

        return json.dumps(resposta, ensure_ascii=False)

    except Exception as e:
        return json.dumps({"status": "erro", "mensagem": f"Erro no processamento JSON do menu Pagamento: {str(e)}"}, ensure_ascii=False)
