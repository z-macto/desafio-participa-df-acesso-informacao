import re
import unicodedata
from src.solicitacoes import Solicitacoes

class LaiAnalisador:
    def __init__(self, 
                 arquivo_palavras_proibidas: str = "dados/parametros/palavras_proibidas.txt",
                 arquivo_expressoes_juridicas_fixas: str = "dados/parametros/expressoes_juridicas_fixas.txt",
                 arquivo_substantivos_solicitacao: str = "dados/parametros/substantivos_solicitacao.txt",):
        
       
                
        self.palavras_proibidas = self._carregar_lista(arquivo_palavras_proibidas)
        self.palavras_solicitacao = Solicitacoes().carregar()
        self.substantivos_solicitacao = self._carregar_lista(arquivo_substantivos_solicitacao)
        self.expressoes_juridicas_fixas = self._carregar_lista(arquivo_expressoes_juridicas_fixas)

        # Expressões jurídicas com verbos conjugáveis
        self.expressoes_juridicas_conjugaveis = {
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

        # Lista final expandida
        self.expressoes_juridicas = self._gerar_expressoes_juridicas()

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

    def _gerar_expressoes_juridicas(self) -> list:
        lista = []
        # Fixas carregadas de arquivo
        lista.extend(self.expressoes_juridicas_fixas)

        # Conjugáveis
        for verbo, moldes in self.expressoes_juridicas_conjugaveis.items():
            conj = self._conjugar_verbo(verbo)
            for molde in moldes:
                for forma in conj:
                    lista.append(molde.replace("{verbo}", forma))

        return lista

    def _detectar_contexto_juridico(self, linha_normalizada: str) -> str | None:
        for exp in self.expressoes_juridicas:
            if exp in linha_normalizada:
                return exp
        return None

    def _detectar_substantivo_solicitacao(self, linha_normalizada: str) -> str | None:
        for s in self.substantivos_solicitacao:
            if s in linha_normalizada:
                return s
        return None

    def analisar(self, texto: str) -> dict:
        linhas = texto.splitlines()
        resultado_linhas = []
        invalido = False
        motivo = None
        motivo_bloqueou = []

        for linha in linhas:
            tokens = self._tokenizar_linha(linha)
            linha_normalizada = self._remover_acentos(linha.lower())

            # Detecta solicitação (verbo)
            expressao_solicitacao = None
            for p in self.palavras_solicitacao:
                if p in linha_normalizada:
                    expressao_solicitacao = p
                    break

            # Detecta substantivo de solicitação
            substantivo_solicitacao = self._detectar_substantivo_solicitacao(linha_normalizada)

            # Detecta contexto jurídico
            expressao_juridica = self._detectar_contexto_juridico(linha_normalizada)

            # Detecta termo proibido (só se houver solicitação ou contexto jurídico)
            termo_invalido = None
            if expressao_solicitacao or substantivo_solicitacao or expressao_juridica:
                for token in tokens:
                    if token in self.palavras_proibidas:
                        termo_invalido = token
                        break

            if (expressao_solicitacao or substantivo_solicitacao or expressao_juridica) and termo_invalido:
                invalido = True
                motivo = f'Solicitação detectada ("{expressao_solicitacao or substantivo_solicitacao or expressao_juridica}") com termo inválido ("{termo_invalido}")'
                motivo_bloqueou.append({
                    "expressao": expressao_solicitacao or substantivo_solicitacao or expressao_juridica,
                    "termo_invalido": termo_invalido,
                    "posicao": linha_normalizada.find(expressao_solicitacao or substantivo_solicitacao or expressao_juridica)
                })
                resultado_linhas.append({
                    "linha": linha.strip(),
                    "status": "NAO",
                    "motivo": motivo,
                    "contexto_juridico": bool(expressao_juridica)
                })
                break
            else:
                resultado_linhas.append({
                    "linha": linha.strip(),
                    "status": "SIM",
                    "motivo": None,
                    "contexto_juridico": bool(expressao_juridica)
                })

        if invalido:
            validacao = "Esse pedido solicita acesso a informacoes pessoais."
            status = "NAO"
        else:
            validacao = "Pedido aceitavel !"
            status = "SIM"

        return {
            "Validacao": validacao,
            "Retorno": texto,
            "Status": status,
            "Linhas": resultado_linhas,
            "Motivo": motivo,
            "Motivo_bloqueou": motivo_bloqueou
        }
