from passlib.hash import pbkdf2_sha256
from banco import conectar  # Mantendo a conexão padronizada do projeto

def registrar_usuario(username, password, restaurante_id):
    # O pbkdf2_sha256 é um padrão de segurança fortíssimo
    hash_password = pbkdf2_sha256.hash(password)

    # Conecta no banco
    conn = conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO usuarios (username, password_hash, restaurante_id) VALUES (%s, %s, %s)",
                (username, hash_password, restaurante_id))
    conn.commit()
    cur.close()
    conn.close()
    print(f"Usuário {username} registrado com segurança!")

def verificar_login(username, password_tentada):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT password_hash FROM usuarios WHERE username = %s", (username,))
    resultado = cur.fetchone()

    cur.close()
    conn.close()

    if resultado and pbkdf2_sha256.verify(password_tentada, resultado[0]):
        print("Login autorizado!")
        return True
    else:
        print("Login ou senha incorretos.")
        return False

