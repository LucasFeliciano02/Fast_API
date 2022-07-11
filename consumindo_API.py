"""
pip install requests
"""

import requests


retorno = requests.get('http://127.0.0.1:8000/usuario', params={'nome': 'Lucas'})

# print(retorno.json()['mensagem'])
print(retorno.json())
