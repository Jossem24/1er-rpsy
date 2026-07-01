class Pessoa:
    def __init__(self, nome):
        self.sdfd = nome

aluno = Pessoa("Jose")#aluno é a referença do objeto, pessoa("jose")é o que cria o objt na memoria
print(aluno.sdfd) 

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("Ola, meu nome e", self.nome)

aluno = Pessoa("Jose")
aluno.falar()





class pessoa:
    def __init__(self, nome):
        self.nome = nome
loco = pessoa("Carrion")        
print(loco.nome) #loco é o objeto e .nome o atributo    
        

class carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano        
uno = carro("toyota", "2009")
print(uno.marca)
print(uno.ano)        



class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    def mostrar(self):
        print("Teu nome é:", self.nome)
        print("Tua nota é:", self.nota)
cinco = Aluno("jose", "18")
Aluno.mostrar(cinco)         
