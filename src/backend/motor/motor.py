import json
import math
import re

from backend.motor.juridico import MotorJuridico
from backend.motor.nominal import detectar_substantivo_solicitacao
from backend.motor.solicitacoes import Solicitacoes
from backend.motor.texto import carregar_lista, remover_acentos, tokenizar_linha


class Motor:
    def __init__(self,
                 arquivo_palavras_proibidas: str = "dados/parametros/palavras_proibidas.txt",
                 arquivo_expressoes_juridicas_fixas: str = "dados/parametros/expressoes_juridicas_fixas.txt",
                 arquivo_substantivos_solicitacao: str = "dados/parametros/substantivos_solicitacao.txt"):

        # Instância do motor jurídico
        self.juridico = MotorJuridico()

        # Carregamento de listas externas
        self.palavras_proibidas = carregar_lista(arquivo_palavras_proibidas)
        self.palavras_solicitacao = Solicitacoes().carregar()
        self.substantivos_solicitacao = carregar_lista(arquivo_substantivos_solicitacao)
        self.expressoes_juridicas_fixas = carregar_lista(arquivo_expressoes_juridicas_fixas)

        # Expressões jurídicas com verbos conjugáveis
        self.expressoes_juridicas_conjugaveis = self.juridico.obter_expressoes_juridicas()

        # Lista completa de expressões jurídicas
        self.expressoes_juridicas = self.juridico.gerar_expressoes_juridicas()

    def analisar(self, texto: str) -> dict:

        documentos_encontrados = []
        DOCUMENTO_CPF = r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b"
        DOCUMENTO_CNPJ =r"\b\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}\b"
        DOCUMENTO_RG = r"\b\d{2}\.?\d{3}\.?\d{3}-?\d{1}\b"
        DOCUMENTO_MATRICULA = r"\b\d{3}\.\d{3}\s\d\b"

        for linha_simples in texto.split(" "):
            linha_simples = remover_acentos(linha_simples.lower())

            # 🔎 Detecta CPFs usando regex
            for documento in re.findall(DOCUMENTO_CPF, linha_simples):
                documentos_encontrados.append(("CPF",documento))
            for documento in re.findall(DOCUMENTO_CNPJ, linha_simples):
                documentos_encontrados.append(("CNPJ",documento))
            for documento in re.findall(DOCUMENTO_RG, linha_simples):
                documentos_encontrados.append(("RG",documento))

        linhas = texto.split(".")
        resultado_linhas = []
        invalido = False
        motivo = None
        motivo_bloqueou = []

        criticidade_linhas_pessoal = 0
        criticidade_verbos_solicitacao = 0
        criticidade_palavras_proibidas = 0

        questionamento_solicitacao_linhas = 0
        questionamento_total_linhas = 0


        for linha in linhas:
            tokens = tokenizar_linha(linha)
            linha_normalizada = remover_acentos(linha.lower())

            termos_proibidos_encontrados = set()
            verbos_solicitacao_encontrados = set()
            tem_solicitacao = False
            tem_termo_proibido = False
            tem_contexto_juridico = False

            # Detecta verbos de solicitação
            for p in self.palavras_solicitacao:
                if p in tokens:
                    verbos_solicitacao_encontrados.add(p)
                    tem_solicitacao = True

            # Detecta substantivo de solicitação
            substantivo_solicitacao = detectar_substantivo_solicitacao(
                self.substantivos_solicitacao, linha_normalizada
            )
            if substantivo_solicitacao:
                verbos_solicitacao_encontrados.add(substantivo_solicitacao)
                tem_solicitacao = True

            # Detecta contexto jurídico
            expressao_juridica = self.juridico.detectar_contexto_juridico(linha_normalizada)
            if expressao_juridica:
                tem_contexto_juridico = True

            # Detecta termos proibidos
            for token in tokens:
                if token in self.palavras_proibidas:
                    termos_proibidos_encontrados.add(token)
                    tem_termo_proibido = True
                    criticidade_palavras_proibidas += 1

            if tem_termo_proibido:
                criticidade_linhas_pessoal += 1

            # Define status e motivo
            if tem_solicitacao and tem_termo_proibido:
                invalido = True
                criticidade_verbos_solicitacao += 1
                motivo = (
                    f'Solicitação detectada com termos proibidos: {", ".join(termos_proibidos_encontrados)}'
                )
                motivo_bloqueou.append({
                    "expressao": verbos_solicitacao_encontrados or expressao_juridica,
                    "termo_invalido": termos_proibidos_encontrados,
                    "posicao": linha_normalizada.find(
                        next(iter(verbos_solicitacao_encontrados), "")
                    )
                })
                status_linha = "NAO"
                motivo_linha = motivo
            else:
                status_linha = "SIM"
                motivo_linha = None

            # Adiciona ao resultado
            resultado_linhas.append({
                "linha": linha.strip(),
                "status": status_linha,
                "motivo": motivo_linha,
                "contexto_juridico": tem_contexto_juridico,
                "tem_solicitacao": tem_solicitacao,
                "tem_termo_proibido": tem_termo_proibido,
                "termos_proibidos": termos_proibidos_encontrados,
                "solicitacao": verbos_solicitacao_encontrados
            })

            if tem_solicitacao:
                questionamento_solicitacao_linhas += 1

            questionamento_total_linhas += 1

        # Validação geral
        if invalido:
            validacao = "Esse pedido solicita acesso a informacoes pessoais."
            status = "NÃO"
        else:
            validacao = "Pedido aceitavel !"
            status = "SIM"

        # Cálculos finais
        if questionamento_total_linhas > 0:
            criticidade = criticidade_linhas_pessoal * criticidade_verbos_solicitacao * criticidade_palavras_proibidas
            questionamento = questionamento_solicitacao_linhas / questionamento_total_linhas
            pessoalidade = criticidade_palavras_proibidas / questionamento_total_linhas
        else:
            criticidade = 0
            questionamento = 0
            pessoalidade = 0

        impessoalidade = 1 - pessoalidade

        indice_final = criticidade * (questionamento + 1) * (pessoalidade + 1)

        criticidade = round(criticidade, 2)
        questionamento = round(questionamento, 2)
        pessoalidade = round(pessoalidade, 2)
        impessoalidade = round(impessoalidade, 2)
        indice_final = round(indice_final, 2)

        """ Calcula o Índice Final robusto conforme a fórmula descrita. """
        # Normalizações para faixa [0,1]
        critnorm = criticidade / (criticidade + 1) if criticidade >= 0 else 0
        persnorm = pessoalidade / (pessoalidade + 1) if pessoalidade >= 0 else 0
        # Log-transformação
        logfactor = math.log(
            (pessoalidade + 1) * (criticidade_verbos_solicitacao + 1) * (criticidade_palavras_proibidas + 1))
        # Índice Final robusto

        indice_comparavel = 0
        if criticidade > 0:
            indice_comparavel = logfactor * (questionamento + 1) * persnorm
        else:
            indice_comparavel = -logfactor * (questionamento + 1) * persnorm

        indice_comparavel = round(indice_comparavel, 4)

        resultado = {
            "Indice": indice_final,
            "Criticidade": criticidade,
            "Questionamento": questionamento,
            "Pessoalidade": pessoalidade,
            "Impessoalidade": impessoalidade,
            "Validacao": validacao,
            "Retorno": texto,
            "Status": status,
            "Linhas": resultado_linhas,
            "Motivo": motivo,
            "Motivo_bloqueou": motivo_bloqueou,
            "Documentos": list(documentos_encontrados)
        }

        #print(resultado)
        return resultado
