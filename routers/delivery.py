from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/{slug}/delivery")
async def delivery_get(request: Request, slug: str):
    db = get_db()
    cursor = db.cursor()
    est_id = 1
    try:
        cursor.execute("SELECT id FROM estabelecimentos WHERE slug = %s", (slug,))
        est = cursor.fetchone()
        if est:
            est_id = est[0]
    except Exception:
        pass
    finally:
        cursor.close()
        db.close()

    return templates.TemplateResponse(request, name="delivery.html", context={"request": request, "slug": slug, "estab_id": est_id})
