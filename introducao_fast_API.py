"""
pip install fastapi

servidor usado pela fast_api  =  uvicorn introducao_fast_API:app --reload


uvicorn teste:app --reload  =  Terminal


/docs  =  Admin do FastAPI

"""

from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def root():
    return {'mensagem': 'Olá mundo'}


@app.get('/cadastro')
def cadastro():
    return {'mensagem': 'cadastro'}


@app.get('/login')
def login():
    return {'mensagem': 'login'}
