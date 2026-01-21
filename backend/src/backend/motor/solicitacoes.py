import unicodedata

from backend.src.backend.motor.texto import remover_acentos, carregar_lista
from backend.src.backend.motor.verbo import carregar_verbos_irregulares, conjugar_regular


class Solicitacoes:
    def __init__(self,
                 arquivo_verbos_regulares: str = "dados/parametros/verbos_regulares.txt",
                 arquivo_verbos_irregulares: str = "dados/parametros/verbos_irregulares.txt",
                 arquivo_expressoes_fixas: str = "dados/parametros/expressoes_fixas.txt"):

        # Carregar listas externas
        self.verbos_regulares = carregar_lista(arquivo_verbos_regulares)
        self.verbos_irregulares = carregar_verbos_irregulares(arquivo_verbos_irregulares)
        self.expressoes_fixas = carregar_lista(arquivo_expressoes_fixas)

        # Lista final
        self.lista = self.gerar_lista()

    def remover_acentos( texto: str) -> str:
        return ''.join(
            c for c in unicodedata.normalize('NFD', texto)
            if unicodedata.category(c) != 'Mn'
        )

    def carregar_lista( arquivo: str) -> list:
        """Carrega lista simples de verbos regulares ou expressões fixas de um arquivo .txt"""
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



    def gerar_lista(self) -> list:
        """Gera lista completa de palavras de solicitação"""
        lista = []
        # Verbos regulares
        for verbo in self.verbos_regulares:
            lista.extend(conjugar_regular(verbo))

        # Verbos irregulares
        for conj in self.verbos_irregulares.values():
            lista.extend(conj)

        # Expressões fixas
        lista.extend(self.expressoes_fixas)

        return lista

    def carregar(self) -> list:
        """Retorna lista completa de palavras/expressões de solicitação."""
        return self.lista
