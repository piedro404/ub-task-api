import requests
from bs4 import BeautifulSoup
from typing import Dict
from src.errors.error_types.http_unauthorized import HttpUnauthorizedError

class UBHandler:
    
    '''
        Responsibility for interaction on the UB Website with Selenium
    '''

    def __init__(self) -> None:
        self.url_login = "https://ead.unibalsas.edu.br/login/index.php"
        self.url_tasks = "https://ead.unibalsas.edu.br/calendar/view.php?view=upcoming"
        self.url_profile = "https://ead.unibalsas.edu.br/user/profile.php"

    def __web_login(self, login: str, password: str) -> requests.Session():
        session = requests.Session()

        response = session.get(self.url_login)
        soup = BeautifulSoup(response.content, 'html.parser')
        token = soup.find('input', {'name': 'logintoken'})['value']

        login = {
            'username': login,
            'password': password,
            'logintoken': token
        }

        session.post(self.url_login, data=login)

        return session
        
    
    def ub_search_profile(self, login: str, password: str) -> Dict:
        try:
            session = self.__web_login(login, password)
            response = session.get(self.url_profile)
            profile_content = BeautifulSoup(response.content, 'html.parser').find('div', class_='selected_filter_widget siderbar_contact_widget style2 mb30').find_all('i')
        
        except:
            raise HttpUnauthorizedError("Invalid login credentials. Please check your email and password.")
        
        profile = []

        profile.append({
                "name": f"{profile_content[0].text.strip().title()} {profile_content[1].text.strip().title()}",
                "email": profile_content[5].text.strip(),
                "language": profile_content[2].text.strip()
            })

        session.close()

        return profile
    
    def ub_search_task(self, login: str, password: str) -> Dict:
        try:
            session = self.__web_login(login, password)
            response = session.get(self.url_tasks)
            tasks_content = BeautifulSoup(response.content, 'html.parser').find('div', class_='calendarwrapper').find_all('div', class_='details')

        except:
            raise HttpUnauthorizedError("Invalid login credentials. Please check your email and password.")

        tasks = []

        for task_content in tasks_content:
            try:
                url_task = task_content.find('a', class_='btn')['href']
                status_task = BeautifulSoup(session.get(url_task).content, 'html.parser').find('div', class_='submissionstatustable').find('td', class_='cell c1 lastcol').text

                if(status_task != "Nenhum envio foi feito ainda"):
                    continue

                name = task_content.find('h3').text.strip()
                details = task_content.find('ul', class_='mb0').find_all('li')
                day_week, date, time_limit = details[0].text.strip().split(',')
                matter = details[2].find('a').text.strip()
                    
                task = {
                    "mat": matter,
                    "name": name,
                    "day_week": day_week,
                    "date": date.strip(),
                    "time_limit": time_limit.strip().replace('  ', ' '),
                    "url_task": url_task
                }
                tasks.append(task)

            except:
                continue
            
        session.close()

        return tasks
