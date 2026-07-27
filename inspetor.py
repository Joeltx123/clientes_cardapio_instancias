import traceback
import sys
import os
import platform
import httpx
from banco import conectar

CENTRAL_URL = os.getenv("CENTRAL_URL", "http://localhost:8000")
CLIENTE_ID = os.getenv("CLIENTE_ID", "matriz")

class InspetorSistema:
    @staticmethod
    def diagnosticar_ambiente():
        status_banco = "Desconectado"
        try:
            conn = conectar()
            cur = conn.cursor()
            cur.execute("SELECT 1;")
            cur.close()
            conn.close()
            status_banco = "Online e Saudável"
        except Exception as e:
            status_banco = f"Erro no Banco: {str(e)}"

        return {
            "sistema_operacional": platform.system(),
            "versao_python": sys.version.split()[0],
            "banco_dados": status_banco,
            "ambiente_termux": "com.termux" in os.getenv("PREFIX", "")
        }

def capturar_erro(e):
    """Captura a exceção atual, formata no padrão esperado pela Central e envia."""
    try:
        exc_type, exc_value, exc_tb = sys.exc_info()

        # Pega o nome do módulo ou arquivo principal onde ocorreu o erro
        tb_list = traceback.extract_tb(exc_tb)
        modulo_origem = os.path.basename(tb_list[-1].filename) if tb_list else "main.py"

        # Formata o erro como string conforme exigido pela Central
        mensagem_erro = f"{exc_type.__name__ if exc_type else 'Exception'}: {str(exc_value)}"

        payload = {
            "cliente_id": CLIENTE_ID,
            "erro": mensagem_erro,
            "modulo": modulo_origem,
            "ambiente": InspetorSistema.diagnosticar_ambiente()
        }

        url = f"{CENTRAL_URL}/suporte/{CLIENTE_ID}/reportar"
        httpx.post(url, json=payload, timeout=2.0)
    except Exception:
        pass

