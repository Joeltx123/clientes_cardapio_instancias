import json
import urllib.parse
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

def consultar_dados_qr():
    """
    Lê a tabela 'administracao' para obter o nome, o slug e a quantidade de mesas.
    Gera os links de acesso e as URLs das imagens de QR Code (via API pública de QR).
    Fornece também as instruções de redirecionamento e ações de interface.
    """
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT nome_estabelecimento, slug, quantidade_mesas FROM administracao ORDER BY id DESC LIMIT 1;")
        config = cur.fetchone()
        cur.close()
        conn.close()

        if not config:
            return {
                "status": "erro",
                "mensagem": "Nenhuma configuração encontrada. Configure o Menu Configuração primeiro."
            }

        nome_estabelecimento = config.get("nome_estabelecimento")
        slug = config.get("slug")
        quantidade_mesas = config.get("quantidade_mesas", 0)

        if not slug:
            return {
                "status": "erro",
                "mensagem": "O estabelecimento não possui um slug cadastrado."
            }

        # Link geral do estabelecimento
        link_geral = f"https://cardapiopro.com/{slug}"
        # URL da imagem do QR Code geral via API pública (ex: api.qrserver.com)
        qrcode_geral_img = f"https://api.qrserver.com/v1/create-qr-code/?size=250x250&data={urllib.parse.quote(link_geral)}"

        # Gera os dados individuais para cada mesa
        mesas_data = []
        for mesa_num in range(1, quantidade_mesas + 1):
            link_mesa = f"https://cardapiopro.com/{slug}/mesa/{mesa_num}"
            # URL da imagem do QR Code da mesa específica
            qrcode_mesa_img = f"https://api.qrserver.com/v1/create-qr-code/?size=250x250&data={urllib.parse.quote(link_mesa)}"
            
            mesas_data.append({
                "mesa": mesa_num,
                "link_acesso": link_mesa,
                "qrcode_imagem_url": qrcode_mesa_img,
                "acoes": {
                    "botao_abrir_link": "abrir_url",
                    "botao_imprimir": "imprimir_qrcode"
                }
            })

        resultado = {
            "status": "sucesso",
            "nome_estabelecimento": nome_estabelecimento,
            "slug_estabelecimento": slug,
            "quantidade_mesas": quantidade_mesas,
            "link_geral": link_geral,
            "qrcode_geral_imagem_url": qrcode_geral_img,
            "acoes_gerais": {
                "mudar_quantidade_mesas": {
                    "descricao": "Alterar a quantidade de mesas",
                    "redirecionar_para": "menu_configuracao"
                },
                "botao_imprimir_todos": "imprimir_todos_qrcodes"
            },
            "mesas": mesas_data
        }

        return {"status": "sucesso", "dados": resultado}

    except Exception as e:
        return {
            "status": "erro",
            "mensagem": f"Erro ao gerar dados dos QR Codes: {str(e)}"
        }

def processar_requisicao(json_requisicao):
    """Ponto de entrada do menu QR Code que processa via JSON."""
    try:
        req = json.loads(json_requisicao) if isinstance(json_requisicao, str) else json_requisicao
        acao = req.get("acao")

        if acao in ["gerar", "consultar", "listar"]:
            resposta = consultar_dados_qr()
        else:
            resposta = {"status": "erro", "mensagem": f"Ação '{acao}' não reconhecida para o menu QR Code."}

        return json.dumps(resposta, ensure_ascii=False)

    except Exception as e:
        return json.dumps({"status": "erro", "mensagem": f"Erro no processamento JSON do QR Code: {str(e)}"}, ensure_ascii=False)
