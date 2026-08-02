import os
import re

print("--- ATUALIZANDO MAPA DE PACOTES DO PROJETO ---")

imports_encontrados = set()
padrao_import = re.compile(r'^(?:import\s+(\w+)|from\s+(\w+))', re.MULTILINE)

for root, dirs, files in os.walk("."):
    if "venv" in root or ".git" in root or "__pycache__" in root:
        continue
    for file in files:
        if file.endswith(".py"):
            caminho_arquivo = os.path.join(root, file)
            try:
                with open(caminho_arquivo, "r", encoding="utf-8") as f:
                    conteudo = f.read()
                    matches = padrao_import.findall(conteudo)
                    for match in matches:
                        mod = match[0] or match[1]
                        if mod:
                            imports_encontrados.add(mod.lower())
            except Exception as e:
                pass

# Mapeamento completo baseado nos módulos detectados no seu projeto
mapa_pacotes = {
    "flask": "Flask==3.0.2",
    "fastapi": "fastapi==0.110.0",
    "uvicorn": "uvicorn==0.27.1",
    "pydantic": "pydantic==2.6.4",
    "psycopg2": "psycopg2-binary==2.9.9",
    "dotenv": "python-dotenv==1.0.1",
    "requests": "requests==2.31.0",
    "qrcode": "qrcode==7.4.2",
    "pil": "Pillow==10.2.0",
    "pandas": "pandas==2.2.1",
    "openpyxl": "openpyxl==3.1.2",
    "sqlalchemy": "SQLAlchemy==2.0.27",
    "gunicorn": "gunicorn==21.2.0",
    "apscheduler": "APScheduler==3.10.4",
    "reportlab": "reportlab==4.1.0",
    "httpx": "httpx==0.27.0"
}

pacotes_finais = []
for imp in imports_encontrados:
    if imp in mapa_pacotes:
        pacote = mapa_pacotes[imp]
        if pacote not in pacotes_finais:
            pacotes_finais.append(pacote)

# Garante os essenciais caso o app rode via uvicorn/gunicorn ou postgres
essenciais = [
    "fastapi==0.110.0",
    "uvicorn==0.27.1",
    "pydantic==2.6.4",
    "psycopg2-binary==2.9.9",
    "python-dotenv==1.0.1",
    "APScheduler==3.10.4",
    "reportlab==4.1.0",
    "requests==2.31.0",
    "qrcode==7.4.2",
    "Pillow==10.2.0"
]

for esp in essenciais:
    if esp not in pacotes_finais:
        pacotes_finais.append(esp)

with open("requirements.txt", "w") as f:
    for p in sorted(pacotes_finais):
        f.write(p + "\n")

print("\nRequirements.txt gerado com sucesso contendo todas as dependencias do FastAPI e servicos!")
