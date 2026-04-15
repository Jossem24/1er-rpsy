def validar_numero(): 
    try: #------------------------------- -------Diz ao programa que rode isso (serve em caso achar que vai dar erro)
        return int(input("Digite o numero: "))
    except:                                      #Se tentou-se o try e não funcionou, este comando em vez de dar erro no programa, da erro em forma de informação ao usuario
        print("Entrada Inválida")                #Dizendo que é uma entrada invalida e manda para a seguinte def/função
        return None                              #return é para encerrar função e passar a seguinte      

                                                  



def validar_numero1(): #--------------------------Crie uma funçaõ para a sumplantar ao def 0 para que ao digitar uma reposta não esperada, volte a perguntar até que 
    while True:        #--------------------------Loop infinito (pelo true) com isto se pode repeter uma entrada no caso o usuario digite algo que não é valido                                                                                       #loop de repetição, oposto a return
        try:
          return int(input("Digite o numero:"))#--Return faz sair do loop
        except:
            print("Entrada invalida, tenta de novo")
                                                  #Resumo: A função (def), pede tentar(try) que o usuario digite uma opçao, se digitar algo invalido se executa a excepção (except) 
                                                  #A diferença com o primer def é o while true, o qual faz repeter até o usuario digitar algo NÃO errado


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

        opcao = validar_numero1()

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

    prato = validar_numero1()

    if prato == 1:
        print("Em que ponto deseja a carne?")
    elif prato == 2:
        print("De carne ou de frango?")
    elif prato == 3:
        print("Picante ou normal?")
    else:
        print("Parto invalido:")    


def inicio():                           #Começo do codigo para o usuario, isto leva aos demais defs
    print("Hola, qual é seu nome?")     #É tambem chamado 0
    nome = input()                      #É preciso criar a variavel nome para depois colocar o nome ao lado de BEM VINDO
    print("BEM VINDA", nome)

    input("O que precisa? ")            #Ao usuario responder a pergunta, igualmente segue o fluxo que leva ao restaurante, corregir depois

    print("Si necesitas comer pide un numero")                 #Ao usuario digitar 51, independentemente do que digite, vai levar ao menu do restaurante
    numero = validar_numero1()           #Aqui CHAMAse em ordem 1 a def/função de validar_numero1 (menu)
    verificar_manguito(numero)          #Aqui chamase em ordem 2 a def/função de verificarmanguito

    menu_restaurante()                  #Aqui chamase em ordem 3 a def/função menu restaurante


inicio()                                #Isto faz com que o programa comece a rodar, porque ta chamado a def/função 0
