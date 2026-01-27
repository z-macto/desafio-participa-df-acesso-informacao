import sqlite3
import uuid
from datetime import datetime, timedelta
import math

from src.backend.motor.texto import obter_pasta


class BancoDados:
    def __init__(self, db_path=obter_pasta("../armazenamento_de_dados/banco.db")):
        self.db_path = db_path
        self._criar_tabela()

    def _conectar(self):
        return sqlite3.connect(self.db_path)

    def _criar_tabela(self):
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS solicitacoes (
                id TEXT PRIMARY KEY,
                data TEXT NOT NULL,
                horario TEXT NOT NULL,
                solicitacao TEXT NOT NULL,
                analise TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def inserir_solicitacao(self, conteudo: str, resposta: str):
        conn = self._conectar()
        cursor = conn.cursor()

        try:
            id = uuid.uuid7().hex  # Python 3.11+
        except AttributeError:
            id = uuid.uuid4().hex  # fallback

        agora = datetime.now()
        data = agora.strftime("%Y-%m-%d")
        horario = agora.strftime("%H:%M:%S")

        cursor.execute("""
            INSERT INTO solicitacoes (id, data, horario, solicitacao, analise)
            VALUES (?, ?, ?, ?, ?)
        """, (id, data, horario, conteudo, resposta))

        conn.commit()
        conn.close()
        return id

    def contar_solicitacoes(self) -> int:
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM solicitacoes")
        total = cursor.fetchone()[0]
        conn.close()
        return total

    def obter_total_paginas(self, tamanho_pagina=50) -> int:
        total = self.contar_solicitacoes()
        return math.ceil(total / tamanho_pagina)

    def obter_solicitacoes_pagina(self, pagina: int, tamanho_pagina=50):
        offset = (pagina - 1) * tamanho_pagina
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, data, horario, solicitacao, analise
            FROM solicitacoes
            ORDER BY data DESC, horario DESC
            LIMIT ? OFFSET ?
        """, (tamanho_pagina, offset))
        registros = cursor.fetchall()
        conn.close()

        # transformar em lista de dicts
        resultado = [
            {
                "id": r[0],
                "data": r[1],
                "horario": r[2],
                "solicitacao": r[3],
                "analise": r[4],
            }
            for r in registros
        ]
        return resultado


    def contar_solicitacoes_por_dia(self, dias=30):
        """Retorna a quantidade de solicitações por dia nos últimos `dias`."""
        conn = self._conectar()
        cursor = conn.cursor()

        # Data limite (30 dias atrás)
        limite = (datetime.now() - timedelta(days=dias)).strftime("%Y-%m-%d")

        cursor.execute("""
                       SELECT data, COUNT(*) as total
                       FROM solicitacoes
                       WHERE data >= ?
                       GROUP BY data
                       ORDER BY data ASC
                       """, (limite,))

        registros = cursor.fetchall()
        conn.close()

        # transforma em lista de dicts
        resultado = [
            {"data": r[0], "total": r[1]}
            for r in registros
        ]
        return resultado

    def remover_solicitacoes_antigas(self):
        conn = self._conectar()
        cursor = conn.cursor()

        # Define a data limite
        data_limite = "2026-01-28"

        # Remove registros anteriores à data limite
        cursor.execute("""
            DELETE FROM solicitacoes
            WHERE data < ?
        """, (data_limite,))

        conn.commit()
        conn.close()

    def inserir_solicitacao(self, conteudo: str, resposta: str, data: str, horario: str):
        """
        Insere uma solicitação no banco de dados.

        Parâmetros:
            conteudo (str): Texto da solicitação
            resposta (str): Texto da análise/resposta
            data (str): Data no formato 'YYYY-MM-DD'
            horario (str): Horário no formato 'HH:MM:SS'
        """
        conn = self._conectar()
        cursor = conn.cursor()

        try:
            id = uuid.uuid7().hex  # Python 3.11+
        except AttributeError:
            id = uuid.uuid4().hex  # fallback

        cursor.execute("""
                       INSERT INTO solicitacoes (id, data, horario, solicitacao, analise)
                       VALUES (?, ?, ?, ?, ?)
                       """, (id, data, horario, conteudo, resposta))

        conn.commit()
        conn.close()
        return id
