from .verbo import conjugar_verbo


class MotorJuridico:
    def __init__(self):
        # Inicializa atributos
        self.expressoes_juridicas_fixas: list[str] = []
        self.expressoes_juridicas_conjugaveis: dict[str, list[str]] = self.expressoes_juridicas()
        self.expressoes_juridicas: list[str] = self.gerar_expressoes_juridicas()

    def obter_expressoes_juridicas(self):
        return self.expressoes_juridicas

    def gerar_expressoes_juridicas(self) -> list:
        lista = []
        # Fixas carregadas de arquivo
        lista.extend(self.expressoes_juridicas_fixas)

        # Conjugáveis
        for verbo, moldes in self.expressoes_juridicas_conjugaveis.items():
            conj = conjugar_verbo(verbo)
            for molde in moldes:
                for forma in conj:
                    lista.append(molde.replace("{verbo}", forma))

        return lista

    def detectar_contexto_juridico(self, linha_normalizada: str) -> str | None:
        for exp in self.expressoes_juridicas:
            if exp in linha_normalizada:
                return exp
        return None

    def expressoes_juridicas(self):
        return {
            "requerer": [
                "venho por meio desta {verbo}",
                "requer-se",
                "requerimento administrativo",
                "requerimento judicial"
            ],
            "fazer": [
                "faço requerimento",
                "faço pedido"
            ]
        }
