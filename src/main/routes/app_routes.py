from flask import Blueprint, request, jsonify

app_routes_bp = Blueprint('app_routes', __name__)

@app_routes_bp.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": True,
        "message": "Welcome to the UB API!",
        "version": "3.0v",
        "endpoints": {
            "home": "/",
            "ub": {
                "ub_profile": "/ub/profile",
                "ub_task": "/ub/task",
            }
        },
        "documentation": "/docs",
        "contact": {
            "email_personal": "pedro.henrique.martins404@gmail.com",
            "email_academic": "pedro.borges@alu.unibalsas.edu.br",
            "github": "piedro404",
            "linkedin": "pedrohenrique404"
        }
    }), 200