#!/bin/sh

# Defina os nomes das pastas que deseja compactar
PASTA1="armazenamento_de_dados"
PASTA2="backend"
PASTA3="distribuicao"

# Nome do arquivo zip de saída
ARQUIVO_SAIDA="distribuicao/app.zip"

# Compacta as três pastas em um único arquivo zip
zip -r "$ARQUIVO_SAIDA" "$PASTA1" "$PASTA2" "$PASTA3"

echo "Compactação concluída! Arquivo gerado: $ARQUIVO_SAIDA"

