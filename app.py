from flask import Flask, render_template, request, session
from src.lai_analisador import LaiAnalisador
from testes.testes import Testes  # importa a classe

app = Flask(__name__)
app.secret_key = "chave-secreta"  # Necessário para usar sessão

@app.route("/", methods=["GET", "POST"])
def index():
    if "ultimos_pedidos" not in session:
        session["ultimos_pedidos"] = []

    resposta = None
    if request.method == "POST":
        texto = request.form.get("entrada")
        analisador = LaiAnalisador()
        resposta = analisador.analisar(texto)

        # adiciona pedido com status
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

# 🚀 Nova rota para página de testes
@app.route("/testes")
def testes_em_massa():
    testes = Testes("dados/testes")
    resumo = testes.executar()
    return render_template("testes.html", resumo=resumo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
