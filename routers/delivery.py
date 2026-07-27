from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")
templates.env.cache = None

@router.get("/admin/delivery", response_class=HTMLResponse)
def delivery_get(request: Request, db = Depends(get_db)):
    return templates.TemplateResponse(request, "delivery.html", {"request": request})
