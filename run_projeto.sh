#!/bin/bash
echo "==> Limpando arquivos de cache pyc antigos..."
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null

echo "==> Verificando arquivo run.sh existente..."
if [ -f "run.sh" ]; then
    echo "Encontrado script run.sh no projeto. Executando..."
    bash run.sh
else
    echo "Arquivo run.sh não encontrado. Iniciando via uvicorn padrão no app.py..."
    if [ ! -d "venv" ]; then
        python3 -m venv venv
    fi
    source venv/bin/activate
    pip install --upgrade pip
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt
    else
        pip install fastapi uvicorn sqlalchemy psycopg2-binary jinja2 python-dotenv
    fi
    uvicorn app:app --host 0.0.0.0 --port 8000 --reload
fi
