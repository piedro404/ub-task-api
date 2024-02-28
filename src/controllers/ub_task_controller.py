from typing import Dict
from src.drivers.ub_handler import UBHandler
from .data_processing.login_data_processing import login_data_processing

class UbTaskController:
    
    '''
        Responsability for implementing business rules
    '''

    def task(self, login: str, password: str) -> Dict:
        tasks = self.__search_task(login, password)
        formatted_response = self.__format_response(tasks)

        return formatted_response

    def __search_task(self, login: str, password: str) -> Dict:
        ub_handler = UBHandler()
        login = login_data_processing(login)
        tasks = ub_handler.ub_search_task(login, password)

        return tasks
    
    def __format_response(self, tasks: Dict) -> Dict:
        return {
            "status": True,
            "tasks": {
                "find_task": len(tasks) > 0,
                "description":f"Há {len(tasks)} atividade(s) pendente(s)!",
                "amount_task": len(tasks),
                "list_tasks": tasks
            }
        }
