@echo off
TITLE Instalador Completo - Cardapio Pro
cd /d "%~dp0"
echo ========================================================
echo   VERIFICANDO E CONFIGURANDO O AMBIENTE NO WINDOWS
echo ========================================================

:: 1. Verifica/Instala o Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python nao encontrado. Instalando via Winget...
    winget install Python.Python.3.11 --silent --accept-source-agreements --accept-package-agreements
    python --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo [X] Erro ao instalar o Python automaticamente. Instale em python.org (Marque "Add to PATH").
        goto FIM
    )
) else (
    echo [+] Python ja esta instalado.
)

:: 2. Verifica/Instala o PostgreSQL
sc query postgresql-x64-15 >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] PostgreSQL nao encontrado. Instalando via Winget...
    winget install PostgreSQL.PostgreSQL.15
) else (
    echo [+] PostgreSQL ja esta instalado.
)

:: 3. Baixa ou atualiza o projeto do GitHub se nao existir a pasta/arquivos
if not exist "instalar.py" (
    echo [!] Baixando o instalador do projeto do GitHub...
    powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/SEU_USUARIO/SEU_REPOSITORIO/main/instalar.py' -OutFile 'instalar.py'"
)

if not exist "requirements.txt" (
    echo [!] Baixando dependencias do GitHub...
    powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/SEU_USUARIO/SEU_REPOSITORIO/main/requirements.txt' -OutFile 'requirements.txt'"
)

:: 4. Roda o script principal que instala dependencias e configura o banco
echo.
echo [+] Iniciando a instalacao completa do projeto...
python instalar.py

:FIM
echo.
echo ========================================================
echo Processo concluido. Pressione qualquer tecla para sair.
echo ========================================================
pause >nul
