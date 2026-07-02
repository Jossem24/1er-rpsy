#Exercicios Ponto 4

#4.2
nome = input("Qual é seu nome? ")
cidade = input("Onde mora? ")
print("Olá,",nome, "Voce mora em", cidade )

#4.3
numero_1 = int(input("Digite um numero: "))
numero_2 = int(input("Digite outro numero: "))
print("A soma deles é", numero_1 + numero_2)
print("A subs deles é", numero_1 - numero_2)
print("A multiplicação deles é", numero_1 * numero_2)

#4.4
nome_aluno = input("Digite seu nome: ")
print("Olá aluno, ", nome_aluno, "Vamos mostrar suas notas")

nota_1 = int(input("De quanto foi sua primeira nota: "))
nota_2 = int(input("De quanto foi sua segunda nota: "))
media_final = (nota_1 + nota_2) / 2
print("Suas notas foram", nota_1, "e",nota_2)
print("Sua media foi", (nota_1 + nota_2) / 2)
print("Sua media final foi", media_final)


#4.5
n_1 = int(input("Digite um numero: "))
n_2 = int(input("Digite um numero: "))
print(n_1 + n_2)
print(n_1 - n_2)
print(n_1 * n_2)
print(n_1 / n_2)


idade = int(input("Digite sua idade: "))
print(idade >= 18)
print(idade < 18)


doc = input("Tem documento? :").lower()   #lower para se o usuario escrever sim de qualquer jeito
adulto = int(input("Dame tu edad chibolo: "))
print( adulto >= 18 and doc == "sim" )


#4.6
edade = int(input("Qual é a sua idade? :"))
if edade >= 18:
    print("Vocé é maior de edade")
else :
    print("Vocé é menor de edade")

nota = int(input("Qual é a sua nota"))
if nota >= 7:
   print("Aprovado")
else :
   print("Reprovado") 

cali = int(input("Cuanto tirou na prova? : "))
if cali >= 9:
   print("Excelente")
elif cali >= 7 :
   print("Aprovado") 
else :  
   print("Reeprovado")     

4.7 
for a in range(1, 6): 
    print( a )

for b in range(3):
    print("python")

numero = 1
while numero <= 5:
    print(numero)
    numero = numero + 1

#4.8 
for numero in range(1, 6):
    if numero == 4:
       break
       
    print(numero)

for i in range(1, 6):
    if i == 3:
     
     continue  

    print(i)  


for p in range(1, 6):
    if p == 2:
        pass

    print(p)


#4.9  Strings
eu = "jose jose seminario carrion"
print(eu)

pala = "python"
print(pala[0])
print(pala[5])

var = input("Dime una palavra: ")
print(var.lower())
print(var.upper())


#mini projeto de boletim

def cadastro_1():
    while True :
        senha = int(input("Digite sua senha: "))
        if senha == 1234 :
            print("Acceso liberado")
            break
        else :
            print("Digite novamente")        
    return      
cadastro_1() 

def dados_pessoais():

    nome = input("Qual é teu nome: ")
    cidade =input("Em que cidade voce mora: ")
    idade = int(input("Qual é a tua idade: "))
    nota_1 = int(input("Fala sua nota 1: "))
    nota_2 = int(input("Fala sua nota 2: "))
    media_final = int((nota_1 + nota_2) / 2)

    print(nome.lower())
    print(nome.upper())
    print(cidade)
    print(nota_1 + nota_2)
    print((nota_1 + nota_2) / 2)

    if media_final >= 9 :
        print("Excelente") 
        
    elif media_final >= 7:
        print("Aprovado")
    else :
        print("Reprovado")       
            
    if idade >= 18:
        print("Vocé é maior de edade")
    else :
        print("Vocé é menor de idade")     

    return None

dados_pessoais()

for i in range(3):
    print("Fim do boletim")


#4.10  Listas

caramelos = ["tentacion", "globopop", "chisitos"]
print(caramelos)

nomes = ["Luis", "jose", "matteo"]
print(nomes[0], nomes[1], nomes[2])

cores = ["azul", "verde"]
cores.append("morado")
cores[1] = "negro"
print(cores)

#4.13 Sets

nums = {1, 2 , 2, 3, 4, 4, 5}
print(nums)
print(len(nums))



nome_1 = input("Digite um nome: ")
nome_2 = input("Digite um nome diferente: ")
nome_3  = input("Digite um nome diferente: ")

nomes = {nome_1, nome_2, nome_3}
print(nomes)


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a & b)
print(a)
print(b)


#4.14 funcoes 
def mensagem ():
    print("estou aprendendo python")
mensagem() 
mensagem()
def dobro (numero):
    print(numero * 2)
dobro(8)
dobro(10)
def boletim(nome, nota1, nota2):
    media = (nota1 + nota2) / 2
    print(nome)
    print(media)

    if media >= 7:
        print("Aprovado, parabens")
    else:
        print("Reprovado")

boletim("Jose", 8, 6)

#4.15 parametros, retorno e escopo
def triplo(numero):
    return numero * 3

resul = triplo(2) 
print(resul)
def media(nota1, nota2):

    nota1 = int(input("Digite sua primeira nota: "))
    nota2 = int(input("Digite sua primeira nota: "))
    return int((nota1 + nota2)) / 2
resultado = media(0, 0)
print("Seu promedio é", resultado)
def maior_idade(idade):

   print( num >= 18 )
  
num = int(input("Me fala sua idade: "))
maior_idade(0)
print(num)

