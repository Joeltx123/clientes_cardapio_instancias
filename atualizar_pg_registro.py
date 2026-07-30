# Este código demonstra a estrutura correta para o seu backend PostgreSQL (Flask)

"""
1. COMANDO SQL PARA CRIAR A TABELA NO POSTGRESQL:
--------------------------------------------------
CREATE TABLE IF NOT EXISTS registros_caixa (
    id SERIAL PRIMARY KEY,
    tenant VARCHAR(100) NOT NULL,
    mesa INT NOT NULL,
    forma_pagamento VARCHAR(150) NOT NULL,
    total NUMERIC(10, 2) NOT NULL,
    troco NUMERIC(10, 2) DEFAULT 0.00,
    horario TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

import psycopg2
from flask import request, jsonify

# Exemplo de como deve ser a sua rota POST que processa o pagamento e salva no Postgres:
# @app.route('/admin/<tenant>/api/processar-pagamento', methods=['POST'])
def processar_pagamento_pg(tenant):
    dados = request.get_json()
    mesa = dados.get('mesa')
    total = dados.get('total')
    forma_pagamento = dados.get('forma_pagamento') # Ex: "Cartão de Crédito (3x)" ou "Dinheiro"
    troco = dados.get('troco', 0.00) # Valor do troco enviado pelo front-end

    # Conexão com o seu banco PostgreSQL (ajuste suas variáveis de ambiente/conexão)
    # conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    # cursor = conn.cursor()

    try:
        # Exemplo de inserção no PostgreSQL:
        # cursor.execute('''
        #     INSERT INTO registros_caixa (tenant, mesa, forma_pagamento, total, troco, horario)
        #     VALUES (%s, %s, %s, %s, %s, NOW())
        # ''', (tenant, mesa, forma_pagamento, total, troco))
        # conn.commit()
        
        # Aqui também entram os comandos para limpar os itens ativos da mesa...
        
        return jsonify({"sucesso": True, "mensagem": f"Mesa {mesa} fechada com sucesso!"})
    except Exception as e:
        # conn.rollback()
        return jsonify({"erro": str(e)}), 500
    finally:
        # cursor.close()
        # conn.close()
        pass


# Rota GET consumida pelo Menu Registro no PostgreSQL:
# @app.route('/admin/<tenant>/api/registros-caixa', methods=['GET'])
def api_registros_caixa_pg(tenant):
    # conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    # cursor = conn.cursor()
    
    # cursor.execute('''
    #     SELECT TO_CHAR(horario, 'DD/MM/YYYY HH24:MI') as data_fmt, mesa, forma_pagamento, total, troco 
    #     FROM registros_caixa 
    #     WHERE tenant = %s 
    #     ORDER BY id DESC
    # ''', (tenant,))
    
    # linhas = cursor.fetchall()
    # cursor.close()
    # conn.close()
    
    registros = []
    # Para cada linha do banco, montamos o JSON:
    # for linha in linhas:
    #     registros.append({
    #         "horario": linha[0],
    #         "mesa": linha[1],
    #         "forma_pagamento": linha[2],
    #         "total": float(linha[3]),
    #         "troco": float(linha[4]) if linha[4] else 0.00
    #     })
        
    return jsonify({"registros": registros})

print("Template PostgreSQL para registro configurado!")
