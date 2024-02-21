from flask import Blueprint, request, jsonify

ub_routes_bp = Blueprint('ub_routes', __name__)

@ub_routes_bp.route('/ub/perfil', methods=["POST"])
def search_perfil():
    print(request.json)
    return jsonify({ "resp": "ok" }), 200

@ub_routes_bp.route('/ub/atividades', methods=["POST"])
def search_atividades():
    print(request.json)
    return jsonify({ "resp": "ok" }), 200