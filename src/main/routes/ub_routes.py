from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest

# Views the Routes
from src.views.ub_profile_view import UBProfileView
from src.views.ub_task_view import UBTaskView

# Errors
from src.errors.error_handler import error_handler

# Validator
from src.validators.ub_validator import ub_validator

ub_routes_bp = Blueprint('ub_routes', __name__)

@ub_routes_bp.route('/ub/profile', methods=['POST'])
def search_profile():
    http_response = None

    try:
        ub_validator(request)
        ub_profile_view = UBProfileView()
        
        http_request = HttpRequest(body=request.json)
        http_response = ub_profile_view.validate_and_search(http_request)
    
    except Exception as exception:
        http_response = error_handler(exception)

    return jsonify(http_response.body), http_response.status_code

@ub_routes_bp.route('/ub/task', methods=['POST'])
def search_task():
    http_response = None

    try:
        ub_validator(request)
        ub_task_view = UBTaskView()
        
        http_request = HttpRequest(body=request.json)
        http_response = ub_task_view.validate_and_search(http_request)
    
    except Exception as exception:
        http_response = error_handler(exception)

    return jsonify(http_response.body), http_response.status_code
