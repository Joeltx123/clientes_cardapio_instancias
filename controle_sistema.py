import os
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from banco import conectar

controle_bp = APIRouter()

# Garante que a tabela de status do sistema existe no banco
def garantir_tabela_controle():
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS sistema_status (
                id SERIAL PRIMARY KEY,
                status VARCHAR(20) DEFAULT 'ativo',
                mensagem VARCHAR(255) DEFAULT ''
            )
        """)
        cur.execute("SELECT COUNT(*) FROM sistema_status")
        if cur.fetchone()[0] == 0:
            cur.execute("INSERT INTO sistema_status (status, mensagem) VALUES ('ativo', '')")
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"[AVISO] Não foi possível garantir a tabela de controle agora: {e}")

garantir_tabela_controle()

# Função auxiliar para verificar o status atual
def obter_status_sistema():
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT status, mensagem FROM sistema_status ORDER BY id DESC LIMIT 1")
        res = cur.fetchone()
        cur.close()
        conn.close()
        if res:
            return res[0], res[1]
    except Exception:
        pass
    return 'ativo', ''

# Middleware/Função para interceptar e bloquear requisições se necessário
def verificar_bloqueio_global():
    # Evita bloquear a própria rota de comando
    # No FastAPI, o request path vem tratado no middleware global
    pass

def checar_bloqueio_requisicao(path: str):
    if path == "/api/sistema/comando":
        return None

    status, mensagem = obter_status_sistema()

    # Rotas do cliente final que devem ser bloqueadas se o sistema estiver pausado ou bloqueado
    eh_rota_cliente = path == "/" or path.startswith("/menu/") or path.startswith("/extrato/")

    if status == 'bloqueado' or (status == 'pausado' and eh_rota_cliente):
        titulo = "Sistema Bloqueado" if status == 'bloqueado' else "Estabelecimento Pausado"
        msg_padrao = "Acesso suspenso temporariamente." if status == 'bloqueado' else "O estabelecimento está pausado no momento."
        msg_final = mensagem or msg_padrao

        html_conteudo = f"""
            <html>
            <head><title>{titulo}</title><meta charset="utf-8">
            <style>body{{font-family:Arial;background:#121212;color:#ff5252;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;}}
            .box{{background:#1e1e1e;padding:40px;border-radius:8px;text-align:center;box-shadow:0 4px 15px rgba(0,0,0,0.5);}}
            h1{{margin-bottom:10px;}} p{{color:#aaa;}}</style></head>
            <body><div class="box">
                <h1>🔒 {titulo}</h1>
                <p>{msg_final}</p>
            </div></body></html>
        """
        return HTMLResponse(content=html_conteudo, status_code=403)

    if status == 'excluido':
        html_conteudo = """
            <html>
            <head><title>Sistema Desativado</title><meta charset="utf-8">
            <style>body{font-family:Arial;background:#121212;color:#ff9800;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;}
            .box{background:#1e1e1e;padding:40px;border-radius:8px;text-align:center;box-shadow:0 4px 15px rgba(0,0,0,0.5);}
            h1{margin-bottom:10px;} p{color:#aaa;}</style></head>
            <body><div class="box">
                <h1>⚠️ Sistema Desativado</h1>
                <p>Os registros desta unidade foram removidos ou desativados pela matriz.</p>
            </div></body></html>
        """
        return HTMLResponse(content=html_conteudo, status_code=403)

    return None

# API para a Central enviar os comandos (Pausar, Bloquear, Excluir, Ativar)
@controle_bp.post('/api/sistema/comando')
async def receber_comando(request: Request):
    dados = await request.json() if request.headers.get("content-type") == "application/json" else {}
    print("[CLIENTE] Recebeu comando:", dados)
    novo_status = dados.get('status')
    mensagem = dados.get('mensagem', '')

    if novo_status not in ['ativo', 'pausado', 'bloqueado', 'excluido']:
        return JSONResponse({"erro": "Status inválido"}, status_code=400)

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("UPDATE sistema_status SET status = %s, mensagem = %s", (novo_status, mensagem))
        conn.commit()
        cur.close()
        conn.close()
        return JSONResponse({"sucesso": True, "status_atual": novo_status}, status_code=200)
    except Exception as e:
        return JSONResponse({"erro": str(e)}, status_code=500)



