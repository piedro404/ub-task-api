from src.errors.error_types.http_bad_request import HttpBadRequestError

def request_json_validator(request: any) -> None:
    try:
        request.json
    except:
        raise HttpBadRequestError("Invalid request. Please check your input and try again.")

