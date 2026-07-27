import os
import zipfile
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from banco import conectar
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

SENHA_ZIP = "SouLivre01"

def gerar_pdf_fechamento(data_alvo_str):
    conn = conectar()
    cur = conn.cursor()
    try:
        cur.execute("SELECT SUM(valor_total) FROM historico_mesas")
        res_total = cur.fetchone()
        faturamento_total = res_total[0] if res_total and res_total[0] else 0.0

        cur.execute("SELECT forma_pagamento, SUM(valor_total) FROM historico_mesas GROUP BY forma_pagamento")
        por_forma = cur.fetchall()

        cur.execute("SELECT mesa, valor_total, forma_pagamento, troco, data_hora FROM historico_mesas ORDER BY id DESC")
        historico = cur.fetchall()

        if not historico and faturamento_total == 0.0:
            return False

        pasta_base = os.path.join(os.getcwd(), "Relatorios_Fechamento")
        os.makedirs(pasta_base, exist_ok=True)

        nome_pdf = f"Fechamento_{data_alvo_str}.pdf"
        caminho_pdf = os.path.join(pasta_base, nome_pdf)

        doc = SimpleDocTemplate(caminho_pdf, pagesize=letter)
        elementos = []
        styles = getSampleStyleSheet()

        titulo_style = ParagraphStyle(
            'Titulo',
            parent=styles['Heading1'],
            fontSize=18,
            alignment=1,
            textColor=colors.HexColor("#1e293b")
        )

        elementos.append(Paragraph(f"<b>Relatório de Fechamento Diário</b>", titulo_style))
        elementos.append(Paragraph(f"<b>Data do Fechamento:</b> {data_alvo_str}", styles['Normal']))
        elementos.append(Spacer(1, 15))

        dados_resumo = [["Faturamento Total", f"R$ {faturamento_total:.2f}"]]
        tabela_resumo = Table(dados_resumo, colWidths=[200, 200])
        tabela_resumo.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f1f5f9")),
            ('TEXTCOLOR', (0,0), (-1,-1), colors.HexColor("#0f172a")),
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,-1), 12),
            ('BOTTOMPADDING', (0,0), (-1,-1), 8),
            ('TOPPADDING', (0,0), (-1,-1), 8),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('GRID', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ]))
        elementos.append(tabela_resumo)
        elementos.append(Spacer(1, 15))

        elementos.append(Paragraph("<b>Faturamento por Forma de Pagamento</b>", styles['Heading3']))
        elementos.append(Spacer(1, 5))

        dados_formas = [["Forma de Pagamento", "Total"]]
        for forma, valor in por_forma:
            dados_formas.append([str(forma), f"R$ {valor:.2f}"])

        tabela_formas = Table(dados_formas, colWidths=[200, 200])
        tabela_formas.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#e2e8f0")),
            ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor("#0f172a")),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('GRID', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ]))
        elementos.append(tabela_formas)
        elementos.append(Spacer(1, 15))

        elementos.append(Paragraph("<b>Histórico Detalhado de Mesas Fechadas</b>", styles['Heading3']))
        elementos.append(Spacer(1, 5))

        dados_hist = [["Mesa", "Valor", "Pagamento", "Troco", "Data/Hora"]]
        for h in historico:
            dados_hist.append([str(h[0]), f"R$ {h[1]:.2f}", str(h[2]), f"R$ {h[3]}", str(h[4])])

        tabela_hist = Table(dados_hist, colWidths=[70, 80, 90, 70, 130])
        tabela_hist.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#e2e8f0")),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,-1), 9),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ]))
        elementos.append(tabela_hist)

        doc.build(elementos)

        caminho_zip = os.path.join(pasta_base, f"Fechamento_{data_alvo_str}.zip")
        comando_zip = f"zip -P {SENHA_ZIP} -j {caminho_zip} {caminho_pdf}"
        os.system(comando_zip)

        if os.path.exists(caminho_pdf):
            os.remove(caminho_pdf)

        print(f"[SUCESSO] Relatório salvo e protegido em: {caminho_zip}")

        cur.execute("DELETE FROM historico_mesas")
        conn.commit()
        return True

    except Exception as e:
        print(f"[ERRO NO FECHAMENTO]: {e}")
        conn.rollback()
        return False
    finally:
        cur.close()
        conn.close()

def executar_fechamento_profissional():
    data_hoje = datetime.now().strftime('%d-%m-%Y')
    gerar_pdf_fechamento(data_hoje)

def verificar_pendencia_ao_ligar():
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM historico_mesas")
        res = cur.fetchone()
        total_registros = res[0] if res else 0

        if total_registros > 0:
            print("[INFO] Fechamento pendente detectado ao iniciar o servidor. Processando...")
            data_pendente = (datetime.now() - timedelta(days=1)).strftime('%d-%m-%Y')
            gerar_pdf_fechamento(data_pendente)
        cur.close()
        conn.close()
    except Exception as e:
        # Ignora caso a tabela ainda não exista
        pass

# Executa a verificação de forma segura
verificar_pendencia_ao_ligar()

scheduler = BackgroundScheduler()
scheduler.add_job(func=executar_fechamento_profissional, trigger="cron", hour=4, minute=0)
scheduler.start()


