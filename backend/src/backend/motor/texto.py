import re
import unicodedata


def remover_acentos( texto: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )


def carregar_lista( arquivo: str) -> list:
    """Carrega lista simples de expressões de um arquivo .txt"""
    lista = []
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    lista.append(remover_acentos(linha.lower()))
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado.")
    return lista

def tokenizar_linha( linha: str) -> list:
    linha_normalizada =remover_acentos(linha.lower())
    return re.findall(r"\w+", linha_normalizada)