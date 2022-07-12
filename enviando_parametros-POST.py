from fastapi import FastAPI


app = FastAPI()

# Envia o valor e ve se existe igual
usuarios = [(1, 'Lucas', 'senha1'), (2, 'Mateus', 'senha2')]


@app.post('/usuario')
def main(nome):
    for i in usuarios:
        if i[1] == nome:
            return i
        
    return 'Não existe esse usuário'
