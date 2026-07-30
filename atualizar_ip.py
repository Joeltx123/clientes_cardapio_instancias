import socket
import json
import os

def obter_ip_local():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Não precisa alcançar a internet de verdade, apenas descobre a interface de rede ativa
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def salvar_ip_json():
    ip_atual = obter_ip_local()
    dados = {"ip_servidor": ip_atual}
    
    caminho_arquivo = "servidor_config.json"
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)
    
    print(f"[IP Logger] IP atualizado com sucesso: {ip_atual} (salvo em {caminho_arquivo})")

if __name__ == "__main__":
    salvar_ip_json()
