from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sisyten.pedido import pedidos

router = APIRouter()

@router.get("/pedidos", response_class=HTMLResponse)
def rota_pedidos_get(request: Request):
    dados = pedidos.obder_dados() if hasattr(pedidos, "obder_dados") else pedidos.obter_dados()
    return request.app.state.templates.TemplateResponse(
        request, "pedidos.html", {"request": request, "dados": dados}
    )

@router.post("/liberar-mesa")
def rota_liberar_mesa(mesa: int = Form(...)):
    # Simula ou chama a função de liberação de mesa se houver
    payload = '{"acao": "liberar_mesa", "mesa": ' + str(mesa) + '}'
    pedidos.processar_requisicao(payload)
    return RedirectResponse(url="/pedidos", status_code=303)
