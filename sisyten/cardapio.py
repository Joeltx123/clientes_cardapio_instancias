import pandas as pd
from sisyten import json_core

def listar_cardapio(caminho_arquivo="dados/cardapio.json"):
    """Lê e processa os itens do cardápio usando pandas e json_core."""
    dados_brutos = json_core.ler_json_seguro(caminho_arquivo, [])
    df = json_core.json_para_dataframe(dados_brutos)
    
    if df.empty:
        return []
    
    return df.to_dict(orient="records")

def salvar_cardapio(itens, caminho_arquivo="dados/cardapio.json"):
    """Salva os itens do cardápio de forma segura."""
    df = pd.DataFrame(itens)
    json_str = json_core.dataframe_para_json(df)
    dados = json_core.json_para_dataframe(json_str).to_dict(orient="records")
    return json_core.salvar_json_seguro(caminho_arquivo, dados)
