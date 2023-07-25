from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from to_check import to_check

def web_login(mtr,ps):
    chrome_options= Options() 
    chrome_options.headless=True  #Mostrar o webdrive abrindo (False caso queria ver)
    chrome_options.add_argument('--no-sandbox') 
    chrome_options.add_argument('--disable-dev-shm-usage') 
    navegador = webdriver. Chrome (options=chrome_options) 

    navegador.get("https://digital.unibalsas.edu.br/login/index.php")

    resp = to_check.valid_email(mtr)
    if(resp[0] == False and len(mtr) == 8):
        mtr = f"{mtr[0:2]}.{mtr[2:3]}.{mtr[3:8]}"
    else:
        mtr = mtr

    navegador.find_element('xpath', '//*[@id="username"]').send_keys(mtr)
    navegador.find_element('xpath', '//*[@id="password"]').send_keys(ps)
    navegador.find_element('xpath', '//*[@id="loginbtn"]').click()

    return navegador

class ub:
        def ub_atvs(mtr,ps):
            try:
                navegador = web_login(mtr,ps)
                navegador.get("https://digital.unibalsas.edu.br/my/")
                time.sleep(2)

                element = navegador.find_element('xpath', '//*[@id="inst5869"]')
                html_content = element.get_attribute('outerHTML')
                navegador.quit()

                soup = BeautifulSoup(html_content, 'html.parser')
                
                atvs=[]
                atvs_n = []
                atvs_m = []
                atvs_d = []
                atvs_h = []
                atvs_l = []
                
                for i in soup.find_all('small', {"class":"mb-0"}):
                    atvs_m.append(i.text.split("·")[1].strip())
                for i in soup.find_all('h6', {"class":"event-name mb-0 pb-1 text-truncate"}):
                    atvs_n.append(i.text.strip())
                for i in soup.find_all('h5', {"class":"h6 d-inline font-weight-bold px-2"}):
                    atvs_d.append(i.text)
                for i in soup.find_all('small', {"class":"text-right text-nowrap align-self-center ml-1"}):
                    atvs_h.append(i.text.strip())
                for i in soup.find_all('h6', {"class":"event-name mb-0 pb-1 text-truncate"}):
                    atvs_l.append(i.find('a')['href'])

                qtd_atvs = 0
                if len(atvs_m) > 0:
                    for i in range(0,len(atvs_m)):
                        a = {
                            "mat": atvs_m[i],
                            "name": atvs_n[i],
                            "day_week": atvs_d[i].split(",")[0],
                            "date": atvs_d[i].split(",")[1].strip(),
                            "time_limit": atvs_h[i],
                            "link_atv": atvs_l[i]
                        }
                        atvs.append(a)
                        qtd_atvs+=1

                    return {
                        "status": True,
                        "atv": True,
                        "description":f"Há {qtd_atvs} atividade(s) pendente(s)!",
                        "qtd": qtd_atvs,
                        "list": atvs
                        }
                
                return {
                        "status": True,
                        "atv": False,
                        "description":"Não tem atividade pendentes!",
                        "qtd": qtd_atvs,
                        "list":None
                    }
                
            except:
                return {
                    "status":False,
                    "description": "Algo deu Errado!"
                    }
            
        def ub_perfil(mtr,ps):
            try:
                navegador = web_login(mtr,ps)
                navegador.get("https://digital.unibalsas.edu.br/user/profile.php")

                element = navegador.find_element('xpath', '//*[@id="topofscroll"]')
                html_content = element.get_attribute('outerHTML')
                navegador.quit()

                soup = BeautifulSoup(html_content, 'html.parser')

                name = soup.find('h1', {"class":"h2"}).text.strip()

                email = soup.find('li', {"class":"contentnode"}).find('a').text.strip()
                info = []
                for i in soup.find_all('li', {"class":"contentnode"}):
                    info.append(i.find('dd').text.strip())

                return {
                        "status": True,
                        "name": name,
                        "email": email,
                        "cidade": info[1],
                        "fuso_horario": info[2]
                    }
            
            except:
                return {
                        "status":False,
                        "description": "Algo deu Errado!"
                    }

        def ub_mat(mtr,ps):
            try:
                navegador = web_login(mtr,ps)
                    
                element = navegador.find_element('xpath', '//*[@id="frontpage-course-list"]')
                html_content = element.get_attribute('outerHTML')
                navegador.quit()

                soup = BeautifulSoup(html_content, 'html.parser')

                mat=[]
                qtd_mat = 0
                for i in soup.find_all('a', {"class":"aalink"}):
                    a = {
                        "name": (i.text.strip()),
                        "link": (i['href'])
                    }
                    mat.append(a)
                    qtd_mat+=1

                if qtd_mat > 0:
                    return {
                            "status": True,
                            "mat": True,
                            "description":f"Há {qtd_mat} curso(s)!",
                            "qtd": qtd_mat,
                            "list":mat
                        }
                return {
                        "status": True,
                        "mat": False,
                        "description":f"Não tem curso(s)!",
                        "qtd": qtd_mat,
                        "list":None
                        }
            
            except:
                return {
                        "status":False,
                        "description": "Algo deu Errado!"
                    }