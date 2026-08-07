from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from sisyten.pagamento import pagamento

router = APIRouter()

@router.get("/pagamento", response_class=HTMLResponse)
def rota_pagamento_get(request: Request):
    return request.app.state.templates.TemplateResponse(
        request, "pagamento.html", {"request": request}
    )

@router.post("/api/pagamento")
async def api_pagamento_post(request: Request):
    try:
        body = await request.json()
        payload_str = str(body) if isinstance(body, dict) else body
        # Passa o payload para a função de processamento existente no pagamento.py
        resposta_json = pagamento.processar_requisicao(body)
        
        import json
        if isinstance(resposta_json, str):
            return JSONResponse(json.loads(resposta_json))
        return JSONResponse(resposta_json)
    except Exception as e:
        return JSONResponse({"status": "erro", "mensagem": str(e), "transacoes": []})
