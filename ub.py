from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from to_check import to_check

def web_login(mtr, ps):
    chrome_options = Options()
    chrome_options.headless = True  # Mostrar o webdrive abrindo (False caso queira ver)
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    navegador = webdriver.Chrome(options=chrome_options)

    navegador.get("https://ead.unibalsas.edu.br/login/index.php")

    resp = to_check.valid_email(mtr)
    if (resp[0] == False and len(mtr) == 8):
        mtr = f"{mtr[0:2]}.{mtr[2:3]}.{mtr[3:8]}"

    navegador.find_element(By.XPATH, '//*[@id="username"]').send_keys(mtr)
    navegador.find_element(By.XPATH, '//*[@id="password"]').send_keys(ps)
    navegador.find_element(By.XPATH, '//*[@id="loginbtn"]').click()

    return navegador

class ub:

    @staticmethod
    def ub_atvs(mtr, ps):
        try:
            navegador = web_login(mtr, ps)
            navegador.get("https://ead.unibalsas.edu.br/calendar/view.php?view=upcoming")
            wait = WebDriverWait(navegador, 10)
            element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.calendarwrapper')))
            html_content = element.get_attribute('outerHTML')
            navegador.quit()
            tarefas = BeautifulSoup(html_content, 'html.parser').find_all('div', class_='details')
            atvs=[]

            for tarefa in tarefas:
                try:
                    nome = tarefa.find('h3').text.strip()
                    link_url = tarefa.find('a', class_='btn')['href']
                    detalhes = tarefa.find_all('li')
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
            navegador = web_login(mtr,ps)
            navegador.get("https://ead.unibalsas.edu.br/user/profile.php")
            wait = WebDriverWait(navegador, 10)
            element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ccn-main"]/div/section/div/div/div[2]/div[1]/div[2]')))
            html_content = element.get_attribute('outerHTML')
            navegador.quit()
            perfil = BeautifulSoup(html_content, 'html.parser').find_all('i')

            nome = f"{perfil[0].text.strip()} {perfil[1].text.strip()}"
            email = perfil[5].text.strip()
            lingua = perfil[2].text.strip()

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

    @staticmethod
    def ub_mat(mtr,ps):
        try:
            navegador = web_login(mtr,ps)
            wait = WebDriverWait(navegador, 10)
            element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-container-0"]/div/div')))
            html_content = element.get_attribute('outerHTML')
            navegador.quit()
            materias = BeautifulSoup(html_content, 'html.parser').find_all('div', class_='mc_content_list')
            mats = []

            for mat in materias:
                try:
                    link_mat = mat.find('div', class_='thumb').find('a', class_='mcc_view')['href']
                    nome = mat.find('div', class_='details').find('h5', class_='title').text.strip()

                    a = {
                        "name": nome,
                        "link": link_mat
                    }
                    mats.append(a)

                except:
                    continue

            return {
                "status": True,
                "mat": len(mats) > 0,
                "description":f"Há {len(mats)} curso(s)!",
                "qtd": len(mats),
                "list": mats
            }
            
        except:
            return {
                "status":False,
                "description": "Algo deu Errado!"
            }