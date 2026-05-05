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

    nome = input("Qual é teu nome: ").lower()
    cidade =input("Em que cidade voce mora: ")
    idade =input("Qual é a tua idade: ")
    nota_1 = int(input("Fala sua nota 1: "))
    nota_2 = int(input("Fala sua nota 2: "))
    media_final = int((nota_1 + nota_2) / 2)

    print(nome)
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
            
    return None

dados_pessoais()
