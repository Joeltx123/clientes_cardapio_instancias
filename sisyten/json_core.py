import json
import io
import pandas as pd
from datetime import datetime

def _log(acao, origem, detalhes=""):
    hora = datetime.now().strftime("%H:%M:%S")
    print(f"[{hora}] [JSON_CORE] [{acao.upper()}] -> {origem} {detalhes}")

def ler_json_seguro(caminho_arquivo, valor_padrao=None):
    if valor_padrao is None:
        valor_padrao = {}
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
            _log("RECEBENDO (Lendo)", caminho_arquivo, f"({len(str(dados))} caracteres)")
            return dados
    except (FileNotFoundError, json.JSONDecodeError):
        _log("AVISO", caminho_arquivo, "Arquivo não encontrado ou vazio. Usando valor padrão.")
        return valor_padrao

def salvar_json_seguro(caminho_arquivo, dados):
    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
            _log("ENVIANDO (Salvando)", caminho_arquivo, f"({len(str(dados))} caracteres)")
        return True
    except Exception as e:
        _log("ERRO", caminho_arquivo, f"Falha ao salvar: {e}")
        return False

def dataframe_para_json(df):
    _log("PROCESSANDO", "DataFrame -> JSON", f"({len(df)} linhas)")
    return df.to_json(orient="records", force_ascii=False)

def json_para_dataframe(json_str):
    _log("PROCESSANDO", "JSON -> DataFrame", "")
    if isinstance(json_str, str):
        return pd.read_json(io.StringIO(json_str), orient="records")
    elif isinstance(json_str, list):
        return pd.DataFrame(json_str)
    return pd.DataFrame()
