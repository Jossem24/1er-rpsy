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