import requests

resposta = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(resposta.status_code)
