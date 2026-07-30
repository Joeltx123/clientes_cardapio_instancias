import os
import json
from urllib.parse import quote
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

def obter_ip_atual():
    if os.path.exists("servidor_config.json"):
        try:
            with open("servidor_config.json", "r") as f:
                data = json.load(f)
                return data.get("ip", "127.0.0.1")
        except Exception:
            pass
    return "127.0.0.1"

@router.get("/admin/{tenant}/qr-codes", response_class=HTMLResponse)
def gerar_qr_codes(request: Request, tenant: str):
    ip = obter_ip_atual()
    porta = "5003"
    
    qtd_mesas = 10
    try:
        from database import get_db
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT quantidade_mesas FROM configuracao LIMIT 1;")
        res = cursor.fetchone()
        if res:
            qtd_mesas = res[0] if isinstance(res, (list, tuple)) else res.get("quantidade_mesas", 10)
        cursor.close()
        conn.close()
    except Exception:
        pass

    mesas_qrs = []
    for mesa in range(1, int(qtd_mesas) + 1):
        link_cardapio = f"http://{ip}:{porta}/cardapio/{tenant}?mesa={mesa}&reset=1"
        
        # Gerando a URL diretamente pelo serviço do qrserver
        encoded_link = quote(link_cardapio, safe='')
        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={encoded_link}"
        
        mesas_qrs.append({
            "numero": mesa,
            "link": link_cardapio,
            "qr_code": qr_url
        })

    return templates.TemplateResponse(
        request,
        "qr_code.html",
        {
            "slug": tenant,
            "mesas": mesas_qrs
        }
    )
