from flask import Blueprint, render_template, request, session
from src.api.microsservico import consultar_resposta, consultar_testes

index_bp = Blueprint("index", __name__)

@index_bp.route("/", methods=["GET", "POST"])
def index():
    resposta = None
    if request.method == "POST":
        texto = request.form.get("entrada", "").strip()
        if texto:
            resposta = consultar_resposta(texto)  # retorna dict

    resumo = consultar_testes("dados/testes")

    return render_template(
        "index.html",
        resposta=resposta,
        ultimos_pedidos=session.get("ultimos_pedidos", []),
        resumo=resumo
    )
