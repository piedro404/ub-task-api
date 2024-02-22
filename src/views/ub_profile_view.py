from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class UBProfileView:
    '''
        Responsability for interacting with HTTP
    '''

    def validate_and_search(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        login, password = body['login'], body['password']

        return HttpResponse(status_code=200, body={"resp": "ok"})
