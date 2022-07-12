from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Usuario(BaseModel):
    id: int
    nome: str
    senha: str
    

@app.post('/usuario')
def main(usuario: Usuario):
    return usuario
