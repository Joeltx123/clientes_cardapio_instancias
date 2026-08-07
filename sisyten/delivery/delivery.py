import pandas as pd
from sisyten import json_core

def calcular_taxa_delivery(bairro_destino, caminho_bairros="dados/bairros.json"):
    """Calcula taxas de entrega cruzando dados com pandas."""
    bairros = json_core.ler_json_seguro(caminho_bairros, [])
    df = json_core.json_para_dataframe(bairros)
    
    if df.empty:
        return 0.00
    
    match = df[df["bairro"].str.lower() == bairro_destino.lower()]
    if not match.empty:
        return float(match.iloc[0].get("taxa", 0.00))
    
    return 0.00
