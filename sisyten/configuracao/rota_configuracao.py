from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from sisyten.configuracao import configuracao
import json

router = APIRouter()

@router.get("/configuracao", response_class=HTMLResponse)
def rota_configuracao_get(request: Request):
    # Consulta os dados usando a função do configuracao.py
    resposta_json = configuracao.consultar_configuracao()
    # Se a função retornar dict diretamente ou string json, tratamos com segurança:
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
    # Validação simples da senha de admin (ajuste conforme a sua regra de segurança do sistema)
    if senha_admin != "123456": # Troque ou ajuste se necessário
        resposta = {"status": "erro", "mensagem": "Senha do Administrador incorreta!"}
    else:
        # Prepara o payload para a função de salvamento do configuracao.py
        payload = {
            "acao": "salvar",
            "dados": {
                "nome": nome_estabelecimento,
                "mesas": quantidade_mesas
            }
        }
        # Processa via lógica do configuracao.py
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
