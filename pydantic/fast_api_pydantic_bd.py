from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


class Usuario(BaseModel):
    id: int
    nome: str  # Optional[str]
    senha: str

lista = [
    Usuario(id=1, nome='Lucas', senha='senha1'),
    Usuario(id=2, nome='Mateus', senha='senha2'),
    Usuario(id=3, nome='Marcos', senha='senha3')
]  

@app.post('/usuario')
def main(usuario: Usuario):
    lista.append(usuario)
    return "Usuário cadastrado"


@app.get('/usuarioListar')
def main():
    return lista


