from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/qrcode")
def ver_qrcode(request: Request):
    dados_qrcode = {} # Substitua pela sua lógica/banco
    return templates.TemplateResponse("qrcode.html", {
        "request": request, 
        "qrcode": dados_qrcode
    })
