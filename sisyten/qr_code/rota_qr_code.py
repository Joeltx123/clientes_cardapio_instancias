from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from sisyten.qr_code import qr_code

router = APIRouter()

@router.get("/qrcode", response_class=HTMLResponse)
def rota_qrcode_get(request: Request):
    # Chama a função de consulta do qr_code.py
    resultado = qr_code.consultar_qr_code()
    # O template espera receber um dicionário na chave "dados"
    return request.app.state.templates.TemplateResponse(
        request, 
        "qrcode.html", 
        {
            "request": request, 
            "dados": resultado.get("dados", {})
        }
    )
