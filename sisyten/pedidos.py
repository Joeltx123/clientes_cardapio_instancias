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

def inicializar_tabela_pedidos():
    """Garante que a tabela 'pedidos_mesas' existe no banco de dados."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS pedidos_mesas (
                id SERIAL PRIMARY KEY,
                slug VARCHAR(255) NOT NULL,
                mesa INT NOT NULL,
                dados_pedido JSONB NOT NULL,
                status VARCHAR(50) DEFAULT 'ocupada',
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Erro ao inicializar tabela pedidos_mesas: {e}")

inicializar_tabela_pedidos()

def consultar_painel_mesas():
    """
    Lê a tabela 'administracao' para pegar o nome, slug e quantidade de mesas.
    Verifica na tabela 'pedidos_mesas' quais mesas estão ativas ('ocupada') 
    e retorna o painel completo formatado em JSON.
    """
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        # Pega as configurações do estabelecimento
        cur.execute("SELECT nome_estabelecimento, slug, quantidade_mesas FROM administracao ORDER BY id DESC LIMIT 1;")
        config = cur.fetchone()
        
        if not config:
            cur.close()
            conn.close()
            return {"status": "erro", "mensagem": "Estabelecimento não configurado na tabela administracao."}

        slug = config["slug"]
        quantidade_mesas = config["quantidade_mesas"]

        # Busca os pedidos ativos salvos na tabela pedidos_mesas
        cur.execute("""
            SELECT id, mesa, dados_pedido, criado_em 
            FROM pedidos_mesas 
            WHERE slug = %s AND status = 'ocupada';
        """, (slug,))
        
        pedidos_ativos = {}
        for row in cur.fetchall():
            num_mesa = row["mesa"]
            pedidos_ativos[num_mesa] = {
                "id_pedido": row["id"],
                "dados_pedido": row["dados_pedido"],
                "criado_em": str(row["criado_em"])
            }
        
        cur.close()
        conn.close()

        # Monta o painel de todas as mesas do salão
        mesas_painel = []
        for num_mesa in range(1, quantidade_mesas + 1):
            if num_mesa in pedidos_ativos:
                # Mesa ocupada (vermelha)
                pedido_info = pedidos_ativos[num_mesa]
                # Extrai apenas os itens/extrato do pedido (sem valores/preços) conforme solicitado
                dados_brutos = pedido_info["dados_pedido"]
                extrato_itens = dados_brutos.get("itens", dados_brutos) # Se vier lista ou dicionário de itens

                mesas_painel.append({
                    "mesa": num_mesa,
                    "status": "ocupada",
                    "cor": "vermelha",
                    "id_pedido": pedido_info["id_pedido"],
                    "extrato_pedido": extrato_itens,
                    "criado_em": pedido_info["criado_em"],
                    "acoes": {
                        "clicar": "exibir_extrato",
                        "imprimir_comanda": "imprimir",
                        "liberar_mesa": "liberar"
                    }
                })
            else:
                # Mesa livre (verde)
                mesas_painel.append({
                    "mesa": num_mesa,
                    "status": "livre",
                    "cor": "verde",
                    "extrato_pedido": [],
                    "acoes": {
                        "clicar": "nenhuma"
                    }
                })

        return {
            "status": "sucesso",
            "nome_estabelecimento": config["nome_estabelecimento"],
            "slug": slug,
            "quantidade_mesas": quantidade_mesas,
            "mesas": mesas_painel
        }

    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao consultar painel de mesas: {str(e)}"}

def receber_pedido_cardapio(dados):
    """
    Salva integralmente o JSON do cardápio online na tabela 'pedidos_mesas'.
    Muda o status da mesa para 'ocupada' (vermelha).
    """
    slug = dados.get("slug")
    mesa = dados.get("mesa")
    
    if not slug or not mesa:
        return {"status": "erro", "mensagem": "Campos obrigatórios ausentes: 'slug' e 'mesa' são necessários."}

    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        # Salva todo o JSON recebido do cardápio online na tabela pedidos_mesas
        cur.execute("""
            INSERT INTO pedidos_mesas (slug, mesa, dados_pedido, status)
            VALUES (%s, %s, %s, 'ocupada')
            RETURNING id;
        """, (slug, mesa, json.dumps(dados)))

        novo_id = cur.fetchone()["id"]
        conn.commit()
        cur.close()
        conn.close()

        return {
            "status": "sucesso",
            "mensagem": f"Pedido da mesa {mesa} salvo com sucesso na tabela pedidos_mesas.",
            "id_pedido": novo_id
        }

    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao salvar pedido na tabela: {str(e)}"}

def liberar_mesa(dados):
    """
    Libera a mesa (desocupa), removendo ou atualizando o status na tabela pedidos_mesas,
    permitindo que outro cliente faça pedidos.
    """
    slug = dados.get("slug")
    mesa = dados.get("mesa")

    if not slug or not mesa:
        return {"status": "erro", "mensagem": "Slug e número da mesa são obrigatórios para liberar."}

    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Remove os pedidos ativos daquela mesa para deixá-la livre novamente
        cur.execute("""
            DELETE FROM pedidos_mesas 
            WHERE slug = %s AND mesa = %s AND status = 'ocupada';
        """, (slug, mesa))

        conn.commit()
        cur.close()
        conn.close()

        return {
            "status": "sucesso",
            "mensagem": f"Mesa {mesa} liberada com sucesso."
        }

    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao liberar mesa: {str(e)}"}

def processar_requisicao(json_requisicao):
    """Ponto de entrada do menu Pedidos que recebe e devolve estritamente JSON."""
    try:
        req = json.loads(json_requisicao) if isinstance(json_requisicao, str) else json_requisicao
        acao = req.get("acao")
        dados = req.get("dados", {})

        if acao == "consultar_painel":
            resposta = consultar_painel_mesas()
        elif acao == "novo_pedido":
            resposta = receber_pedido_cardapio(dados)
        elif acao == "liberar_mesa":
            resposta = liberar_mesa(dados)
        else:
            resposta = {"status": "erro", "mensagem": f"Ação '{acao}' não reconhecida no menu Pedidos."}

        return json.dumps(resposta, ensure_ascii=False)

    except Exception as e:
        return json.dumps({"status": "erro", "mensagem": f"Erro no processamento JSON do menu Pedidos: {str(e)}"}, ensure_ascii=False)
