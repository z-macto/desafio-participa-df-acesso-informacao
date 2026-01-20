from flask import Flask, render_template, request, session
from motor.motor import Motor
from testes.testes import Testes  # importa a classe
from src.backend.rotas.index_routes import index_bp
from src.backend.rotas.teste_routes import teste_bp

app = Flask( 
        __name__, 
        template_folder="web/templates",
        static_folder="web/static" 
)
            
app.secret_key = "{DESAFIO-PARTICIPA-DF-ACESSO-INFORMACAO}" 

app.register_blueprint(index_bp)
app.register_blueprint(teste_bp)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
