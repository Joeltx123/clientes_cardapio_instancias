import json
import io
import pandas as pd

def ler_json_seguro(caminho_arquivo, valor_padrao=None):
    if valor_padrao is None:
        valor_padrao = {}
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return valor_padrao

def salvar_json_seguro(caminho_arquivo, dados):
    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"Erro ao salvar JSON em {caminho_arquivo}: {e}")
        return False

def dataframe_para_json(df):
    return df.to_json(orient="records", force_ascii=False)

def json_para_dataframe(json_str):
    if isinstance(json_str, str):
        return pd.read_json(io.StringIO(json_str), orient="records")
    elif isinstance(json_str, list):
        return pd.DataFrame(json_str)
    return pd.DataFrame()
