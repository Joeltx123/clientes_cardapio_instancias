import os
import psycopg2
from psycopg2.extras import RealDictCursor

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "cardapio_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_PORT = os.getenv("DB_PORT", "5432")

def get_db():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT,
        cursor_factory=RealDictCursor
    )
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS configuracao (
            id SERIAL PRIMARY KEY,
            nome_restaurante VARCHAR(100) NOT NULL,
            quantidade_mesas INT NOT NULL
        );
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            descricao TEXT,
            preco NUMERIC(10,2) NOT NULL,
            categoria VARCHAR(50) NOT NULL,
            arquivado BOOLEAN DEFAULT FALSE
        );
    """)

    # Dropa a tabela de pedidos para garantir que recrie com a coluna forma_pagamento correta
    cursor.execute("DROP TABLE IF EXISTS pedidos CASCADE;")

    cursor.execute("""
        CREATE TABLE pedidos (
            id SERIAL PRIMARY KEY,
            mesa INT NOT NULL,
            itens TEXT NOT NULL,
            total NUMERIC(10,2) NOT NULL,
            forma_pagamento VARCHAR(30) DEFAULT 'Não informada',
            status VARCHAR(30) DEFAULT 'Pendente',
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    conn.commit()
    cursor.close()
    conn.close()
