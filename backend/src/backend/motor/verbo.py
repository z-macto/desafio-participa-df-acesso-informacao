from .texto import remover_acentos


def conjugar_verbo( verbo: str) -> list:
    """Conjugações simples no presente para verbos regulares."""
    conj = []
    if verbo.endswith("ar"):
        raiz = verbo[:-2]
        conj = [raiz + "o", raiz + "a", raiz + "amos", raiz + "am"]
    elif verbo.endswith("er"):
        raiz = verbo[:-2]
        conj = [raiz + "o", raiz + "e", raiz + "emos", raiz + "em"]
    elif verbo.endswith("ir"):
        raiz = verbo[:-2]
        conj = [raiz + "o", raiz + "e", raiz + "imos", raiz + "em"]
    return [verbo] + conj


def carregar_verbos_irregulares( arquivo: str) -> dict:
    """Carrega verbos irregulares e suas conjugações de um arquivo .txt"""
    verbos = {}
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                partes = linha.strip().split(",")
                if len(partes) > 1:
                    verbo = remover_acentos(partes[0].lower())
                    conj = [remover_acentos(p.lower()) for p in partes]
                    verbos[verbo] = conj
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado.")
    return verbos

def conjugar_regular( verbo: str) -> list:
    """Gera conjugações simples no presente para verbos regulares."""
    conj = []
    if verbo.endswith("ar"):
        raiz = verbo[:-2]
        conj = [raiz + "o", raiz + "a", raiz + "amos", raiz + "am"]
    elif verbo.endswith("er"):
        raiz = verbo[:-2]
        conj = [raiz + "o", raiz + "e", raiz + "emos", raiz + "em"]
    elif verbo.endswith("ir"):
        raiz = verbo[:-2]
        conj = [raiz + "o", raiz + "e", raiz + "imos", raiz + "em"]
    return [verbo] + conj