def dados(nome, idade):
    return nome + " tem " + str(idade) + " anos "

x = input("Me da seu nome: ")
y = int(input("Me sua idade: "))
resultados = dados(x, y)
print(resultados)

#4.16 organização do codigo e reutilização 

def mostrar_nome(nome):
    print("Seu nome é ", nome)

a = input("Qual é seu nome?: ") 
mostrar_nome(a)   

b = input("Qual é seu nome?: ")
mostrar_nome(b)


def mostrar_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    print("Sua media é:", media)

x = int(input("Me da sua primeira nota: "))
y = int(input("Me da sua segunda nota: "))
mostrar_media(x,y)


a = int(input("Me da sua primeira nota:"))
b = int(input("Me da sua segunda nota:"))
mostrar_media(a,b)


def situacao_aluno(nome, nota1, nota2):
    prom =(nota1 + nota2) / 2
    veri = "Aprovado" if prom >= 6 else "Desaprovado"
    print("Seu nome é", nome)
    print("Voce tem de promedio", prom )
    print("Vocé tá", veri)

x = input("Qual é seu nome?: ") 
y = int(input("Me da sua primeira nota: "))
z = int(input("Me da sua segunda nota: ")) 
situacao_aluno(x, y, z)   


a = input("Qual é seu nome?: ") 
b = int(input("Me da sua primeira nota: "))
c = int(input("Me da sua segunda nota: ")) 
situacao_aluno(a, b, c)   

#4.17 try e except 

try:

    num = int(input("Me da un numero: "))
    print("Seu numero é: ", num)
except:

    print("Valor errado")

 
try :

    num_1 = int(input("Me da um numero: "))
    num_2 = int(input("Me da outro numero: "))
    soma = num_1 + num_2
    print("A soma é: ", soma)
except :

    print("Voce digitou errado")             


try:
     


 num_1 = int(input("Me da um numero: "))
 divi = 10 / num_1 
 print("A divisão é: ", divi)

except ZeroDivisionError:
 print("Não se pode digitar por zero")
except:
 print("Não didigitou corretamente")    


#4.18 biblioteca e modulos 

import math #math é um modulo
print(math.sqrt(25)) #da raiz cuadrada

import random
print(random.randint(1, 10)) #mostra um numero ao azar dentro do intervalo


import math
print(math.sqrt(81))

import random
print(random.randint(1, 5))

import math
num = int(input("Me da um numero: "))
print(math.sqrt(num))
print(num * num)


#4.19 From e import

import math
print(math.sqrt(49))

from math import sqrt
print(sqrt(64))

from math import sqrt
num = int(input("Me da um numero: "))
print(sqrt(num))

#4.20 arquivos .txt

arquivo = open("meu_texto.txt", "w")
arquivo.write("Estou aprendendo python")
arquivo.close()

arquivo = open("meu_texto.txt", "r")
lendo = arquivo.read()
print(lendo)
arquivo.close()


nome = input("Me da seu nome: ")
arquivo = open("nome.txt", "w")
arquivo.write(nome)
arquivo.close()

arquivo = open("nome.txt", "r")
mostra = arquivo.read()
print(mostra)
arquivo.close()

#4.21 strings, listas e diccionarios

pessoa = {"nome": "Jose", "idade": 20}
print(pessoa.keys()) #keys mostra chaves (nomes)
print(pessoa.values()) #mostra valores (cantidades)


texto = "PapAriLo"
print(texto.upper())
print(texto.lower())


mercado = ["maca", "naranja", "banana"]
mercado.append("mamao")
mercado.remove("banana")
print(mercado)


nomes = { "nome" : "jose", "idade" : 19, "cidade" : "chiclayo" }
print(nomes.keys())
print(nomes.values())


#4.22 list compreshion

uno = []
for i in range (1, 6):
 uno.append(i)
print(uno)

dos = []
for i in range (1, 6):
 dos.append(i * 2)
print(dos)

tres = []
for i in range (1, 7):
    tres.append(i * i)
print(tres)  

#4.23 list, map, filter
uno = lambda x : x + 10
print(uno(5))

dos = [ 4 , 6 ,7, 8, 37]
tres = list(map(lambda y : y * 3, dos))
print(tres)

cuatro = [1, 2, 3, 4, 5, 6] #lista
cinco = list(filter(lambda z : z >3, cuatro)) #da lista, mostra valores maiores do que 3
print(cinco)

#4.24 datas, hora e uso de datetime

from datetime import datetime
uno = datetime.now()
print(uno)

from datetime import datetime
dos = datetime.now()
print(dos.day)
print(dos.month)
print(dos.year)

from datetime import datetime
tres = datetime.now()
print(tres.hour)
print(tres.minute)

#4.25 classes e obj

class Pessoa:
    pass
aluno = Pessoa()
class Carro:
    pass
meu_carro = Carro()
print(meu_carro)

class Animal:
    pass
gato = Animal()
class Casa:
    pass
lar = Casa()



#4.26 metodos, atributos
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

#4.27 Heranca e encapsulamento
class Animal :
    def som(self):
        print("Faz um som")
class Cachorro(Animal):
    pass
sonido = Cachorro() #não faz necessidade de chamar a classe cachorro com (Animal), só basta ()
sonido.som()

class Pessoa :
    def __init__(self, nome) :
        self._nome = nome
uno = Pessoa("Juan")
print(uno._nome)

class Vehiculo :
    def andar (self):
        print("O vehiculo está andando")
class Moto(Vehiculo) :
    pass
dos = Moto()
dos.andar()