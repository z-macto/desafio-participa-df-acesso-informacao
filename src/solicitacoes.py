class Solicitacoes:
    def __init__(self):
        # Verbos regulares base
        self.verbos_regulares = ["solicitar", "demandar", "reivindicar"]

        # Verbos irregulares com conjugações principais
        self.verbos_irregulares = {
            "pedir": ["pedir", "peco", "pede", "pedimos", "pedem", "pedi", "pedirei", "pediria"],
            "requerer": ["requerer", "requero", "requer", "requeremos", "requerem", "requeri", "requererei"],
            "querer": ["querer", "quero", "quer", "queremos", "querem", "quis", "queria", "quererei"],
            "ter": ["ter", "tenho", "tem", "temos", "têm", "tive", "terei", "teria"],
            "obter": ["obter", "obtenho", "obtem", "obtemos", "obtem", "obtive", "obterei", "obteria"],
            "precisar": ["precisar", "preciso", "precisa", "precisamos", "precisam", "precisei", "precisarei"]
        }

        # Expressões fixas
        self.expressoes_fixas = [
            "gostaria de acesso", "desejo acesso", "quero acesso",
            "preciso acesso", "necessito acesso", "necessitamos acesso",
            "venho por meio desta solicitar", "venho requerer", "faço requerimento",
            "faço pedido", "faço solicitacao", "encaminho solicitacao",
            "protocolar solicitacao", "requerimento administrativo",
            "requerimento oficial", "requerimento judicial",
            "abrir os documentos", "liberar acesso", "liberar consulta",
            "liberar visualizacao", "liberar informacoes", "liberar dados"
        ]

        # Lista final
        self.lista = self._gerar_lista()

    def _conjugar_regular(self, verbo: str) -> list:
        """
        Gera conjugações simples no presente para verbos regulares.
        """
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
        """
        Gera lista completa de palavras de solicitação:
        - conjugações de verbos regulares
        - conjugações de verbos irregulares
        - expressões fixas
        """
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
        """
        Retorna lista completa de palavras/expressões de solicitação.
        """
        return self.lista
