import socket
import json
import os

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def save_ip_to_json(filename="server_ip.json"):
    ip = get_local_ip()
    data = {
        "ip": ip,
        "url_local": f"http://{ip}:8000"
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"[IP Capturado] IP da rede: {ip} | Salvo em {filename}")
    return data

if __name__ == "__main__":
    save_ip_to_json()
