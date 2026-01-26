from .juridico import MotorJuridico
from .solicitacoes import Solicitacoes
from .texto import carregar_lista, obter_pasta

class ConfiguracoesMotor:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            # Cria a instância apenas uma vez
            cls._instance = super(ConfiguracoesMotor, cls).__new__(cls)

            # Carregamento único dos dados
            cls._instance.juridico = MotorJuridico()
            cls._instance.termos_sensiveis = carregar_lista(
                obter_pasta("dados/parametros/termos_sensiveis.txt")
            )
            cls._instance.palavras_solicitacao = Solicitacoes().carregar()
            cls._instance.substantivos_solicitacao = carregar_lista(
                obter_pasta("dados/parametros/substantivos_solicitacao.txt")
            )
            cls._instance.expressoes_juridicas_fixas = carregar_lista(
                obter_pasta("dados/parametros/expressoes_juridicas_fixas.txt")
            )
            cls._instance.expressoes_juridicas_conjugaveis = cls._instance.juridico.obter_expressoes_juridicas()
            cls._instance.expressoes_juridicas = cls._instance.juridico.gerar_expressoes_juridicas()

        return cls._instance
