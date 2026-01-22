#!/bin/bash
# Script para executar aplicação python
set -e

mkdir -p armazenamento_de_dados

echo "⚙️ Executando aplicação..."
python3 backend/app.py
