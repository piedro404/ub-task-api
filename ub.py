import requests
from bs4 import BeautifulSoup
from to_check import to_check

def web_login(mtr, ps):
    login_url = "https://ead.unibalsas.edu.br/login/index.php"
    
    session = requests.Session()

    # Fazer o POST do formulário de login
    response = session.get(login_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    token = soup.find('input', {'name': 'logintoken'})['value']

    if(to_check.valid_email(mtr)[0] == False and len(mtr) == 8):
        mtr = f"{mtr[0:2]}.{mtr[2:3]}.{mtr[3:8]}"

    login = {
        'username': mtr,
        'password': ps,
        'logintoken': token
    }

    session.post(login_url, data=login)

    return session

class ub:

    @staticmethod
    def ub_atvs(mtr, ps):
        try:
            session = web_login(mtr, ps)
            response = session.get("https://ead.unibalsas.edu.br/calendar/view.php?view=upcoming")
            tarefas = BeautifulSoup(response.content, 'html.parser').find('div', class_='calendarwrapper').find_all('div', class_='details')

            atvs=[]

            for tarefa in tarefas:
                try:
                    nome = tarefa.find('h3').text.strip()
                    link_url = tarefa.find('a', class_='btn')['href']
                    detalhes = tarefa.find('ul', class_='mb0').find_all('li')
                    dia_semana, data, hora_limite = detalhes[0].text.strip().split(',')
                    materia = detalhes[2].find('a').text.strip()
                    
                    a = {
                        "mat": materia,
                        "name": nome,
                        "day_week": dia_semana,
                        "date": data.strip(),
                        "time_limit": hora_limite.strip(),
                        "link_atv": link_url
                    }
                    atvs.append(a)

                except:
                    continue
            
            session.close()

            return {
                "status": True,
                "atv": len(atvs) > 0,
                "description":f"Há {len(atvs)} atividade(s) pendente(s)!",
                "qtd": len(atvs),
                "list": atvs
            }

        except:
            return {
                "status":False,
                "description": "Algo deu Errado!"
            }
            
    
    @staticmethod
    def ub_perfil(mtr,ps):
        try:
            session = web_login(mtr, ps)
            response = session.get("https://ead.unibalsas.edu.br/user/profile.php")
            perfil = BeautifulSoup(response.content, 'html.parser').find('div', class_='selected_filter_widget siderbar_contact_widget style2 mb30').find_all('i')
            
            nome = f"{perfil[0].text.strip()} {perfil[1].text.strip()}"
            email = perfil[5].text.strip()
            lingua = perfil[2].text.strip()

            session.close()

            return {
                "status": True,
                "name": nome,
                "email": email,
                "language": lingua
            }

        except:
            return {
                "status":False,
                "description": "Algo deu Errado!"
            }