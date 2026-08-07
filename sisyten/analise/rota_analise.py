from fastapi import APIRouter, Request, Query
from fastapi.responses import HTMLResponse
from sisyten.analise import analise

router = APIRouter()

@router.get("/analise", response_class=HTMLResponse)
def rota_analise_get(request: Request, periodo: str = Query("todos")):
    dados_analise = analise.obter_dados(filtro_periodo=periodo)
    return request.app.state.templates.TemplateResponse(
        request, 
        "analise.html", 
        {
            "request": request, 
            "analise": dados_analise, 
            "periodo_atual": periodo
        }
    )
