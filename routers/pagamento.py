from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/pagamento", response_class=HTMLResponse)
def pagamento_get(request: Request):
    return templates.TemplateResponse(request, "pagamento.html", {"request": request})
