import os

# Lista de arquivos críticos que não podem ficar com 0 bytes
ARQUIVOS_CRITICOS = [
    "sisyten/json_core.py", 
    "sisyten/analise.py",
    "sisyten/cardapio.py",
    "sisyten/pedidos.py"
]

def verificar_integridade():
    print("[🔍] Verificando integridade dos arquivos do projeto...")
    for arquivo in ARQUIVOS_CRITICOS:
        if os.path.exists(arquivo):
            if os.path.getsize(arquivo) == 0:
                print(f"[❌ ALERTA CRÍTICO] O arquivo '{arquivo}' está VAZIO (0 bytes)!")
            else:
                print(f"[✔] '{arquivo}' está OK.")
        else:
            print(f"[⚠️ AVISO] Arquivo '{arquivo}' não foi encontrado.")

if __name__ == "__main__":
    verificar_integridade()
    print("\n[🚀] Sistema pronto para iniciar!")
