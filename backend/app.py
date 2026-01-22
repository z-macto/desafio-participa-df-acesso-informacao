

from flask import Flask, send_from_directory

from src.api import api_bp
from src.backend.rotas.teste_routes import teste_bp

app = Flask(__name__, static_folder="../distribuicao", static_url_path="")
app.secret_key = "{DESAFIO-PARTICIPA-DF-ACESSO-INFORMACAO}"

app.register_blueprint(teste_bp)
app.register_blueprint(api_bp)


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
