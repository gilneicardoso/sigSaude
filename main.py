from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

# Rota Raiz
@app.get("/")
def raiz():
    return {"Ola": "Seja Ben Vindo ao SIGSAUDE"}

# Criar model
class Usuario(BaseModel):
    cartao_sus: int
    email: str
    senha: str

# Criar base de dados

base_de_dados = [
    Usuario(cartao_sus=152813948762394, email="gs4gil@gmail.com", senha="sarah2022"),
    Usuario(cartao_sus=285237410896037, email="hudson.kairo@gmail.com", senha="kh3007")
]

# Rota Get All
@app.get("/usuarios")
def get_todos_os_usuarios():
    return base_de_dados

# Rota Get Id
@app.get("/usuarios/{id_usuario}")
def get_usuario_usando_id(cartao_sus_usuario: int):
    for usuario in base_de_dados:
        if(usuario.cartao_sus == cartao_sus_usuario):
            return usuario
    
    return {"Status": 404, "Mensagem": "Não encontrou usuario"}

# Rota Insere
@app.post("/usuarios")
def insere_usuario(usuario: Usuario):
    # criar regras de negocio
    base_de_dados.append(usuario)
    return usuario
