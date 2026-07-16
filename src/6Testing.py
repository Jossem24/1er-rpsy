import requests

resposta = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(resposta.status_code)
print(resposta.json())