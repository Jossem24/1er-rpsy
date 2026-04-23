def saudacao(nome):
 return nome
chamado = saudacao("jose")
print("Olá ", chamado)


def area_retangulo(largura, altura):
    return largura * altura
resultado = area_retangulo(4, 5)
print(resultado)


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

def contar():
     numeros = (1, 2, 3, 4, 5)
     return (1, 2, 3, 4, 5)



