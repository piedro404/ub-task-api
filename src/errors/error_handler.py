from src.views.http_types.http_response import HttpResponse

def error_handler(error: Exception) -> HttpResponse: 
    return HttpResponse(
        status_code=500,
        body={
            "status":False,
            "errors": [{
                "title": "Server Error",
                "details": str(error)
            }]
        }
    )

