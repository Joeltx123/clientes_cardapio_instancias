import psycopg2

def configurar_banco():
    try:
        conn = psycopg2.connect(dbname="cardapio_pro", user="postgres")
        cur = conn.cursor()

        # Tabela de Administração
        cur.execute("""
            CREATE TABLE IF NOT EXISTS administracao (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100),
                mesas INT DEFAULT 5
            );
        """)

        # Tabela de Cardápio
        cur.execute("""
            CREATE TABLE IF NOT EXISTS cardapio (
                id SERIAL PRIMARY KEY,
                nome_item VARCHAR(100),
                preco NUMERIC(10, 2),
                categoria VARCHAR(50)
            );
        """)

        # Tabela de Transações
        cur.execute("""
            CREATE TABLE IF NOT EXISTS transacoes (
                id SERIAL PRIMARY KEY,
                mesa INT,
                detalhes TEXT,
                status VARCHAR(50),
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        conn.commit()
        cur.close()
        conn.close()
        print("✅ Banco de dados configurado e tabelas criadas com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao configurar o banco de dados: {e}")

if __name__ == "__main__":
    configurar_banco()
