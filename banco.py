import os
import psycopg2
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env da instância
load_dotenv()

def conectar():
    try:
        database_url = os.getenv("DATABASE_URL")

        if database_url:
            # Conecta usando a URL completa do .env (gerada pelo script de cadastro)
            return psycopg2.connect(database_url)
        else:
            # Fallback padrão caso não haja DATABASE_URL definida
            return psycopg2.connect(
                dbname=os.getenv("DB_NAME", "cardapio_pro_db"),
                user=os.getenv("DB_USER", "postgres"),
                password=os.getenv("DB_PASSWORD", ""),
                host=os.getenv("DB_HOST", "127.0.0.1"),
                port=os.getenv("DB_PORT", "5432")
            )
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise e


