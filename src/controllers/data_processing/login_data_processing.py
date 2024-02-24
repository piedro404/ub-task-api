import re

def __email_validator(email) -> bool:
    default_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if re.match(default_email, email):
        return True
    else:
        return False
    
def login_data_processing(login) -> str:
    if(__email_validator(login) == False and len(login) == 8):
        login = f"{login[0:2]}.{login[2:3]}.{login[3:8]}"

    return login
