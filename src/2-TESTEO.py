print("Joginho das torres")
print("torre A: 5,4,3,2,1" \
" torre B: " \
" torre C: ")
torre_a=[5,4,3,2,1]
torre_b=[]
torre_c = []
torres = {
    "A": torre_a,
    "B": torre_b,
    "C": torre_c       
}   

def mover_disco(origem, destino):
   if not origem:             #primeiro verifica erro e so depois mexe
       return False

   if destino and origem[-1] > destino[-1]:
       return False
    
   disco = origem.pop()       #mexer discos
   destino.append(disco)

   return True

# print(mover_disco(torre_a,torre_b)) #Antes dos outros prints
# print(mover_disco(torre_a,torre_b))
movimentos = 0

while True:

    origem_escolhida= input("Escolha origem: A, B ou C: ").strip().upper()
    destino_escolhido= input("Escolha destino: A, B ou C: ").strip().upper()

    
    if not origem_escolhida or not destino_escolhido:
        print("Não deixe campos vazios")
        continue 
    if origem_escolhida not in torres or destino_escolhido not in torres :
        print("Torre invalida")
        continue 
    origem= torres[origem_escolhida]
    destino=torres[destino_escolhido]



    if mover_disco(origem, destino):
        movimentos= movimentos + 1
        print("Numero de jogadas:", movimentos) 
    if torre_c == [5, 4, 3, 2, 1]:
        print("Voce ganhou")
        break    

    print("Torre A: ",torre_a)              
    print("Torre B: ", torre_b)
    print("Torre C: ", torre_c)