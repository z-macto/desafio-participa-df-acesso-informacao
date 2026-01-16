import unicodedata

class EntradasProibidas:
    def __init__(self, arquivo: str = "dados/palavras_proibidas.txt"):
        self.arquivo = arquivo

    def _remover_acentos(self, texto: str) -> str:
        """
        Remove acentos de qualquer string.
        """
        return ''.join(
            c for c in unicodedata.normalize('NFD', texto)
            if unicodedata.category(c) != 'Mn'
        )

    def carregar(self) -> list:
        """
        Lê o arquivo .txt e devolve uma lista de palavras proibidas.
        Ignora linhas vazias, remove espaços extras, coloca em caixa baixa e sem acentuação.
        """
        palavras = []
        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                for linha in f:
                    palavra = linha.strip()
                    if palavra:  # ignora linhas vazias
                        palavra = self._remover_acentos(palavra.lower())
                        palavras.append(palavra)
        except FileNotFoundError:
            print(f"Arquivo {self.arquivo} não encontrado.")
        return palavras
