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