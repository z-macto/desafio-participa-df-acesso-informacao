from flask import Blueprint, render_template
from src.api.microsservico import consultar_testes

teste_bp = Blueprint("teste", __name__)

@teste_bp.route("/testes")
def testes_em_massa():
    # 🔑 agora a consulta vem do microsserviço
    resumo = consultar_testes("dados/testes")
    return render_template("testes.html", resumo=resumo)
