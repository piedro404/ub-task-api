from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

#Arquivo PY externo com as funcoes
from ub import ub

# Criando o Ambiente da API
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"], 
    allow_headers=["*"], 
    allow_credentials=True, 
    allow_origins=["*"],
)

# Caminhos da Api
@app.get("/")
def home():
    return {
        "Status": True,
        "Description": "API UB ON!",
        "Version": "2.0v"
    }

@app.get("/ub/atv/{log}&{ps}", tags=["UB","Atividade"])
async def ub_atv(log:str,ps:str):
    return ub.ub_atvs(log,ps)

@app.get("/ub/perfil/{log}&{ps}", tags=["UB", "Perfil"])
async def ub_p(log:str,ps:str):
    return ub.ub_perfil(log,ps)

@app.get("/ub/mat/{log}&{ps}", tags=["UB", "Cursos"])
async def ub_m(log:str,ps:str):
    return ub.ub_mat(log,ps)


#Execulta a Api
uvicorn.run(app)

