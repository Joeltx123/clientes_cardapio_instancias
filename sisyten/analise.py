import pandas as pd
from sisyten import json_core
from datetime import datetime

def gerar_relatorio_vendas(caminho_vendas="dados/vendas.json", filtro_periodo="todos"):
    """Gera análises estatísticas de vendas utilizando pandas com suporte a filtros."""
    vendas = json_core.ler_json_seguro(caminho_vendas, [])
    df = json_core.json_para_dataframe(vendas)
    
    if df.empty or "valor" not in df.columns:
        return {
            "total_vendas": 0, "faturamento_total": 0.0, "ticket_medio": 0.0,
            "pix": 0.0, "cartao": 0.0, "dinheiro": 0.0, "transacoes": []
        }

    # Converte coluna de data se existir
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

    # Totais por forma de pagamento se a coluna existir
    pix = float(df[df["forma"].str.lower() == "pix"]["valor"].sum()) if "forma" in df.columns and not df.empty else 0.0
    cartao = float(df[df["forma"].str.lower().str.contains("cartao|cartão", na=False)]["valor"].sum()) if "forma" in df.columns and not df.empty else 0.0
    dinheiro = float(df[df["forma"].str.lower() == "dinheiro"]["valor"].sum()) if "forma" in df.columns and not df.empty else 0.0

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
