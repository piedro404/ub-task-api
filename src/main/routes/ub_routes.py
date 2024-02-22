from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.ub_profile_view import UBProfileView

ub_routes_bp = Blueprint('ub_routes', __name__)

@ub_routes_bp.route('/ub/profile', methods=['POST'])
def search_profile():
    ub_profile_view = UBProfileView()
    
    http_request = HttpRequest(body=request.json)
    http_response = ub_profile_view.validate_and_search(http_request)

    return jsonify({"resp": "ok"}), 200

@ub_routes_bp.route('/ub/task', methods=['POST'])
def search_task():
    return jsonify(http_response.body), http_response.status_code
