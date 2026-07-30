from database import init_db, get_db

def testar_conexao():
    print("🔄 Testando a conexão e inicialização do banco de dados...")
    try:
        # Executa a função que cria as tabelas se não existirem
        init_db()
        print("✅ Sucesso: Tabelas ('configuracao', 'produtos', 'pedidos') verificadas ou criadas com êxito!")

        # Testa uma consulta rápida na conexão
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        versao = cursor.fetchone()
        print(f"✅ Sucesso: Conexão com o PostgreSQL estabelecida!")
        print(f"📊 Versão do Banco: {list(versao.values())[0] if isinstance(versao, dict) else versao}")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Erro ao conectar ou inicializar o banco: {e}")

if __name__ == "__main__":
    testar_conexao()
