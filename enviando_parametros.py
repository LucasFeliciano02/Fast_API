from fastapi import FastAPI


app = FastAPI()

# Digitando o id se tem o usuario e a senha
usuarios = [(1, 'Lucas', 'senha1'), (2, 'Mateus', 'senha2')]


@app.get('/usuario/{id}')
def main(id: int):
    for i in usuarios:
        if i[0] == id:
            return i
        
    return 'Não existe esse usuário'
