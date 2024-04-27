import requests
from bs4 import BeautifulSoup
from typing import Dict
from src.errors.error_types.http_unauthorized import HttpUnauthorizedError
from datetime import datetime, timedelta

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
            profile_content = BeautifulSoup(response.content, 'html.parser')
            try:
                profile_img = profile_content.find('div', class_='page-header-image mr-2').find('img').attrs['src']
            except:
                profile_img = profile_content.find('div', class_='instructor_thumb text-center').find('img').attrs['src']

            profile_details = profile_content.find('div', class_='selected_filter_widget siderbar_contact_widget style2 mb30').find_all('i')
            profile_name = f"{profile_details[0].text.strip().title()} {profile_details[1].text.strip().title()}".split()
            
        except:
            raise HttpUnauthorizedError("Invalid login credentials. Please check your email and password.")

        profile = {
                "name": " ".join(profile_name),
                "email": profile_details[-1].text.strip(),
                "language": profile_details[2].text.strip(),
                "user_initials": f"{profile_name[0][0]}{profile_name[1][0]}",
                "user_picture": profile_img,
            }

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
                time = details[0].text.strip().split(',')
                if len(time)==3:
                    day_week, date, time_limit = time
                else:
                    day_time = datetime.now()
                    if time[0] != "Hoje":
                        day_time += timedelta(days=1)
                    months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
                    day_week, date, time_limit = time[0], f"{day_time.day} {months[day_time.month -1]}",time[1]
                matter = details[2].find('a').text.strip()
                    
                task = {
                    "matter": matter,
                    "task_name": name,
                    "day_week": day_week,
                    "date": date.strip(),
                    "time_limit": time_limit.strip().replace('  ', ' '),
                    "url_task": url_task
                }
                tasks.append(task)

            except Exception as e:
                print(e)
            
        session.close()

        return tasks
