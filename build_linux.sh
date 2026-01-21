#!/bin/bash
# Script para build do frontend e disponibilizar em 'distribuicao'

# Parar execução se algum comando falhar
set -e

# Ir para a pasta do frontend
cd "$(dirname "$0")/frontend"

echo "📦 Instalando dependências..."
npm install

echo "⚙️ Executando build do frontend..."
npm run build

# Voltar para a raiz do projeto
cd ..

# Criar pasta de distribuição se não existir
mkdir -p distribuicao

echo "📂 Copiando arquivos gerados para 'distribuicao'..."
cp -r frontend/dist/* distribuicao/

echo "✅ Build concluído e arquivos disponíveis em 'distribuicao'."

echo "⚙️ Executando aplicação..."
python3 backend/app.py
