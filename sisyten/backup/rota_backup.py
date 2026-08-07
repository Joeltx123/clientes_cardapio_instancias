from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, HTMLResponse
from sisyten.backup import backup
import os

router = APIRouter()

@router.get("/backup", response_class=HTMLResponse)
def rota_backup_pagina(request: Request):
    return request.app.state.templates.TemplateResponse(
        request, "backup.html", {"request": request}
    )

@router.post("/api/backup/executar")
def api_executar_backup():
    try:
        arquivo_zip = backup.realizar_backup()
        return JSONResponse({
            "status": "sucesso", 
            "mensagem": "Backup realizado com sucesso!", 
            "arquivo": os.path.basename(arquivo_zip)
        })
    except Exception as e:
        return JSONResponse({
            "status": "erro", 
            "mensagem": str(e)
        }, status_code=500)
