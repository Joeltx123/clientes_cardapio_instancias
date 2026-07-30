# Exemplo de como a rota de processar pagamento deve estar estruturada no seu FastAPI:

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import psycopg2
import os

router = APIRouter()

class PagamentoModel(BaseModel):
    mesa: int
    total: float
    forma_pagamento: str
    troco: float = 0.00

# Exemplo da rota POST que o front-end chama ao fechar a comanda:
# @router.post("/admin/{tenant}/api/processar-pagamento")
def processar_pagamento_fastapi(tenant: str, dados: PagamentoModel):
    try:
        # Conexão com o banco cardapio_db
        # Substitua pelas suas credenciais de conexão do PostgreSQL
        conn = psycopg2.connect(database="cardapio_db", user="postgres")
        cursor = conn.cursor()

        # Inserção exata na tabela registros_caixa
        cursor.execute("""
            INSERT INTO registros_caixa (tenant, mesa, forma_pagamento, total, troco, horario)
            VALUES (%s, %s, %s, %s, %s, NOW())
        """, (tenant, dados.mesa, dados.forma_pagamento, dados.total, dados.troco))

        conn.commit()
        cursor.close()
        conn.close()

        return {"sucesso": True, "mensagem": f"Mesa {dados.mesa} salva com sucesso no registro!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

print("Estrutura de salvamento para o FastAPI pronta para conferência.")
