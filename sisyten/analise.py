import os
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
import pandas as pd

def get_db_connection():
    return psycopg2.connect(
        dbname="cardapio_pro",
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", ""),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432")
    )

def obter_dados(filtro_periodo="todos"):
    """Consulta as transações no PostgreSQL e gera o relatório estatístico."""
    conn = get_db_connection()
    try:
        query = "SELECT id, valor_total as valor, forma_pagamento as forma, criado_em as data, nome_cliente as cliente FROM transacoes;"
        df = pd.read_sql(query, conn)
    except Exception as e:
        print(f"Erro ao consultar transações: {e}")
        df = pd.DataFrame()
    finally:
        conn.close()

    if df.empty or "valor" not in df.columns:
        return {
            "total_vendas": 0, "faturamento_total": 0.0, "ticket_medio": 0.0,
            "pix": 0.0, "cartao": 0.0, "dinheiro": 0.0, "transacoes": []
        }

    if "data" in df.columns:
        df["data_dt"] = pd.to_datetime(df["data"], errors="coerce")
        hoje = datetime.now().date()

        if filtro_periodo == "hoje":
            df = df[df["data_dt"].dt.date == hoje]
        elif filtro_periodo == "semana":
            inicio_semana = hoje - pd.Timedelta(days=7)
            df = df[df["data_dt"].dt.date >= inicio_semana]
        elif filtro_periodo == "mes":
            df = df[(df["data_dt"].dt.month == hoje.month) & (df["data_dt"].dt.year == hoje.year)]

    total_vendas = len(df)
    faturamento_total = float(df["valor"].sum()) if not df.empty else 0.0
    ticket_medio = faturamento_total / total_vendas if total_vendas > 0 else 0.0

    forma_serie = df["forma"].astype(str).str.lower() if "forma" in df.columns else pd.Series()
    pix = float(df[forma_serie == "pix"]["valor"].sum()) if not df.empty else 0.0
    cartao = float(df[forma_serie.str.contains("cartao|cartão", na=False)]["valor"].sum()) if not df.empty else 0.0
    dinheiro = float(df[forma_serie == "dinheiro"]["valor"].sum()) if not df.empty else 0.0

    analise = {
        "total_vendas": total_vendas,
        "faturamento_total": round(faturamento_total, 2),
        "ticket_medio": round(ticket_medio, 2),
        "pix": round(pix, 2),
        "cartao": round(cartao, 2),
        "dinheiro": round(dinheiro, 2),
        "transacoes": df.to_dict(orient="records") if not df.empty else []
    }

    return analise
