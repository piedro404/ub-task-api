class HttpUnauthorizedError(Exception):
    
    '''
        Responsibility for Unauthorized HTTP Error
    '''

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "Unauthorized"
        self.status_code = 401
