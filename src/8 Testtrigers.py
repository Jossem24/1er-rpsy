def peru_anadas() :
    try: 

        x = int(input("Digite numero: "))
        y = int(input("Digite o outro numero: ")) 
        resultado = x + y
        print(resultado)            
        return resultado
   
    except: 
        print("Erro")
        return None



peru_anadas()

