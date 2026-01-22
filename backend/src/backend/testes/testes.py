import os
import csv
from src.backend.motor.motor import Motor

from src.backend.motor.texto import obter_pasta


class Testes:
    def __init__(self, pasta: str = "dados/testes") -> None:
        """
        Inicializa carregando todos os arquivos CSV da pasta indicada.
        Cada linha dos CSV vira uma entrada para teste.
        """
        self.pasta = obter_pasta(pasta)

        self.entradas = self._carregar_csvs()
        self.analisador = Motor()

    def _carregar_csvs(self) -> list[str]:
        """
        Lê todos os arquivos .csv da pasta e retorna uma lista com os textos de cada linha.
        """
        entradas = []
        if not os.path.exists(self.pasta):
            raise FileNotFoundError(f"Pasta '{self.pasta}' não encontrada em {self.pasta}")

        for nome_arquivo in os.listdir(self.pasta):
            caminho = os.path.join(self.pasta, nome_arquivo)
            if os.path.isfile(caminho) and nome_arquivo.endswith(".csv"):
                with open(caminho, "r", encoding="utf-8") as f:
                    leitor = csv.DictReader(f, delimiter="\t")
                    for linha in leitor:
                        texto = linha.get("Texto Mascarado") or linha.get("Texto") or ""
                        if texto.strip():
                            entradas.append(texto.strip())
        return entradas

    def executar(self) -> dict:
        """
        Executa os testes em massa chamando Motor.analisar para cada entrada.
        Retorna um dict com resumo e resultados individuais.
        """
        resultados = []
        total_sim = 0
        total_nao = 0

        for texto in self.entradas:
            resultado = self.analisador.analisar(texto)   # agora retorna dict
            resultados.append(resultado)

            if resultado.get("Status") == "SIM":
                total_sim += 1
            else:
                total_nao += 1

        resumo = {
            "TotalEntradas": len(self.entradas),
            "Validos": total_sim,
            "Invalidos": total_nao,
            "Resultados": resultados
        }

        return resumo   # <-- dict direto, sem json.dumps
