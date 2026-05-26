def quadrado(numero):
    return numero * numero
num = quadrado(5)
print(num)


def aprovado(nota):
    return nota >= 7

usu = int(input("Me da sua nota: "))
fin = aprovado(usu)
print(fin)