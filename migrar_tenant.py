from database import get_db, init_db

def migrar():
    init_db()
    conn = get_db()
    cursor = conn.cursor()
    
    # Garante que as colunas de relacionamento existem nas tabelas antigas
    for tabela in ['produtos', 'pedidos']:
        cursor.execute(f"""
            DO $$ 
            BEGIN 
                IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name='{tabela}' and column_name='estabelecimento_id') THEN
                    ALTER TABLE {tabela} ADD COLUMN estabelecimento_id INT REFERENCES estabelecimentos(id) ON DELETE CASCADE;
                END IF;
            END $$;
        """)
    
    conn.commit()
    
    # Verifica se já existe um estabelecimento padrão
    cursor.execute("SELECT id FROM estabelecimentos WHERE slug = 'joel-burguer';")
    est = cursor.fetchone()
    
    if not est:
        print("Criando estabelecimento padrão: Joel Burger (slug: joel-burguer)...")
        cursor.execute(
            "INSERT INTO estabelecimentos (nome, slug, quantidade_mesas) VALUES (%s, %s, %s) RETURNING id;",
            ("Joel Burger", "joel-burguer", 10)
        )
        est_id = cursor.fetchone()['id']
        conn.commit()
    else:
        est_id = est['id']
        print(f"Estabelecimento padrão já existe com ID: {est_id}")
    
    # Atualiza registros antigos que estejam sem estabelecimento_id
    cursor.execute("UPDATE produtos SET estabelecimento_id = %s WHERE estabelecimento_id IS NULL;", (est_id,))
    cursor.execute("UPDATE pedidos SET estabelecimento_id = %s WHERE estabelecimento_id IS NULL;", (est_id,))
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Migração concluída com sucesso!")

if __name__ == "__main__":
    migrar()
