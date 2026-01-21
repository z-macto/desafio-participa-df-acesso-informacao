import json
import re

from backend.motor.motor import Motor
from backend.motor.texto import remover_acentos
from backend.testes.testes import Testes


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
