class HttpBadRequestError(Exception):
    
    '''
        Responsibility for Bad Request HTTP Error
    '''

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "Bad Request"
        self.status_code = 400
