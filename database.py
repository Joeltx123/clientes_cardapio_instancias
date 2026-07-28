import os
import psycopg2
from psycopg2.extras import RealDictCursor

DB_HOST = "localhost"
DB_NAME = "cardapio_db"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_PORT = "5432"

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
    
    # Tabela de Estabelecimentos (Tenants) com Slug único
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estabelecimentos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            slug VARCHAR(100) UNIQUE NOT NULL,
            quantidade_mesas INT NOT NULL DEFAULT 10,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # Tabela de Produtos vinculada ao estabelecimento
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id SERIAL PRIMARY KEY,
            estabelecimento_id INT REFERENCES estabelecimentos(id) ON DELETE CASCADE,
            nome VARCHAR(100) NOT NULL,
            descricao TEXT,
            preco NUMERIC(10,2) NOT NULL,
            categoria VARCHAR(50) NOT NULL,
            foto VARCHAR(255),
            visivel BOOLEAN DEFAULT TRUE,
            arquivado BOOLEAN DEFAULT FALSE
        );
    """)

    # Tabela de Pedidos vinculada ao estabelecimento
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
            id SERIAL PRIMARY KEY,
            estabelecimento_id INT REFERENCES estabelecimentos(id) ON DELETE CASCADE,
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
