# V1 Função suma simples
def comeco(j, p):
   return j + p
print(comeco(4, 5))
  

# V2 Função suma com inputs 
def peru_anadas() :
    
 x = int(input())
 y = int(input()) 


 resultado = x + y

 print(resultado)
 return resultado
peru_anadas ()


# V3 Função suma com inputs
def mira_calculo (a, b) :
    return a + b
    
resultado = mira_calculo (int (input()), int (input()))
print (resultado)


#V4 função com try
def creando_try (q, e) :
    try :
      q = 52
      e = 40 
      operação = q + e
      return print(operação)
    except :
       print("Error")
       return None
creando_try (52,40)


#V5 função para obter o numero maior con try e input
def maior():
   
     try :
    
         a = int(input("Digite o primer numero: "))
         b = int(input("Digite o segundo numero: "))
    
         if a > b :

               print("O numero maior é: ", a)
               return a
         elif b > a :
               print("O numero maior é: ", b)
               return b
         else:
               print("Resposta invalida")
     except :
         print("Invalido")   
maior()


#V6 função para escolha 
def escoger():
    samsung = 1
    iphone = 2
    outro = 3

    while True:

            try: 
                
                print("1- Samsung", "2- Iphone", "3-Outro")
                telefono = int(input("Cual es tu movil?"))

                if  telefono == 1 :
                    print("Eres pituco")
                    break
                elif telefono == 2 :
                    print ("Estás en algo")
                    break
                elif telefono == 3:    
                    print("Fuera misio") 
                    break
                else:
                     print("Opcao invalida")
                     
            except ValueError:
                    print("Tenta de novo")
escoger()

#V7 Para multiplicar
num = int(input("Dame un numero: "))
for o in range(1, 11):
    
    print(o, "x", num, "=", num * o )

#V8 Para pedir senha até achar a correta
while pss != 1234:
    print("Senha incorreta")
    print("Digite novamente")
    pss = int(input("Digite sua senha: "))

print("Senha correta")       

