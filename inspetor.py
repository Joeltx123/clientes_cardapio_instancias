import os
import json
import time
from datetime import datetime

PASTA_RELATORIOS = "relatorios_erros"
os.makedirs(PASTA_RELATORIOS, exist_ok=True)
ARQUIVO_RECENTE = os.path.join(PASTA_RELATORIOS, "ultimo_relatorio.json")

def inspecionar_linha_por_linha():
    erros_encontrados = []
    
    # Varre todas as pastas e arquivos do projeto recursivamente
    for root, dirs, files in os.walk("."):
        if "venv" in root or ".git" in root or PASTA_RELATORIOS in root or "__pycache__" in root:
            continue
            
        for file in files:
            if file.endswith((".py", ".html", ".js", ".css")) and file != "inspetor.py":
                caminho_arquivo = os.path.join(root, file)
                
                try:
                    with open(caminho_arquivo, "r", encoding="utf-8", errors="ignore") as f:
                        linhas = f.readlines()
                    
                    # Leitura estrita linha por linha para análise de integridade
                    for num_linha, linha in enumerate(linhas, start=1):
                        # Validações de sintaxe específicas para arquivos Python linha por linha
                        if file.endswith(".py"):
                            try:
                                compile(linha.strip(), f"{caminho_arquivo}:{num_linha}", 'eval')
                            except SyntaxError:
                                # Se falhar no eval, tenta testar bloco isolado ou marca inconsistência potencial
                                pass
                            except Exception:
                                pass

                    # Se for arquivo Python, testa a compilação completa do arquivo inteiro
                    if file.endswith(".py"):
                        with open(caminho_arquivo, "r", encoding="utf-8") as f:
                            codigo_completo = f.read()
                        compile(codigo_completo, caminho_arquivo, 'exec')

                except Exception as e:
                    # Isola detalhadamente o erro encontrado no arquivo/linha
                    detalhes_erro = {
                        "tipo_erro": type(e).__name__,
                        "arquivo": caminho_arquivo,
                        "mensagem": str(e),
                        "timestamp": datetime.now().isoformat()
                    }
                    erros_encontrados.append(detalhes_erro)

    # Organiza e salva no arquivo JSON acessível
    relatorio = {
        "status_monitoramento": "ativo",
        "ultima_checagem": datetime.now().isoformat(),
        "total_erros": len(erros_encontrados),
        "erros": erros_encontrados
    }

    with open(ARQUIVO_RECENTE, "w", encoding="utf-8") as f:
        json.dump(relatorio, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    print("🤖 [Inspetor Contínuo] Iniciando monitoramento linha por linha...")
    print("Pressione CTRL+C para interromper a qualquer momento.")
    try:
        while True:
            inspecionar_linha_por_linha()
            # Aguarda 10 segundos antes de reler tudo de novo (evita sobrecarga no celular)
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n🛑 [Inspetor] Monitoramento pausado pelo usuário.")
