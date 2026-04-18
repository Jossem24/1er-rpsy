#primer intento meu de funcoes


def validar_numero():
    try:
        return int(input("Digite o numero: "))
    except:
        print("Entrada Inválida")
        return None
    

def verificar_manguito(numero):
    manguito = 50

    if numero is None:
        return


    if numero == manguito:
        print("Pode comer manguito peladito")
    elif numero < manguito:
        print("Mangazo")
    else:
        print("Sigue para el siguiente exercicio")


def menu_restaurante():
    while True:
        print("\nBem vindo a Arki")
        print("1: Quero comer")
        print("2: Onde fica o banheiro")
        print("3: Quero para levar")

        opcao = validar_numero()

        if opcao ==  1:
            escolher_prato()
            break
        elif opcao == 2:
            print("Na sua casa")
            break
        elif opcao == 3:
            print("Enseguida senor")
        else:
            print("Opção invalida")   


def escolher_prato():
    print("\nTemos:")
    print("1: Bisteck")
    print("2: Chaufa")
    print("3: Ceviche")

    prato = validar_numero()

    if prato == 1:
        print("Em que ponto deseja a carne?")
    elif prato == 2:
        print("De carne ou de frango?")
    elif prato == 3:
        print("Picante ou normal?")
    else:
        print("Parto invalido:")    


def inicio():
    print("Hola, qual é seu nome?")
    nome = input()
    print("BEM VINDA", nome)

    input("O que precisa? ")

    print("Escribe 51")
    numero = validar_numero()
    verificar_manguito(numero)

    menu_restaurante()


inicio()




