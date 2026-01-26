@echo off
REM Script para build do frontend e disponibilizar em 'distribuicao'

REM Parar execução se algum comando falhar
setlocal enabledelayedexpansion

REM Ir para a pasta do frontend
cd /d "%~dp0frontend"

echo 📦 Instalando dependências...
call npm install

echo ⚙️ Executando build do frontend...
call npm run build

REM Voltar para a raiz do projeto
cd ..

REM Criar pasta de distribuição se não existir
if not exist distribuicao (
    mkdir distribuicao
)

if not exist armazenamento_de_dados (
    mkdir armazenamento_de_dados
)

echo 📂 Copiando arquivos gerados para 'distribuicao'...
xcopy /E /Y frontend\dist\* distribuicao\

echo ✅ Build concluído e arquivos disponíveis em 'distribuicao'.

echo ⚙️ Executando aplicação...
py backend\app.py
