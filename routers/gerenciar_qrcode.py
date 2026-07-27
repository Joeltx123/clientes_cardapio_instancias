from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import urllib.parse
from database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")
templates.env.cache = None

def get_total_mesas(db):
    try:
        cursor = db.cursor()
        cursor.execute("SELECT quantidade_mesas FROM configuracao LIMIT 1")
        res = cursor.fetchone()
        cursor.close()
        if res and res[0]:
            return int(res[0])
    except Exception:
        pass
    return 5

@router.get("/qrcodes", response_class=HTMLResponse)
def admin_qrcodes(request: Request, db = Depends(get_db)):
    total_mesas = get_total_mesas(db)
    host = request.url.hostname or "127.0.0.1"
    porta = request.url.port or 5002
    host_url = f"http://{host}:{porta}"

    mesas = []
    for i in range(1, total_mesas + 1):
        link_mesa = f"{host_url}/cardapio/{i}"
        encoded_url = urllib.parse.quote(link_mesa)
        qr_img = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={encoded_url}"

        mesas.append({
            "numero": i,
            "link": link_mesa,
            "qr": qr_img
        })

    return templates.TemplateResponse(request, "qrcodes.html", {
        "request": request,
        "mesas": mesas
    })
