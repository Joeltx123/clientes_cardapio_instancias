import os
import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    return psycopg2.connect(
        dbname="cardapio_pro",
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", ""),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432")
    )

def listar_cardapio(apenas_ativos=False):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        if apenas_ativos:
            cursor.execute("SELECT id, categoria, nome, descricao, preco, visivel, arquivado, foto_url FROM cardapio WHERE arquivado = false AND visivel = true ORDER BY categoria, nome;")
        else:
            cursor.execute("SELECT id, categoria, nome, descricao, preco, visivel, arquivado, foto_url FROM cardapio WHERE arquivado = false ORDER BY categoria, nome;")
        return [dict(row) for row in cursor.fetchall()]
    finally:
        cursor.close()
        conn.close()

def listar_arquivados():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT id, categoria, nome, descricao, preco, visivel, arquivado, foto_url FROM cardapio WHERE arquivado = true ORDER BY categoria, nome;")
        return [dict(row) for row in cursor.fetchall()]
    finally:
        cursor.close()
        conn.close()

def salvar_produto(nome, preco, categoria, descricao, foto_url=""):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO cardapio (nome, preco, categoria, descricao, foto_url, visivel, arquivado) VALUES (%s, %s, %s, %s, %s, true, false);", (nome, preco, categoria, descricao, foto_url))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def alterar_visibilidade(produto_id, visivel):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE cardapio SET visivel = %s WHERE id = %s;", (visivel, produto_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def arquivar_produto(produto_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE cardapio SET arquivado = true WHERE id = %s;", (produto_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def desarquivar_produto(produto_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE cardapio SET arquivado = false WHERE id = %s;", (produto_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def excluir_produto(produto_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM cardapio WHERE id = %s;", (produto_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()
