import requests



resposta = requests.get("https://jsonplaceholder.typicode.com/todos/1")

dados = resposta.json()




print(dados["title"]) 

