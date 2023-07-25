import re

def mult9(mults):
    dep = 0
    for x in range(1,10):
        dep += int(mults[x-1])*x

    if dep%11 == 10:
        return str(0)

    return str(dep%11)

class to_check:
    def valid_password(senha):
        try:
            msg=""
            lenght_e = len(senha) < 8
            digit_e = re.search(r"\d", senha) is None
            symbol_e = re.search(r"\W", senha) is None
            password_ok = not (lenght_e or digit_e or symbol_e)

            if not password_ok:
                if lenght_e:
                    msg="Password too short!"
                elif digit_e:
                    msg="Password must have a digit!"
                else:
                    msg="Password must have symbol!"
                
                return password_ok,msg
        except:
            password_ok = False
            msg = "Error..."

        return password_ok,msg

    def valid_email(email):
        try:
            pe_e = True
            vrf_e = re.search("@", email) is None
            if vrf_e == False:
                email_V = email.split("@")
                if len(email_V[0]) > 0 and len(email_V[1]) > 0:
                    pe_e = False
            
            password_ok = not (vrf_e or pe_e)

            if not password_ok:
                return password_ok,"Email incorrect!"
        except:
            password_ok=False
        return password_ok,""

    def valid_cpf(cpf):
        cpf_r=""
        try:
            for x in range(0,len(cpf)):
                if cpf[x] != "." and cpf[x] != "-":
                    cpf_r += str(cpf[x])

            cpf_N,cpf_I = cpf_r[0:9],cpf_r[9:11]
            i = ""
            mults = cpf_N
            i += mult9(mults)
            mults = (mults[1:9]+i) 
            i += mult9(mults)
            cpf_ok = (cpf_I == i)
        except:
            cpf_ok=False

        if not cpf_ok or (len(cpf_r)>11 and cpf_r !=0):
            return False,"CPF incorrect!"

        return cpf_ok,""

