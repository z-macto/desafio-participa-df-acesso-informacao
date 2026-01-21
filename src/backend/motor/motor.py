import json

from backend.motor.juridico import MotorJuridico
from backend.motor.nominal import detectar_substantivo_solicitacao
from backend.motor.solicitacoes import Solicitacoes
from backend.motor.texto import carregar_lista, remover_acentos, tokenizar_linha


class Motor:
    def __init__(self,
                 arquivo_termos_sensiveis: str = "dados/parametros/termos_sensiveis.txt",
                 arquivo_expressoes_juridicas_fixas: str = "dados/parametros/expressoes_juridicas_fixas.txt",
                 arquivo_substantivos_solicitacao: str = "dados/parametros/substantivos_solicitacao.txt"):

        # Instância do motor jurídico
        self.juridico = MotorJuridico()

        # Carregamento de listas externas
        self.termos_sensiveis = carregar_lista(arquivo_termos_sensiveis)
        self.palavras_solicitacao = Solicitacoes().carregar()
        self.substantivos_solicitacao = carregar_lista(arquivo_substantivos_solicitacao)
        self.expressoes_juridicas_fixas = carregar_lista(arquivo_expressoes_juridicas_fixas)

        # Expressões jurídicas com verbos conjugáveis
        self.expressoes_juridicas_conjugaveis = self.juridico.obter_expressoes_juridicas()

        # Lista completa de expressões jurídicas
        self.expressoes_juridicas = self.juridico.gerar_expressoes_juridicas()

    def analisar(self, texto: str) -> dict:
        linhas = texto.split(".")
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
            for p in self.palavras_solicitacao:
                if p in tokens:
                    verbos_solicitacao_encontrados.append(p)
                    tem_solicitacao = True

            # Detecta substantivo de solicitação
            substantivo_solicitacao = detectar_substantivo_solicitacao(
                self.substantivos_solicitacao, linha_normalizada
            )
            if substantivo_solicitacao:
                verbos_solicitacao_encontrados.append(substantivo_solicitacao)
                tem_solicitacao = True

            # Detecta contexto jurídico
            expressao_juridica = self.juridico.detectar_contexto_juridico(linha_normalizada)
            if expressao_juridica:
                tem_contexto_juridico = True

            # Detecta termos proibidos
            for token in tokens:
                if token in self.termos_sensiveis:
                    termos_sensiveis_encontrados.append(token)
                    tem_termo_sensivel = True
                    criticidade_termos_sensiveis += 1

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
        if questionamento_total_linhas > 0:
            criticidade = criticidade_linhas_pessoal * criticidade_verbos_solicitacao * criticidade_termos_sensiveis
            questionamento = questionamento_solicitacao_linhas / questionamento_total_linhas
            pessoalidade = criticidade_termos_sensiveis / questionamento_total_linhas
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
            "Motivo_bloqueou": motivo_bloqueou
        }

        print(resultado)
        return resultado
