print ("Hola, qual é seu nome? ")
nome = input("")
print("BEM VINDA", nome)
input("Que necesitas? ")
print("Escribe 51")

manguito = 50
numero = int(input("Digite o numero: "))

#se e igual
if manguito == numero :
    print("Pode comer peladito")

#se o digito é 50 ou menos   
elif manguito > numero :
    print("Mangazo")  

#se o digito é maior a 50    
else :
    print("Sigue para el siguiente exercicio")
    

opcao1 = ("1 bisteck")
opcao2 = ("2 Chaufa")
opcao3 = ("3 Ceviche")

while True :

    print("Bem vindo a Arki, atenderemos como voce merece")
    print("Escolha uma das opcoes") 
    print("1: Quero comer")
    print("2: Onde fica o banheiro")
    print("3: Quero para levar") 


    opcao = int(input("Escolha a opcao: "))
          

    if  opcao == 1 :
        print("Temos os seguintes pratos:")
        print(opcao1)
        print(opcao2)
        print(opcao3)
        
        
        prato = int(input("Qual deseja?: "))

        if prato == 1 :
            print("Em que ponto deseja a carne?")
            break
        elif prato == 2 :
            print("De carne ou de frango")
            break
        elif prato == 3 :
            print("Picante ou normal") 
            break

     

        break
    elif opcao == 2 :
        print("Na sua casa")
        break
    elif opcao == 3 :
        print("Enseguida senor")
        break
    else :
        print("Volte pronto, muito obrigado")
        
