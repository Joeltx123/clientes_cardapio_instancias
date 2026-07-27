import os, re
base = os.path.expanduser("~/Projetos/CardapioPro_V2")

# A. Atualizar rotas_pagamento.py
rotas = os.path.join(base, "rotas_pagamento.py")
with open(rotas, "r") as f: code = f.read()
nova_funcao = """@app.route('/processar_pagamento/<int:numero_mesa>/<forma>', methods=['GET', 'POST'])
def processar_pagamento(numero_mesa, forma):
    from flask import request
    conn = conectar()
    cur = conn.cursor()

    # Busca o valor total real do pedido somando os itens
    cur.execute("SELECT SUM(i.preco) FROM itens_pedido ip JOIN itens i ON ip.item_id = i.id JOIN pedidos p ON ip.pedido_id = p.id WHERE p.mesa = %s::text AND p.status = 'cozinha'", (numero_mesa,))
    res = cur.fetchone()
    valor_total = res[0] if res and res[0] else 0

    # Se for dinheiro, pega o valor digitado no form. Se não, assume o valor total.
    valor_pago = float(request.form.get('valor_pago', valor_total)) if request.method == 'POST' and forma == 'Dinheiro' else float(valor_total)
    troco = max(0, valor_pago - float(valor_total))

    # Salva todos os dados
    cur.execute("UPDATE pedidos SET status = 'finalizado', forma_pagamento = %s, valor_total = %s, troco = %s, data_finalizacao = NOW() WHERE mesa = %s::text AND status = 'cozinha'", (forma, valor_total, troco, numero_mesa))
    cur.execute("UPDATE mesas SET status = 'livre' WHERE numero = %s", (numero_mesa,))
    conn.commit()
    cur.close(); conn.close()

    return f"<h1>Pagamento em {forma} efetuado com Sucesso!</h1><h3>Total do Pedido: R$ {valor_total:.2f}</h3><h3 style='color:green;'>Troco a devolver: R$ {troco:.2f}</h3><br><a href='/pagamento'>Voltar para as Mesas</a>"
"""
code = re.sub(r"@app\.route\('/processar_pagamento/.*", nova_funcao, code, flags=re.DOTALL)
with open(rotas, "w") as f: f.write(code)

# B. Atualizar a consulta no app.py para incluir a busca do troco
app = os.path.join(base, "app.py")
with open(app, "r") as f: app_code = f.read()
app_code = app_code.replace("SELECT mesa, valor_total, forma_pagamento, data_finalizacao FROM pedidos", "SELECT mesa, valor_total, forma_pagamento, data_finalizacao, troco FROM pedidos")
with open(app, "w") as f: f.write(app_code)

# C. Substituir o link simples de 'Dinheiro' por um campo perguntando o valor
pag = os.path.join(base, "templates", "pagamento.html")
with open(pag, "r") as f: html = f.read()
html = re.sub(r'<a href="[^"]*/Dinheiro"[^>]*>.*?</a>',
              r'<form action="/processar_pagamento/{{ mesa }}/Dinheiro" method="POST" style="margin: 10px 0;"><label>💰 Dinheiro (Cliente Pagou: R$ </label><input type="number" step="0.01" name="valor_pago" required style="width: 80px;"><button type="submit">Pagar</button>)</form>', html)
with open(pag, "w") as f: f.write(html)

print("\n✔️ Código atualizado com sucesso! O sistema agora calcula o troco.")

