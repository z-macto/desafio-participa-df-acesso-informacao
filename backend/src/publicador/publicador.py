import csv
import os
import random
from datetime import datetime, timedelta

from flask import jsonify, json

from src.api.solicitacoes import db
from src.backend.motor.motor import Motor
from src.backend.motor.texto import obter_pasta


def gerar_lista_datas_inteiros():
    inicio = datetime(2026, 1, 8)
    fim = datetime(2026, 1, 25)
    delta = fim - inicio

    lista = []
    for i in range(delta.days + 1):  # inclui o último dia
        data = inicio + timedelta(days=i)
        numero = random.randint(30, 80)
        lista.append((data.strftime("%d/%m/%Y"), numero))

    return lista


def publique():
    # Exemplo de uso

    pasta = obter_pasta("dados/testes")

    entradas = carregar_csvs(pasta)

    db.remover_solicitacoes_antigas()
    print(entradas)

    motor = Motor()

    resultado = gerar_lista_datas_inteiros()
    for item in resultado:

        (data,quantidade) = item

        print("Data :: ",data)
        print(quantidade)

        for i in range(0,quantidade):
            print("Processando ",i)

            texto = random.choice(entradas)

            resposta = motor.analisar(texto)

            resposta_json = jsonify({
                "resposta": resposta,
            })

            id_solicitacao = db.inserir_solicitacao(texto,json.dumps(resposta_json.get_json(), ensure_ascii=False))



def carregar_csvs(pasta) -> list[str]:
    """
    Lê todos os arquivos .csv da pasta e retorna uma lista com os textos de cada linha.
    """
    entradas = []
    if not os.path.exists(pasta):
        raise FileNotFoundError(f"Pasta '{pasta}' não encontrada em {pasta}")

    for nome_arquivo in os.listdir(pasta):
        caminho = os.path.join(pasta, nome_arquivo)
        print(">>> ",caminho)

        if os.path.isfile(caminho) and nome_arquivo.endswith(".csv"):
            with open(caminho, "r", encoding="utf-8") as f:
                leitor = csv.DictReader(f, delimiter="\t")
                for linha in leitor:
                    texto = linha.get("Texto Mascarado") or linha.get("Texto") or ""
                    if texto.strip():
                        entradas.append(texto.strip())
    return entradas