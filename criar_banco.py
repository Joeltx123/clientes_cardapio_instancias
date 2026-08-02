import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

load_dotenv()
db_url = os.getenv("DATABASE_URL")

if not db_url:
    print("Erro: DATABASE_URL não encontrada no arquivo .env")
    exit(1)

# Extrai o nome do banco e a URL base (conectando ao banco 'postgres' padrão primeiro para criar o cardapio_db se precisar)
# Exemplo de URL: postgresql://usuario:senha@localhost:5432/cardapio_db
base_url = db_url.rsplit('/', 1)[0]
db_name = db_url.rsplit('/', 1)[1]

print(f"Verificando / Criando o banco de dados '{db_name}'...")

try:
    # Conecta no banco padrão 'postgres' para garantir a criação do cardapio_db
    conn_padrao = psycopg2.connect(f"{base_url}/postgres")
    conn_padrao.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor_padrao = conn_padrao.cursor()
    
    cursor_padrao.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}';")
    exists = cursor_padrao.fetchone()
    
    if not exists:
        cursor_padrao.execute(f"CREATE DATABASE {db_name};")
        print(f"Banco de dados '{db_name}' criado com sucesso!")
    else:
        print(f"Banco de dados '{db_name}' já existe.")
        
    cursor_padrao.close()
    conn_padrao.close()
except Exception as e:
    print(f"Aviso ao verificar/criar o banco (pode ignorar se já estiver conectado): {e}")

print("Conectando ao banco de dados e criando as tabelas...")

# Conecta no banco definitivo para criar as tabelas
conn = psycopg2.connect(db_url)
conn.autocommit = True
cursor = conn.cursor()

# Comando para criar todas as tabelas do sistema
cursor.execute("""
CREATE TABLE IF NOT EXISTS estabelecimentos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150),
    ativo BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS configuracao (
    id SERIAL PRIMARY KEY,
    dados_json TEXT
);

CREATE TABLE IF NOT EXISTS produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    preco NUMERIC(10, 2) NOT NULL,
    descricao TEXT,
    categoria VARCHAR(100),
    disponivel BOOLEAN DEFAULT TRUE,
    dados_json TEXT
);

CREATE TABLE IF NOT EXISTS pedidos (
    id SERIAL PRIMARY KEY,
    cliente VARCHAR(150),
    status VARCHAR(50) DEFAULT 'pendente',
    total NUMERIC(10, 2),
    itens_json TEXT,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS pedidos_delivery (
    id SERIAL PRIMARY KEY,
    cliente VARCHAR(150),
    endereco TEXT,
    status VARCHAR(50) DEFAULT 'pendente',
    total NUMERIC(10, 2),
    itens_json TEXT,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS registros_caixa (
    id SERIAL PRIMARY KEY,
    tipo VARCHAR(50),
    valor NUMERIC(10, 2),
    descricao TEXT,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

print("Todas as tabelas foram criadas com sucesso no PostgreSQL!")
cursor.close()
conn.close()
