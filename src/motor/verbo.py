def _conjugar_verbo(self, verbo: str) -> list:
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