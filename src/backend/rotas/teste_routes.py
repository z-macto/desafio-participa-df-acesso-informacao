from flask import Blueprint, render_template

from testes.testes import Testes

teste_bp = Blueprint("teste", __name__)


@teste_bp.route("/testes")
def testes_em_massa():
    testes = Testes("dados/testes")
    resumo = testes.executar()
    return render_template("testes.html", resumo=resumo)