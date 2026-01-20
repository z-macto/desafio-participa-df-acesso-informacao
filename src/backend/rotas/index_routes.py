from flask import Blueprint, render_template, request, session
from motor.motor import Motor

# cria blueprint
index_bp = Blueprint("index", __name__)

@index_bp.route("/", methods=["GET", "POST"])
def index():
    if "ultimos_pedidos" not in session:
        session["ultimos_pedidos"] = []

    if request.method == "POST":
        texto = request.form.get("entrada", "").strip()

        if not texto:
            return render_template(
                "index.html",
                ultimos_pedidos=session.get("ultimos_pedidos", [])
            )

        analisador = Motor()
        resposta = analisador.analisar(texto)

        pedidos = session["ultimos_pedidos"]
        pedidos.insert(0, {
            "texto": texto,
            "status": resposta.get("Status", "NAO")
        })
        session["ultimos_pedidos"] = pedidos[:5]

        return render_template(
            "index.html",
            resposta=resposta,
            ultimos_pedidos=session.get("ultimos_pedidos", [])
        )

    return render_template(
        "index.html",
        ultimos_pedidos=session.get("ultimos_pedidos", [])
    )
