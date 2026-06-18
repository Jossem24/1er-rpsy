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
