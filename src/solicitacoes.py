import unicodedata

class Solicitacoes:
    def __init__(self,
                 arquivo_verbos_regulares: str = "dados/parametros/verbos_regulares.txt",
                 arquivo_verbos_irregulares: str = "dados/parametros/verbos_irregulares.txt",
                 arquivo_expressoes_fixas: str = "dados/parametros/expressoes_fixas.txt"):

        # Carregar listas externas
        self.verbos_regulares = self._carregar_lista(arquivo_verbos_regulares)
        self.verbos_irregulares = self._carregar_verbos_irregulares(arquivo_verbos_irregulares)
        self.expressoes_fixas = self._carregar_lista(arquivo_expressoes_fixas)

        # Lista final
        self.lista = self._gerar_lista()

    def _remover_acentos(self, texto: str) -> str:
        return ''.join(
            c for c in unicodedata.normalize('NFD', texto)
            if unicodedata.category(c) != 'Mn'
        )

    def _carregar_lista(self, arquivo: str) -> list:
        """Carrega lista simples de verbos regulares ou expressões fixas de um arquivo .txt"""
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

    def _carregar_verbos_irregulares(self, arquivo: str) -> dict:
        """Carrega verbos irregulares e suas conjugações de um arquivo .txt"""
        verbos = {}
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                for linha in f:
                    partes = linha.strip().split(",")
                    if len(partes) > 1:
                        verbo = self._remover_acentos(partes[0].lower())
                        conj = [self._remover_acentos(p.lower()) for p in partes]
                        verbos[verbo] = conj
        except FileNotFoundError:
            print(f"Arquivo {arquivo} não encontrado.")
        return verbos

    def _conjugar_regular(self, verbo: str) -> list:
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

    def _gerar_lista(self) -> list:
        """Gera lista completa de palavras de solicitação"""
        lista = []
        # Verbos regulares
        for verbo in self.verbos_regulares:
            lista.extend(self._conjugar_regular(verbo))

        # Verbos irregulares
        for conj in self.verbos_irregulares.values():
            lista.extend(conj)

        # Expressões fixas
        lista.extend(self.expressoes_fixas)

        return lista

    def carregar(self) -> list:
        """Retorna lista completa de palavras/expressões de solicitação."""
        return self.lista
