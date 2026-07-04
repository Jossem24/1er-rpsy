import json

humano = {

    "nome" : "jose",
    "idade" : 22
}


with open ("humano.json", "w") as caixa:
    json.dump(humano, caixa) 

with open ("humano.json", "r") as caixa:
    dados = json.load(caixa)
    print(dados)