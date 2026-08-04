import json
import os
import zipfile
import pyzipper
import pandas as pd
import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    "dbname": "cardapio_pro",
    "user": "postgres",
    "password": "",
    "host": "localhost",
    "port": "5432"
}

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)

def gerar_backup_sistema(dados):
    """
    Lê os dados da tabela 'transacoes' (ganhos por dia, mês e ano separados),
    gera uma planilha Excel organizada, compacta em um arquivo ZIP criptografado 
    com a senha 'Soulivre01' e salva no armazenamento interno do computador.
    Payload: {"slug": "nome-do-estabelecimento", "pasta_destino": "/caminho/para/downloads"}
    """
    slug = dados.get("slug")
    pasta_destino = dados.get("pasta_destino", os.path.expanduser("~/Downloads"))

    if not slug:
        return {"status": "erro", "mensagem": "O campo 'slug' é obrigatório para gerar o backup."}

    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        # Busca todas as transações do estabelecimento
        cur.execute("""
            SELECT id, tipo_pedido, referencia_id, nome_cliente, 
                   forma_pagamento, valor_total, criado_em 
            FROM transacoes 
            WHERE slug = %s 
            ORDER BY criado_em DESC;
        """, (slug,))
        
        transacoes = cur.fetchall()
        cur.close()
        conn.close()

        if not transacoes:
            return {"status": "erro", "mensagem": "Nenhuma transação encontrada para gerar o backup."}

        # Prepara os dados para o DataFrame do Pandas
        dados_planilha = []
        for t in transacoes:
            data_hora = t["criado_em"]
            dados_planilha.append({
                "ID": t["id"],
                "Tipo": t["tipo_pedido"],
                "Referencia/Mesa": t["referencia_id"],
                "Cliente": t["nome_cliente"],
                "Pagamento": t["forma_pagamento"],
                "Valor (R$)": float(t["valor_total"] or 0.0),
                "Data/Hora": str(data_hora),
                "Dia": data_hora.strftime("%Y-%m-%d"),
                "Mês": data_hora.strftime("%Y-%m"),
                "Ano": data_hora.strftime("%Y")
            })

        df = pd.DataFrame(dados_planilha)

        # Caminhos dos arquivos temporários e finais
        os.makedirs(pasta_destino, exist_ok=True)
        excel_path = os.path.join(pasta_destino, f"backup_financeiro_{slug}.xlsx")
        zip_path = os.path.join(pasta_destino, f"backup_seguro_{slug}.zip")

        # Salva em planilha organizada por dia, mês e ano
        with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name="Geral Transacoes", index=False)
            
            # Agrupamentos separados para melhor organização
            if not df.empty:
                por_dia = df.groupby("Dia")["Valor (R$)"].sum().reset_index()
                por_dia.to_excel(writer, sheet_name="Ganhos por Dia", index=False)

                por_mes = df.groupby("Mês")["Valor (R$)"].sum().reset_index()
                por_mes.to_excel(writer, sheet_name="Ganhos por Mês", index=False)

                por_ano = df.groupby("Ano")["Valor (R$)"].sum().reset_index()
                por_ano.to_excel(writer, sheet_name="Ganhos por Ano", index=False)

        # Compacta e criptografa o arquivo ZIP com a senha exigida: Soulivre01
        senha_zip = b"Soulivre01"
        
        with pyzipper.AESZipFile(zip_path, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
            zipf.setpassword(senha_zip)
            zipf.write(excel_path, arcname=os.path.basename(excel_path))

        # Remove o arquivo Excel avulso, mantendo apenas o ZIP criptografado seguro
        if os.path.exists(excel_path):
            os.remove(excel_path)

        return {
            "status": "sucesso",
            "mensagem": "Backup gerado, compactado e criptografado com sucesso.",
            "arquivo_zip": zip_path,
            "senha_utilizada": "Soulivre01",
            "armazenamento": "interno_computador"
        }

    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao gerar backup criptografado: {str(e)}"}

def processar_requisicao(json_requisicao):
    """Ponto de entrada do menu Backup que recebe e devolve estritamente JSON."""
    try:
        req = json.loads(json_requisicao) if isinstance(json_requisicao, str) else json_requisicao
        acao = req.get("acao")
        dados = req.get("dados", {})

        if acao in ["gerar_backup", "baixar_backup"]:
            resposta = gerar_backup_sistema(dados)
        else:
            resposta = {"status": "erro", "mensagem": f"Ação '{acao}' não reconhecida no menu Backup."}

        return json.dumps(resposta, ensure_ascii=False)

    except Exception as e:
        return json.dumps({"status": "erro", "mensagem": f"Erro no processamento JSON do menu Backup: {str(e)}"}, ensure_ascii=False)
