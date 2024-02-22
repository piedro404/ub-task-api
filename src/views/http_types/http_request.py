from typing import Dict

class HttpRequest:
    '''
        Responsability for interacting with Request
    '''
    
    def __init__(
            self, 
            header: Dict = None, 
            body: Dict = None, 
            query_params: Dict = None
        ) -> None:
        self.header = header
        self.body = body
        self.query_params = query_params
