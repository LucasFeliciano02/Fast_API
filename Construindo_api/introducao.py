# pip install fastapi
# pip install unicorn  =  Hospedagem dentro do pc para que funcione ("servidor local")
# Roda o server:  uvicorn main:app --reload
# dar cd nome da pasta e dps rodar
# http://127.0.0.1:8000/docs  =  Documentação criada automatica de como a api esta funcionando, try out simula uma requisição para seu endereço

from fastapi import FastAPI


app = FastAPI()

vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa 2L", "preco_unitario": 15, "quantidade": 5},
    3: {"item": "garrafa 750ml", "preco_unitario": 10, "quantidade": 5},
    4: {"item": "lata mini", "preco_unitario": 2, "quantidade": 5},
}


# Rota 1: mostra o total devendas
@app.get("/")
def home():
    return {"vendas": len(vendas)}


# Rota 2: Mostra uma venda específica

@app.get("/vendas/{id_venda}")  # Decorator que atribui uma funcionalidade nova para a função abaixo quando estiver nesse link
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {"Erro": "ID da Venda inexistente"}
