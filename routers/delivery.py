from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/delivery", response_class=HTMLResponse)
def delivery_get(request: Request):
    return templates.TemplateResponse(request, "delivery.html", {"request": request})
