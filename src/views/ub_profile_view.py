from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.ub_profile_controller import UbProfileController

class UBProfileView:
    
    '''
        Responsability for interacting with HTTP
    '''

    def validate_and_search(self, http_request: HttpRequest) -> HttpResponse:
        ub_profile_controller = UbProfileController()
        
        body = http_request.body
        login, password = body['login'], body['password']

        formatted_response = ub_profile_controller.profile(login, password)

        return HttpResponse(status_code=200, body=formatted_response)
