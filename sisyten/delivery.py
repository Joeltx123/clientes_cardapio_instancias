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

def gerar_link_delivery(dados):
    """
    Gera o link único e individual de Delivery do estabelecimento baseado no slug.
    Permite acesso simultâneo de múltiplos clientes ao cardápio online delivery.
    Payload: {"slug": "nome-do-estabelecimento"}
    """
    slug = dados.get("slug")
    if not slug:
        return {"status": "erro", "mensagem": "O campo 'slug' é obrigatório para gerar o link de delivery."}

    link_delivery = f"https://cardapiopro.com/{slug}/delivery"
    
    return {
        "status": "sucesso",
        "slug": slug,
        "link_delivery": link_delivery,
        "mensagem": "Link de delivery gerado com sucesso. Múltiplos clientes podem acessar simultaneamente."
    }

def receber_pedido_delivery(dados):
    """
    Recebe o JSON do cardápio online delivery contendo os dados do cliente e os itens.
    Salva integralmente na tabela 'pedidos_delivery'.
    Payload esperado: {
      "slug": "...",
      "nome_cliente": "João da Silva",
      "telefone": "(27) 99999-9999",
      "endereco": "Rua Exemplo, 123",
      "itens": [...],
      "pagamento": {"forma": "dinheiro", "troco_para": 50.00}
    }
    """
    slug = dados.get("slug")
    nome_cliente = dados.get("nome_cliente")

    if not slug or not nome_cliente:
        return {"status": "erro", "mensagem": "Campos obrigatórios ausentes: 'slug' e 'nome_cliente' são necessários."}

    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute("""
            INSERT INTO pedidos_delivery (slug, nome_cliente, dados_pedido, status)
            VALUES (%s, %s, %s, 'pendente')
            RETURNING id, nome_cliente, criado_em;
        """, (slug, nome_cliente, json.dumps(dados)))

        novo_pedido = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        novo_pedido["criado_em"] = str(novo_pedido["criado_em"])
        return {
            "status": "sucesso",
            "mensagem": f"Pedido delivery de {nome_cliente} registrado com sucesso.",
            "pedido_id": novo_pedido["id"]
        }

    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao salvar pedido delivery: {str(e)}"}

def listar_pedidos_delivery(dados):
    """
    Lista todos os pedidos delivery ativos separados por nome do cliente.
    Payload: {"slug": "..."}
    """
    slug = dados.get("slug")
    if not slug:
        return {"status": "erro", "mensagem": "O campo 'slug' é obrigatório."}

    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute("""
            SELECT id, slug, nome_cliente, dados_pedido, status, criado_em 
            FROM pedidos_delivery 
            WHERE slug = %s AND status = 'pendente'
            ORDER BY criado_em ASC;
        """, (slug,))

        pedidos = cur.fetchall()
        cur.close()
        conn.close()

        for p in pedidos:
            p["criado_em"] = str(p["criado_em"])

        return {
            "status": "sucesso",
            "slug": slug,
            "total_pedidos": len(pedidos),
            "pedidos": pedidos
        }

    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao listar pedidos delivery: {str(e)}"}

def processar_acao_pedido_delivery(dados):
    """
    Gerencia as ações do painel de Delivery:
    - 'liberar_errado': Apaga/limpa o pedido do sistema em caso de pedido errado.
    - 'enviar_motoboy': Marca como pronto/enviado, arquiva o pedido e registra a transação.
    Payload: {
      "pedido_id": 1,
      "acao_tipo": "enviar_motoboy", # ou "liberar_errado"
      "pagamento": {"forma": "pix", "valor": 45.00},
      "valor_total": 45.00
    }
    """
    pedido_id = dados.get("pedido_id")
    acao_tipo = dados.get("acao_tipo")

    if not pedido_id or not acao_tipo:
        return {"status": "erro", "mensagem": "Campos 'pedido_id' e 'acao_tipo' são obrigatórios."}

    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        # Busca o pedido original
        cur.execute("SELECT * FROM pedidos_delivery WHERE id = %s;", (pedido_id,))
        pedido = cur.fetchone()

        if not pedido:
            cur.close()
            conn.close()
            return {"status": "erro", "mensagem": "Pedido delivery não encontrado."}

        slug = pedido["slug"]
        nome_cliente = pedido["nome_cliente"]
        dados_brutos = pedido["dados_pedido"]

        if acao_tipo == "liberar_errado":
            # Apaga o pedido do sistema (caso de pedido errado)
            cur.execute("DELETE FROM pedidos_delivery WHERE id = %s;", (pedido_id,))
            conn.commit()
            cur.close()
            conn.close()
            return {"status": "sucesso", "mensagem": f"Pedido ID {pedido_id} de {nome_cliente} foi cancelado e limpo do sistema."}

        elif acao_tipo == "enviar_motoboy":
            # Pedido pronto/enviado: remove dos pendentes e salva na tabela transacoes
            pagamento_info = dados.get("pagamento", {})
            forma_pagamento = pagamento_info.get("forma", "desconhecido")
            valor_total = dados.get("valor_total", 0.00)

            # Insere na tabela transacoes (separando a coluna delivery)
            cur.execute("""
                INSERT INTO transacoes (slug, tipo_pedido, referencia_id, nome_cliente, forma_pagamento, detalhes_pagamento, valor_total)
                VALUES (%s, 'delivery', %s, %s, %s, %s, %s);
            """, (slug, pedido_id, nome_cliente, forma_pagamento, json.dumps(pagamento_info), valor_total))

            # Remove da lista de pendentes ativos
            cur.execute("DELETE FROM pedidos_delivery WHERE id = %s;", (pedido_id,))

            conn.commit()
            cur.close()
            conn.close()

            return {
                "status": "sucesso",
                "mensagem": f"Pedido de {nome_cliente} enviado para entrega e histórico salvo nas Transações com sucesso."
            }
        else:
            cur.close()
            conn.close()
            return {"status": "erro", "mensagem": "Ação de delivery inválida."}

    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao processar ação do pedido delivery: {str(e)}"}

def processar_requisicao(json_requisicao):
    """Ponto de entrada do menu Delivery que recebe e devolve estritamente JSON."""
    try:
        req = json.loads(json_requisicao) if isinstance(json_requisicao, str) else json_requisicao
        acao = req.get("acao")
        dados = req.get("dados", {})

        if acao == "gerar_link":
            resposta = gerar_link_delivery(dados)
        elif acao == "novo_pedido":
            resposta = receber_pedido_delivery(dados)
        elif acao == "listar":
            resposta = listar_pedidos_delivery(dados)
        elif acao == "processar_pedido":
            resposta = processar_acao_pedido_delivery(dados)
        else:
            resposta = {"status": "erro", "mensagem": f"Ação '{acao}' não reconhecida no menu Delivery."}

        return json.dumps(resposta, ensure_ascii=False)

    except Exception as e:
        return json.dumps({"status": "erro", "mensagem": f"Erro no processamento JSON do menu Delivery: {str(e)}"}, ensure_ascii=False)
