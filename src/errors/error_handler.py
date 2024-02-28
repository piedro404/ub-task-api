from src.views.http_types.http_response import HttpResponse

# Error Types
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .error_types.http_unauthorized import HttpUnauthorizedError
from .error_types.http_bad_request import HttpBadRequestError

'''
    Responsibility for validating HTTP request input
'''

def error_handler(error: Exception) -> HttpResponse: 
    if isinstance(error, HttpUnprocessableEntityError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "status":False,
                "errors": {
                    "title": error.name,
                    "details": error.message
                }
            }
        )
    
    if isinstance(error, HttpUnauthorizedError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "status":False,
                "errors": {
                    "title": error.name,
                    "details": error.message
                }
            }
        )
    
    if isinstance(error, HttpBadRequestError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "status":False,
                "errors": {
                    "title": error.name,
                    "details": error.message
                }
            }
        )
    
    return HttpResponse(
        status_code=500,
        body={
            "status":False,
            "errors": {
                "title": "Server Error",
                "details": str(error)
            }
        }
    )
