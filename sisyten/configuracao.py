import json
import re
import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    "dbname": "cardapio_pro",
    "user": "postgres",
    "password": "",
    "host": "localhost",
    "port": "5432"
}

ADMIN_SENHA_CORRETA = "Soulivre01"

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)

def gerar_slug(texto):
    """Gera um slug amigável a partir de uma string."""
    if not texto:
        return ""
    texto = texto.lower()
    import unicodedata
    nfkd = unicodedata.normalize('NFKD', texto)
    texto_sem_acento = "".join([c for c in nfkd if not unicodedata.combining(c)])
    slug = re.sub(r'[^a-z0-9]+', '-', texto_sem_acento)
    return slug.strip('-')

def consultar_configuracao():
    """Consulta as configurações atuais via JSON."""
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT id, nome_estabelecimento, slug, nome_dono, quantidade_mesas, atualizado_em FROM administracao ORDER BY id DESC LIMIT 1;")
        config = cur.fetchone()
        cur.close()
        conn.close()

        if config:
            config["atualizado_em"] = str(config["atualizado_em"])
            return {"status": "sucesso", "dados": config}
        else:
            return {"status": "sucesso", "dados": None, "mensagem": "Nenhuma configuração cadastrada ainda."}

    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao consultar o banco de dados: {str(e)}"}

def salvar_ou_atualizar_configuracao(dados):
    """Valida a senha do administrador e processa os dados para salvar/atualizar."""
    senha_informada = dados.get("senha_admin")

    if senha_informada != ADMIN_SENHA_CORRETA:
        return {
            "status": "erro",
            "mensagem": "Acesso negado: Senha do administrador incorreta ou não informada."
        }

    nome_estabelecimento = dados.get("nome_estabelecimento")
    nome_dono = dados.get("nome_dono")
    quantidade_mesas = dados.get("quantidade_mesas")
    
    slug_informado = dados.get("slug")
    if slug_informado:
        slug = gerar_slug(slug_informado)
    elif nome_estabelecimento:
        slug = gerar_slug(nome_estabelecimento)
    else:
        slug = None

    if quantidade_mesas is not None:
        try:
            quantidade_mesas = int(quantidade_mesas)
            if quantidade_mesas < 0:
                raise ValueError()
        except ValueError:
            return {
                "status": "erro",
                "mensagem": "A quantidade de mesas deve ser um número inteiro válido e não negativo."
            }

    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute("SELECT id FROM administracao ORDER BY id DESC LIMIT 1;")
        registro = cur.fetchone()

        if registro:
            id_registro = registro["id"]
            cur.execute("""
                UPDATE administracao
                SET nome_estabelecimento = COALESCE(%s, nome_estabelecimento),
                    slug = COALESCE(%s, slug),
                    nome_dono = COALESCE(%s, nome_dono),
                    quantidade_mesas = COALESCE(%s, quantidade_mesas),
                    atualizado_em = CURRENT_TIMESTAMP
                WHERE id = %s;
            """, (nome_estabelecimento, slug, nome_dono, quantidade_mesas, id_registro))
            conn.commit()
            mensagem = "Configurações atualizadas com sucesso."
        else:
            cur.execute("""
                INSERT INTO administracao (nome_estabelecimento, slug, nome_dono, quantidade_mesas)
                VALUES (%s, %s, %s, %s);
            """, (nome_estabelecimento, slug, nome_dono, quantidade_mesas or 0))
            conn.commit()
            mensagem = "Configurações cadastradas com sucesso."

        cur.close()
        conn.close()

        return {"status": "sucesso", "mensagem": mensagem, "slug": slug}

    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao salvar no banco de dados: {str(e)}"}

def processar_requisicao(json_requisicao):
    """Ponto de entrada que recebe e devolve estritamente JSON."""
    try:
        req = json.loads(json_requisicao) if isinstance(json_requisicao, str) else json_requisicao
        acao = req.get("acao")

        if acao == "consultar":
            resposta = consultar_configuracao()
        elif acao in ["cadastrar", "alterar", "salvar"]:
            dados = req.get("dados", {})
            resposta = salvar_ou_atualizar_configuracao(dados)
        else:
            resposta = {"status": "erro", "mensagem": f"Ação '{acao}' não reconhecida."}

        return json.dumps(resposta, ensure_ascii=False)

    except Exception as e:
        return json.dumps({"status": "erro", "mensagem": f"Erro no processamento JSON: {str(e)}"}, ensure_ascii=False)
