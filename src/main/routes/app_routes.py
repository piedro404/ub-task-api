import os
from flask import Blueprint, request, jsonify, send_from_directory

app_routes_bp = Blueprint('app_routes', __name__)

@app_routes_bp.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": True,
        "message": "Welcome to the UB API!",
        "version": "3.0.3v",
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

@app_routes_bp.route('/docs')
def swagger_ui():
    return send_from_directory(os.path.join(app_routes_bp.root_path, '../../templates'),
                          'docs.html')

@app_routes_bp.route('/openapi.json')
def swagger():
    return send_from_directory(os.path.join(app_routes_bp.root_path, '../../templates/documentation'),
                          'openapi.json')

@app_routes_bp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app_routes_bp.root_path, '../../static'),
                          'favicon.ico')
