import json
import re

from . import api_bp
from ..backend.motor.motor import Motor
from ..backend.testes.testes import Testes
from ..persistencia.banco_de_dados import BancoDados


def consultar_resposta(texto: str) -> dict:
    """
    Executa o Motor e retorna a resposta como dict.
    """
    motor = Motor()
    objeto_resposta = motor.analisar(texto)



    return objeto_resposta

def consultar_testes(pasta: str = "dados/testes") -> dict:
    """
    Executa os testes em massa e retorna o resumo como dict.
    """
    testes = Testes(pasta)
    objeto_resposta = testes.executar()
    return objeto_resposta


from flask import Blueprint, request, jsonify, session
from src.api.microsservico import consultar_resposta, consultar_testes


@api_bp.route("/api/solicitar_analise", methods=["POST"])
def solicitar_analise():
    data = request.get_json(silent=True) or {}
    texto = data.get("solicitacao", "").strip()

    if not texto:
        return jsonify({"erro": "Texto não informado"}), 400

    resposta = consultar_resposta(texto)

    resposta_json = jsonify({
        "resposta": resposta,
    })

    #print(resposta_json.get_json())

    db = BancoDados()
    id_solicitacao = db.inserir_solicitacao(texto,json.dumps(resposta_json.get_json(), ensure_ascii=False))

    return resposta_json, 200


@api_bp.route("/api/testes", methods=["GET"])
def realizar_testes():
    pasta: str = "dados/testes"
    testes = Testes(pasta)
    objeto_resposta = testes.executar()

    resposta_json = jsonify({
        "resposta": objeto_resposta,
    })

    #print(resposta_json.get_json())

    return resposta_json, 200

@api_bp.route("/api/estatisticas_30dias", methods=["GET"])
def estatisticas_30dias():
    db = BancoDados()
    dados = db.contar_solicitacoes_por_dia(dias=30)

    resposta_json = jsonify({
        "resposta": dados
    })

    print(resposta_json.get_json())
    return resposta_json, 200
