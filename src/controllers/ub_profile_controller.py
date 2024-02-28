from typing import Dict
from src.drivers.ub_handler import UBHandler
from .data_processing.login_data_processing import login_data_processing

class UbProfileController:
    
    '''
        Responsability for implementing business rules
    '''

    def profile(self, login: str, password: str) -> Dict:
        profile = self.__search_profile(login, password)
        formatted_response = self.__format_response(profile)

        return formatted_response

    def __search_profile(self, login: str, password: str) -> Dict:
        ub_handler = UBHandler()
        login = login_data_processing(login)
        profile = ub_handler.ub_search_profile(login, password)

        return profile
    
    def __format_response(self, profile: Dict) -> Dict:
        return {
            "status": True,
            "profile": profile
        }
