import unicodedata


def _remover_acentos(self, texto: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )


def _carregar_lista(self, arquivo: str) -> list:
    """Carrega lista simples de expressões de um arquivo .txt"""
    lista = []
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    lista.append(self._remover_acentos(linha.lower()))
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado.")
    return lista

def _tokenizar_linha(self, linha: str) -> list:
    linha_normalizada = self._remover_acentos(linha.lower())
    return re.findall(r"\w+", linha_normalizada)