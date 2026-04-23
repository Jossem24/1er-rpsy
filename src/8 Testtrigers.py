




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