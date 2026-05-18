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