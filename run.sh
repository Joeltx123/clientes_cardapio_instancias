#!/bin/bash
source venv/bin/activate
echo "Ativando ambiente virtual e iniciando a API do Cardápio Pro..."
uvicorn main:app --host 0.0.0.0 --port 5002 --reload
