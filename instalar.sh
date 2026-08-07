#!/bin/bash

echo "========================================================"
echo "  VERIFICANDO AMBIENTE NO LINUX / TERMUX"
echo "========================================================"

# 1. Verifica e instala o Python se faltar
if ! command -v python3 &> /dev/null; then
    echo "⚠️ Python3 não encontrado no sistema."
    echo "Tentando instalar o Python automaticamente..."
    
    if command -v apt &> /dev/null; then
        sudo apt update && sudo apt install -y python3 python3-pip git
    elif command -v pkg &> /dev/null; then
        pkg update && pkg install -y python python-pip git
    else
        echo "❌ Gerenciador de pacotes não suportado automaticamente."
        echo "Por favor, instale o Python3 manualmente."
        exit 1
    fi
else
    echo "✅ Python3 já está instalado."
fi

# 2. Verifica e instala o PostgreSQL se faltar
if ! command -v psql &> /dev/null; then
    echo "⚠️ PostgreSQL não encontrado."
    echo "Tentando instalar o PostgreSQL automaticamente..."
    
    if command -v apt &> /dev/null; then
        sudo apt install -y postgresql postgresql-contrib
        sudo service postgresql start
    elif command -v pkg &> /dev/null; then
        pkg install -y postgresql
        pg_ctl -D $PREFIX/var/lib/postgresql start
    fi
else
    echo "✅ PostgreSQL já está instalado."
fi

# 3. Executa o instalador mestre em Python
echo "--------------------------------------------------------"
echo "🚀 Executando o instalador principal..."
python3 instalar.py
