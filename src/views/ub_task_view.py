from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.ub_task_controller import UbTaskController

class UBTaskView:
    
    '''
        Responsability for interacting with HTTP
    '''

    def validate_and_search(self, http_request: HttpRequest) -> HttpResponse:
        ub_task_controller = UbTaskController()
        
        body = http_request.body
        login, password = body['login'], body['password']

        formatted_response = ub_task_controller.task(login, password)

        return HttpResponse(status_code=200, body=formatted_response)

