from flask import Flask
from flask_cors import CORS
from src.main.routes.ub_routes import ub_routes_bp

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {
        "status": True,
        "message": "Welcome to the UB API!",
        "version": "3.0v",
        "endpoints": {
            "ub_atv": "/ub/atv",
            "ub_perfil": "/ub/perfil",
        },
        "documentation": "/docs",
        "contact": {
            "email_personal": "pedro.henrique.martins404@gmail.com",
            "email_academic": "pedro.borges@alu.unibalsas.edu.br",
            "github": "piedro404",
            "linkedin": "pedrohenrique404"
        }
    }

app.register_blueprint(ub_routes_bp)



