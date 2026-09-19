import pygame

pygame.init()

LARGURA = 800
ALTURA = 500

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Torre de hanoi")

relogio = pygame.time.Clock()
executando = True


torres = [
    [5, 4, 3, 2, 1],
    [],
    []
]
torre_selecionada = None
movimientos = 0
posicoes_x = (200, 400, 600)
altura_disco = 32

def mover_disco(origem, destino):
   if not origem:             #primeiro verifica erro e so depois mexe
       return False

   if destino and origem[-1] > destino[-1]:
       return False
    
   disco = origem.pop()       #mexer discos
   destino.append(disco)

   return True

def desenhar_discos():
    for indice_torre, torre in enumerate(torres):  #pelo for torres se repete 3 vezes
        centro_x = posicoes_x[indice_torre]

        for nivel, disco in enumerate(torre):
            largura = 40 + disco * 20
            x = centro_x - largura // 2   #para o disco entra na haste
            y = 420 - (nivel + 1) * altura_disco 


            #desenho do disco
            pygame.draw.rect(
                tela,
                (45,55,75),
                (x,y, largura, altura_disco - 4), #define o tamanho do rectangulo
                border_radius=6, #arredonda cantos
            )   

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
                                   #MOUSEBU indica que o mouse foi clicado
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            indice_clicado = evento.pos[0] // (LARGURA // 3)
            print(indice_clicado)

    tela.fill((15,15,18))
    COR_TORRE = (75,85,105)

    pygame.draw.line(
        tela,
        COR_TORRE,
        (100,420),
        (700,420),
        6,
    ) 

    for x in (200, 400, 600):
        pygame.draw.line(
            tela,
            COR_TORRE,
            (x, 420),
            (x, 180),
            6,
        )
    desenhar_discos()
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
           