from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from ub import ub

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"], 
    allow_headers=["*"], 
    allow_credentials=True, 
    allow_origins=["*"],
)

@app.get("/")
def home():
    """
    Rota de boas-vindas à API.
    Retorna um JSON com informações sobre a API.
    """
    return {
        "Status": True,
        "Description": "API UB ON!",
        "Version": "2.5v"
    }

@app.get("/ub/atv/{log}&{ps}", tags=["UB","Atividade"])
async def ub_atv(log:str,ps:str):
    """
    Rota para obter informações sobre atividades do UB.
    
    Parâmetros:
        - log (str): O nome de usuário ou login do aluno.
        - ps (str): A senha do aluno.

    Retorna:
        Um JSON contendo informações sobre as atividades.
    """
    try:
        return ub.ub_atvs(log,ps)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/ub/perfil/{log}&{ps}", tags=["UB", "Perfil"])
async def ub_p(log:str,ps:str):
    """
    Rota para obter informações do perfil do aluno.

    Parâmetros:
        - log (str): O nome de usuário ou login do aluno.
        - ps (str): A senha do aluno.

    Retorna:
        Um JSON contendo informações do perfil.
    """
    try:
        return ub.ub_perfil(log,ps)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Executa a API
if __name__ == "__main__":
    uvicorn.run(app)
