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

def cadastrar_produto(dados):
    """
    Cadastra um produto separado por categoria, com descrição, preço, foto (URL ou local)
    e visibilidade inicial padrão (visível).
    Payload: {
      "slug": "...", 
      "categoria": "Porções", 
      "nome": "Batata Frita", 
      "descricao": "Porção grande com cheddar e bacon", 
      "preco": 35.00,
      "foto_url": "https://exemplo.com/foto.jpg"
    }
    """
    slug = dados.get("slug")
    categoria = dados.get("categoria")
    nome = dados.get("nome")
    descricao = dados.get("descricao", "")
    preco = dados.get("preco")
    foto_url = dados.get("foto_url", "")

    if not slug or not categoria or not nome or preco is None:
        return {
            "status": "erro",
            "mensagem": "Campos obrigatórios ausentes: 'slug', 'categoria', 'nome' e 'preco' são necessários."
        }

    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute("""
            INSERT INTO cardapio (slug, categoria, nome, descricao, preco, visivel, arquivado, foto_url)
            VALUES (%s, %s, %s, %s, %s, TRUE, FALSE, %s)
            RETURNING id, slug, categoria, nome, descricao, preco, visivel, arquivado, foto_url;
        """, (slug, categoria, nome, descricao, preco, foto_url))

        novo_produto = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        novo_produto["preco"] = float(novo_produto["preco"])
        return {
            "status": "sucesso",
            "mensagem": "Produto cadastrado com sucesso.",
            "produto": novo_produto
        }

    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao cadastrar produto: {str(e)}"}

def consultar_cardapio(dados):
    """
    Lista os produtos ativos (não arquivados) separados por categoria e visibilidade.
    Payload: {"slug": "..."}
    """
    slug = dados.get("slug")
    if not slug:
        return {"status": "erro", "mensagem": "O campo 'slug' é obrigatório."}

    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute("""
            SELECT id, categoria, nome, descricao, preco, visivel, arquivado, foto_url, atualizado_em 
            FROM cardapio 
            WHERE slug = %s AND arquivado = FALSE
            ORDER BY categoria, nome;
        """, (slug,))

        produtos = cur.fetchall()
        cur.close()
        conn.close()

        for p in produtos:
            p["preco"] = float(p["preco"])
            p["atualizado_em"] = str(p["atualizado_em"])

        return {
            "status": "sucesso",
            "slug": slug,
            "total_produtos": len(produtos),
            "produtos": produtos
        }

    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao consultar cardápio: {str(e)}"}

def listar_arquivados(dados):
    """
    Lista os produtos que estão na aba de Arquivados.
    Payload: {"slug": "..."}
    """
    slug = dados.get("slug")
    if not slug:
        return {"status": "erro", "mensagem": "O campo 'slug' é obrigatório."}

    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute("""
            SELECT id, categoria, nome, descricao, preco, visivel, arquivado, foto_url, atualizado_em 
            FROM cardapio 
            WHERE slug = %s AND arquivado = TRUE
            ORDER BY categoria, nome;
        """, (slug,))

        produtos = cur.fetchall()
        cur.close()
        conn.close()

        for p in produtos:
            p["preco"] = float(p["preco"])
            p["atualizado_em"] = str(p["atualizado_em"])

        return {
            "status": "sucesso",
            "slug": slug,
            "produtos_arquivados": produtos
        }

    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao listar arquivados: {str(e)}"}

def alterar_visibilidade(dados):
    """
    Alterna se o produto fica visível ou oculto no cardápio online digital.
    Payload: {"id": 1, "visivel": false}
    """
    produto_id = dados.get("id")
    visivel = dados.get("visivel")

    if produto_id is None or visivel is None:
        return {"status": "erro", "mensagem": "Os campos 'id' e 'visivel' (true/false) são obrigatórios."}

    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute("""
            UPDATE cardapio
            SET visivel = %s, atualizado_em = CURRENT_TIMESTAMP
            WHERE id = %s
            RETURNING id, nome, visivel;
        """, (visivel, produto_id))

        prod = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        if not prod:
            return {"status": "erro", "mensagem": "Produto não encontrado."}

        estado = "visível" if prod["visivel"] else "oculto"
        return {"status": "sucesso", "mensagem": f"Produto '{prod['nome']}' agora está {estado} no cardápio digital."}

    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao alterar visibilidade: {str(e)}"}

def arquivar_ou_desarquivar(dados):
    """
    Move o produto para a aba de arquivados ou tira de lá (desarquiva).
    Payload: {"id": 1, "arquivado": true}
    """
    produto_id = dados.get("id")
    arquivado = dados.get("arquivado")

    if produto_id is None or arquivado is None:
        return {"status": "erro", "mensagem": "Os campos 'id' e 'arquivado' (true/false) são obrigatórios."}

    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute("""
            UPDATE cardapio
            SET arquivado = %s, atualizado_em = CURRENT_TIMESTAMP
            WHERE id = %s
            RETURNING id, nome, arquivado;
        """, (arquivado, produto_id))

        prod = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        if not prod:
            return {"status": "erro", "mensagem": "Produto não encontrado."}

        acao_str = "arquivado" if prod["arquivado"] else "desarquivado"
        return {"status": "sucesso", "mensagem": f"Produto '{prod['nome']}' foi {acao_str} com sucesso."}

    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao alterar status de arquivo: {str(e)}"}

def excluir_produto_definitivamente(dados):
    """
    Exclui o cadastro do produto do banco de dados (geralmente usado dentro da aba arquivados).
    Como os pedidos salvos guardam o JSON completo dos itens, a exclusão do cardápio não interfere neles.
    Payload: {"id": 1}
    """
    produto_id = dados.get("id")
    if not produto_id:
        return {"status": "erro", "mensagem": "O 'id' do produto é obrigatório para exclusão definitiva."}

    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("DELETE FROM cardapio WHERE id = %s RETURNING id;", (produto_id,))
        removido = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        if not removido:
            return {"status": "erro", "mensagem": "Produto não encontrado."}

        return {"status": "sucesso", "mensagem": f"Cadastro do produto ID {produto_id} excluído permanentemente."}

    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao excluir produto: {str(e)}"}

def processar_requisicao(json_requisicao):
    """Ponto de entrada do menu Cardápio que recebe e devolve estritamente JSON."""
    try:
        req = json.loads(json_requisicao) if isinstance(json_requisicao, str) else json_requisicao
        acao = req.get("acao")
        dados = req.get("dados", {})

        if acao == "cadastrar":
            resposta = cadastrar_produto(dados)
        elif acao == "consultar":
            resposta = consultar_cardapio(dados)
        elif acao == "listar_arquivados":
            resposta = listar_arquivados(dados)
        elif acao == "visibilidade":
            resposta = alterar_visibilidade(dados)
        elif acao == "arquivar":
            resposta = arquivar_ou_desarquivar(dados)
        elif acao == "excluir":
            resposta = excluir_produto_definitivamente(dados)
        else:
            resposta = {"status": "erro", "mensagem": f"Ação '{acao}' não reconhecida no menu Cardápio."}

        return json.dumps(resposta, ensure_ascii=False)

    except Exception as e:
        return json.dumps({"status": "erro", "mensagem": f"Erro no processamento JSON do menu Cardápio: {str(e)}"}, ensure_ascii=False)
