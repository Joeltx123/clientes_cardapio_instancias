from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/qrcodes", response_class=HTMLResponse)
def gerar_qrcodes(request: Request):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT quantidade_mesas FROM configuracao LIMIT 1")
    config = cursor.fetchone()
    cursor.close()
    db.close()
    
    total_mesas = config['quantidade_mesas'] if config else 0
    
    # Pega o host atual da requisição para montar o link correto do QR code
    base_url = str(request.base_url).rstrip('/')
    
    mesas = []
    for i in range(1, total_mesas + 1):
        mesas.append({
            "numero": i,
            "url": f"{base_url}/mesa/{i}"
        })
        
    return templates.TemplateResponse(request, "qrcodes.html", {"mesas": mesas})
