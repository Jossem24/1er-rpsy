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


#4.9
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



















