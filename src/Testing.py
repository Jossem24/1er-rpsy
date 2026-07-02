# class Pessoa:  #Clase base
#     def falar (self): #metodo falar
#         print("Ola")
# class Aluno(Pessoa): #Aluno hereda Pessoa
#     pass
# a = Aluno()
# a.falar()

# class Conta:
#     def __init__(self, saldo):
#         self._saldo = saldo  # o _ avisa que é interno, privado, isso é encapsulamento




class Animal :
    def som(self):
        print("Faz um som")

class Cachorro(Animal):
    pass

sonido = Cachorro() #não faz necessidade de chamar a classe cachorro com (Animal), só basta ()
sonido.som()


class Pessoa :
    def __init__(self, nome) :
        self._nome = nome
uno = Pessoa("Juan")
print(uno._nome)


class Vehiculo :
    def andar (self):
        print("O vehiculo está andando")

class Moto(Vehiculo) :
    pass

dos = Moto()
dos.andar()
