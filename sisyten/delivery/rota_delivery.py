from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from sisyten.delivery import delivery
import psycopg2
from psycopg2.extras import RealDictCursor

router = APIRouter()

@router.get("/delivery", response_class=HTMLResponse)
def rota_delivery_get(request: Request):
    return request.app.state.templates.TemplateResponse(
        request, "delivery.html", {"request": request}
    )

@router.post("/api/delivery")
async def api_delivery_post(request: Request):
    try:
        body = await request.json()
        acao = body.get("acao")
        dados = body.get("dados", {})

        conn = psycopg2.connect(dbname="cardapio_pro", user="postgres")
        cur = conn.cursor(cursor_factory=RealDictCursor)

        if acao == "listar":
            # Busca pedidos de delivery pendentes no banco (ajuste a tabela conforme sua estrutura)
            cur.execute("SELECT * FROM pedidos WHERE tipo = 'delivery' AND status = 'pendente' ORDER BY criado_em DESC;")
            pedidos = [dict(row) for row in cur.fetchall()]
            cur.close()
            conn.close()
            return JSONResponse({"status": "sucesso", "pedidos": pedidos})

        elif acao == "processar_pedido":
            pedido_id = dados.get("pedido_id")
            acao_tipo = dados.get("acao_tipo")
            novo_status = "cancelado" if acao_tipo == "liberar_errado" else "enviado_motoboy"

            cur.execute("UPDATE pedidos SET status = %s WHERE id = %s;", (novo_status, pedido_id))
            conn.commit()
            cur.close()
            conn.close()
            return JSONResponse({"status": "sucesso", "mensagem": "Pedido atualizado com sucesso!"})

        cur.close()
        conn.close()
        return JSONResponse({"status": "erro", "mensagem": "Ação desconhecida"})

    except Exception as e:
        return JSONResponse({"status": "erro", "mensagem": str(e)})
