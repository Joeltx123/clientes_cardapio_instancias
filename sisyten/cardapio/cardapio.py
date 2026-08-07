import os
import shutil
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

def salvar_arquivo_local(foto_arquivo):
    if foto_arquivo and foto_arquivo.filename:
        upload_dir = os.path.join("static", "uploads")
        os.makedirs(upload_dir, exist_ok=True)
        
        # Garante um nome de arquivo seguro/único
        filename = foto_arquivo.filename.replace(" ", "_")
        filepath = os.path.join(upload_dir, filename)
        
        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(foto_arquivo.file, buffer)
        
        return f"/static/uploads/{filename}"
    return ""

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

def salvar_produto(nome, preco, categoria, descricao, foto_url="", foto_arquivo=None):
    caminho_foto = foto_url
    if foto_arquivo and foto_arquivo.filename:
        caminho_foto = salvar_arquivo_local(foto_arquivo)

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO cardapio (nome, preco, categoria, descricao, foto_url, visivel, arquivado) VALUES (%s, %s, %s, %s, %s, true, false);", (nome, preco, categoria, descricao, caminho_foto))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def atualizar_foto_produto(produto_id, foto_arquivo=None, remover=False):
    caminho_foto = ""
    if not remover and foto_arquivo and foto_arquivo.filename:
        caminho_foto = salvar_arquivo_local(foto_arquivo)

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        if remover:
            cursor.execute("UPDATE cardapio SET foto_url = '' WHERE id = %s;", (produto_id,))
        elif caminho_foto:
            cursor.execute("UPDATE cardapio SET foto_url = %s WHERE id = %s;", (caminho_foto, produto_id))
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
