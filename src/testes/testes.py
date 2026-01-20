import os
import csv
from motor.motor import Motor

class Testes:
    def __init__(self, pasta: str = "dados/testes") -> None:
        """
        Inicializa carregando todos os arquivos CSV da pasta indicada.
        Cada linha dos CSV vira uma entrada para teste.
        """
        # caminho absoluto relativo ao app.py
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.pasta = os.path.join(base_dir, "..", pasta)
        self.pasta = os.path.abspath(self.pasta)

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
                    leitor = csv.DictReader(f, delimiter="\t")  # usa tabulação como separador
                    for linha in leitor:
                        texto = linha.get("Texto Mascarado") or linha.get("Texto") or ""
                        if texto.strip():
                            entradas.append(texto.strip())
        return entradas

    def executar(self) -> dict:
        """
        Executa os testes em massa chamando LaiAnalisador.analisar para cada entrada.
        Retorna um resumo com quantos passaram e quantos foram inválidos,
        além dos resultados individuais.
        """
        resultados = []
        total_sim = 0
        total_nao = 0

        for texto in self.entradas:
            resultado = self.analisador.analisar(texto)
            resultados.append(resultado)

            if resultado["Status"] == "SIM":
                total_sim += 1
            else:
                total_nao += 1

        return {
            "TotalEntradas": len(self.entradas),
            "Validos": total_sim,
            "Invalidos": total_nao,
            "Resultados": resultados
        }
