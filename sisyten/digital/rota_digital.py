import json
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from sisyten.cardapio import cardapio
from sisyten import json_core

try:
    from sisyten.pedido import pedido as pedidos
except ImportError:
    try:
        from sisyten import pedidos
    except ImportError:
        pedidos = None

router = APIRouter()

@router.get("/mesa/cardapio", response_class=HTMLResponse)
def ver_cardapio(request: Request, mesa: int = None):
    if mesa is None:
        raise HTTPException(status_code=400, detail="Mesa não informada. Por favor, escaneie o QR Code da mesa.")

    try:
        produtos_lista = cardapio.listar_cardapio()
    except Exception:
        produtos_lista = []

    try:
        config = json_core.ler_json_seguro("dados/configuracao.json", {"nome_estabelecimento": "Meu Estabelecimento"})
    except Exception:
        config = {"nome_estabelecimento": "Meu Estabelecimento"}

    cat_dict = {}
    for prod in produtos_lista:
        cat = prod.get("categoria", "Outros")
        if cat not in cat_dict:
            cat_dict[cat] = []
        cat_dict[cat].append(prod)

    return request.app.state.templates.TemplateResponse(
        request, 
        "cardapio_digital.html", 
        {
            "request": request,
            "mesa": mesa,
            "nome_estabelecimento": config.get("nome_estabelecimento", "Cardápio Digital"),
            "categorias": cat_dict
        }
    )

@router.get("/delivery/cardapio", response_class=HTMLResponse)
def ver_cardapio_delivery(request: Request):
    try:
        produtos_lista = cardapio.listar_cardapio()
    except Exception:
        produtos_lista = []

    try:
        config = json_core.ler_json_seguro("dados/configuracao.json", {"nome_estabelecimento": "Meu Estabelecimento"})
    except Exception:
        config = {"nome_estabelecimento": "Meu Estabelecimento"}

    cat_dict = {}
    for prod in produtos_lista:
        cat = prod.get("categoria", "Outros")
        if cat not in cat_dict:
            cat_dict[cat] = []
        cat_dict[cat].append(prod)

    return request.app.state.templates.TemplateResponse(
        request, 
        "cardapio_digital.html", 
        {
            "request": request,
            "mesa": "Delivery",
            "nome_estabelecimento": config.get("nome_estabelecimento", "Cardápio Delivery"),
            "categorias": cat_dict
        }
    )

@router.post("/mesa/cardapio/enviar_pedido", response_class=JSONResponse)
def enviar_pedido(payload: dict):
    try:
        mesa = payload.get("mesa")
        itens = payload.get("itens", [])

        pedido_dados = {
            "mesa": mesa,
            "itens": itens,
            "status": "pendente"
        }

        if pedidos and hasattr(pedidos, "salvar_pedido_mesa"):
            pedidos.salvar_pedido_mesa(json.dumps(pedido_dados))
        
        return {"status": "sucesso", "mensagem": "Pedido enviado com sucesso!"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "erro", "mensagem": str(e)})
