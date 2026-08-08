from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from sisyten.configuracao import configuracao
import json

router = APIRouter()

@router.get("/configuracao", response_class=HTMLResponse)
def rota_configuracao_get(request: Request):
    resposta_json = configuracao.consultar_configuracao()
    res = resposta_json if isinstance(resposta_json, dict) else json.loads(resposta_json)

    dados = res.get("dados", {})
    status = res.get("status", "sucesso")
    mensagem = res.get("mensagem") if status == "erro" else None

    return request.app.state.templates.TemplateResponse(
        request,
        "configuracao.html",
        {"request": request, "dados": dados, "mensagem": mensagem, "status": status}
    )

@router.post("/configuracao", response_class=HTMLResponse)
def rota_configuracao_post(
    request: Request,
    nome_estabelecimento: str = Form(...),
    quantidade_mesas: int = Form(...),
    senha_admin: str = Form(...)
):
    if senha_admin != "Soulivre01":
        resposta = {"status": "erro", "mensagem": "Senha do Administrador incorreta!"}
    else:
        payload = {
            "acao": "salvar",
            "dados": {
                "nome": nome_estabelecimento,
                "mesas": quantidade_mesas
            }
        }
        resultado_str = configuracao.processar_requisicao(json.dumps(payload))
        resposta = json.loads(resultado_str)

    dados = {
        "nome": nome_estabelecimento,
        "quantidade_mesas": quantidade_mesas,
        "slug": "estabelecimento"
    }

    return request.app.state.templates.TemplateResponse(
        request,
        "configuracao.html",
        {"request": request, "dados": dados, "mensagem": resposta.get("mensagem"), "status": resposta.get("status")}
    )
