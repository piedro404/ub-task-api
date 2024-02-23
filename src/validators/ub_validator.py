from cerberus import Validator
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

'''
    Responsibility for validating HTTP request input
'''

def ub_validator(request: any) -> None:
    body_validator = Validator({
        "login": {"type": "string", "required": True, "empty": False},
        "password": {"type": "string", "required": True, "empty": False}
    })

    response = body_validator.validate(request.json)
    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
