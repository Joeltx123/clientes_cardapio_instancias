from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/backup")
def ver_backup(request: Request):
    status_backup = {} # Substitua pela sua lógica/banco
    return templates.TemplateResponse("backup.html", {
        "request": request, 
        "backup": status_backup
    })
