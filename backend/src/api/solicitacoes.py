from flask import jsonify, request

from . import api_bp
from src.persistencia.banco_de_dados import BancoDados

db = BancoDados()

# Rota 1: devolve total de solicitações e número de páginas
@api_bp.route("/api/solicitacoes/info", methods=["GET"])
def info_solicitacoes():
    total = db.contar_solicitacoes()
    total_paginas = db.obter_total_paginas()
    return jsonify({
        "total_solicitacoes": total,
        "total_paginas": total_paginas
    }), 200


# Rota 2: devolve uma página específica de solicitações
@api_bp.route("/api/solicitacoes", methods=["GET"])
def listar_solicitacoes():
    try:
        pagina = int(request.args.get("pagina", 1))
    except ValueError:
        pagina = 1

    solicitacoes = db.obter_solicitacoes_pagina(pagina)
    return jsonify({
        "pagina": pagina,
        "solicitacoes": solicitacoes
    }), 200
