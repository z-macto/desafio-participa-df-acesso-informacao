import json
import re

from .nominal import detectar_substantivo_solicitacao
from .texto import carregar_lista, remover_acentos, tokenizar_linha

from .configuracoes_motor import ConfiguracoesMotor
from ..validadores.cnh import cnh_validar
from ..validadores.cpf import cpf_validar
from ..validadores.sus import sus_validar


class Motor:

    def __init__(self):
        self.config = ConfiguracoesMotor()



    def analisar(self, texto: str) -> dict:
        texto = texto.strip()

        REGEX_CPF = r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b"
        REGEX_RG = r"\b\d{1,2}\.?\d{3}\.?\d{3}-?\d{1}\b"
        REGEX_CNH = r"\b\d{11}\b"
        REGEX_OAB = r"\b\d{4,6}[-/ ]?[A-Z]{2}\b"
        REGEX_SUS = r"\b\d{15}\b"
        REGEX_PROCESSO_SEI = r"\b\d{5}-\d{8}/\d{4}-\d{2}\b"
        REGEX_TELEFONE = r"\(?\d{2}\)?\s?\d{4,5}-?\d{4}\b"
        REGEX_EMAIL = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

        encontrados_processo_sei = set()
        encontrados_cpf = set()
        encontrados_rg = set()
        encontrados_cnh = set()
        encontrados_sus = set()
        encontrados_oab = set()
        encontrados_telefone = set()
        encontrados_email = set()

        linhas_simples = texto.split('\n')

        for linha in linhas_simples:
            linha_cpf = set(re.findall(REGEX_CPF, linha))
            linha_rg = set(re.findall(REGEX_RG, linha))
            linha_cnh = set(re.findall(REGEX_CNH, linha))
            linha_oab = set(re.findall(REGEX_OAB, linha))
            linha_sus = set(re.findall(REGEX_SUS, linha))

            linha_processo_sei = set(re.findall(REGEX_PROCESSO_SEI, linha))
            linha_telefone = set(re.findall(REGEX_TELEFONE, linha))
            linha_email = set(re.findall(REGEX_EMAIL, linha))

            for item in linha_cpf:
                if(cpf_validar(item)):
                    encontrados_cpf.add(item)

            for item in linha_rg:
                encontrados_rg.add(item)

            for item in linha_cnh:
                if(cnh_validar(item)):
                    encontrados_cnh.add(item)

            for item in linha_sus:
                if(sus_validar(item)):
                    encontrados_sus.add(item)

            for item in linha_oab:
                encontrados_oab.add(item)

            for item in linha_processo_sei:
                encontrados_processo_sei.add(item)

            for item in linha_telefone:
                encontrados_telefone.add(item)

            for item in linha_email:
                encontrados_email.add(item)

        #print("--------------------- DOCUMENTOS ---------------------")
        documentos = set()

        documentos = {
            "CPF": list(encontrados_cpf),
            "RG": list(encontrados_rg),
            "CHN": list(encontrados_cnh),
            "SUS": list(encontrados_sus),
            "OAB": list(encontrados_oab),
            "PROCESSO_SEI": list(encontrados_processo_sei),
            "TELEFONE": list(encontrados_telefone),
            "E-MAIL": list(encontrados_email)
        }



        indice_rastreabilidade = 0

        indice_rastreabilidade+=len(encontrados_cpf)
        indice_rastreabilidade+=len(encontrados_rg)
        indice_rastreabilidade+=len(encontrados_processo_sei)
        indice_rastreabilidade+=len(encontrados_telefone)
        indice_rastreabilidade+=len(encontrados_email)

       # print(documentos)

        linhas = texto.split(".")
        linhas = [linha.strip() for linha in linhas if linha.strip()]
        resultado_linhas = []
        invalido = False
        motivo = None
        motivo_bloqueou = []

        criticidade_linhas_pessoal = 0
        criticidade_verbos_solicitacao = 0
        criticidade_termos_sensiveis = 0

        questionamento_solicitacao_linhas = 0
        questionamento_total_linhas = 0

        for linha in linhas:
            tokens = tokenizar_linha(linha)
            linha_normalizada = remover_acentos(linha.lower())

            termos_sensiveis_encontrados = []
            verbos_solicitacao_encontrados = []
            tem_solicitacao = False
            tem_termo_sensivel = False
            tem_contexto_juridico = False

            # Detecta verbos de solicitação
            for p in self.config.palavras_solicitacao:
                if p in tokens:
                    verbos_solicitacao_encontrados.append(p)
                    tem_solicitacao = True

            # Detecta substantivo de solicitação
            substantivo_solicitacao = detectar_substantivo_solicitacao(
                self.config.substantivos_solicitacao, linha_normalizada
            )
            if substantivo_solicitacao:
                verbos_solicitacao_encontrados.append(substantivo_solicitacao)
                tem_solicitacao = True

            # Detecta contexto jurídico
            expressao_juridica = self.config.juridico.detectar_contexto_juridico(linha_normalizada)
            if expressao_juridica:
                tem_contexto_juridico = True

            # Detecta termos proibidos
            termos_sensiveis_encontrados = []
            tem_termo_sensivel = False

            for termo in self.config.termos_sensiveis:
                termo_tokens = termo.split()  # quebra o termo em palavras
                tamanho = len(termo_tokens)

                # caso seja termo de uma palavra
                if tamanho == 1:
                    if termo_tokens[0] in tokens:
                        termos_sensiveis_encontrados.append(termo)
                        tem_termo_sensivel = True
                        criticidade_termos_sensiveis += 1

                # caso seja termo com mais de uma palavra
                else:
                    for i in range(len(tokens) - tamanho + 1):
                        if tokens[i:i + tamanho] == termo_tokens:
                            termos_sensiveis_encontrados.append(termo)
                            tem_termo_sensivel = True
                            criticidade_termos_sensiveis += 1
                            break  # evita duplicar o mesmo termo

            if tem_termo_sensivel:
                criticidade_linhas_pessoal += 1

            # Define status e motivo
            if tem_solicitacao and tem_termo_sensivel:
                invalido = True
                criticidade_verbos_solicitacao += 1
                motivo = (
                    f'Solicitação detectada com termos sensiveis: {", ".join(termos_sensiveis_encontrados)}'
                )
                motivo_bloqueou.append({
                    "expressao": verbos_solicitacao_encontrados or expressao_juridica,
                    "termo_invalido": termos_sensiveis_encontrados,
                    "posicao": linha_normalizada.find(
                        verbos_solicitacao_encontrados[0] if verbos_solicitacao_encontrados else ""
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
                "tem_termo_sensivel": tem_termo_sensivel,
                "termos_sensiveis": termos_sensiveis_encontrados,
                "solicitacao": verbos_solicitacao_encontrados
            })

            if tem_solicitacao:
                questionamento_solicitacao_linhas += 1

            questionamento_total_linhas += 1

        # Validação geral
        if invalido:
            validacao = "Esse pedido solicita acesso a informacoes pessoais."
            status = "NAO"
        else:
            validacao = "Pedido aceitavel !"
            status = "SIM"

        # Cálculos finais
        criticidade = criticidade_linhas_pessoal * criticidade_verbos_solicitacao * criticidade_termos_sensiveis
        questionamento = questionamento_solicitacao_linhas / questionamento_total_linhas
        pessoalidade = criticidade_termos_sensiveis / questionamento_total_linhas

      #  print("Linhas Pessoal = ",criticidade_linhas_pessoal)
       # print("Verbos Soliciticao = ",criticidade_verbos_solicitacao)
        #print("Termos Sensiveis = ",criticidade_termos_sensiveis)

        impessoalidade = 1 - pessoalidade

        indice_final = criticidade * (questionamento + 1) * (pessoalidade + 1)

        criticidade = round(criticidade, 2)
        questionamento = round(questionamento, 2)
        pessoalidade = round(pessoalidade, 2)
        impessoalidade = round(impessoalidade, 2)
        indice_final = round(indice_final, 2)

        resultado = {
            "Mensagem":texto,
            "Indice": indice_final,
            "Criticidade": criticidade,
            "Questionamento": questionamento,
            "Pessoalidade": pessoalidade,
            "Impessoalidade": impessoalidade,
            "Rastreabilidade":indice_rastreabilidade,
            "Validacao": validacao,
            "Retorno": texto,
            "Status": status,
            "Linhas": resultado_linhas,
            "Documentos":documentos,
            "Motivo": motivo,
            "Motivo_bloqueou": motivo_bloqueou
        }

       # print(resultado)
        return resultado
