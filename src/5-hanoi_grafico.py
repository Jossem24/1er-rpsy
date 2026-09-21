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

            cor = (45, 55, 75)

            if (
                indice_torre == torre_selecionada
                and nivel == len(torre) - 1
            ):
                cor = (255, 185, 40)
            #desenho do disco
            pygame.draw.rect(
                tela,
                cor,
                (x,y, largura, altura_disco - 4), #define o tamanho do rectangulo
                border_radius=6, #arredonda cantos
            )   

            texto_numero = fonte.render(
                # str converte numero para texto
                str(disco),
                True,
                (230, 230, 235),
            )
            area_numero = texto_numero.get_rect(
                center=(
                    #calculo para centrar o texto no retangulo do texto
                    centro_x,
                    y + (altura_disco - 4) // 2,
                )
            )    #mostra  o numero
            tela.blit(texto_numero, area_numero)

fonte = pygame.font.Font(None, 28)

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

        #Detectar em que torre clicou o jogador    
                                   #MOUSEBU indica que o mouse foi clicado
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            indice_clicado = evento.pos[0] // (LARGURA // 3)
            if torre_selecionada is None :
                if torres[indice_clicado]:
                    torre_selecionada = indice_clicado
                    print("Origem selecionada: ", torre_selecionada)
            else:
                if indice_clicado != torre_selecionada:
                    if mover_disco(
                        torres[torre_selecionada],
                        torres[indice_clicado],
                    ):
                        movimientos += 1
                        print("Movimentos:", movimientos)
                torre_selecionada = None        
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
    for indice, letra in enumerate (("A", "B", "C")):
        texto_letra = fonte.render(letra, True, (230, 230, 235))
                                 #get_rect cria uma area centralizada e centra a letra na barra(haste)
        area_texto = texto_letra.get_rect(
            center=(posicoes_x[indice], 455)
        )    #blit mostra a letra na area centralizada
        tela.blit(texto_letra, area_texto)
    texto_movimentos = fonte.render(  #render transforma texto em imagem
        f"Movimentos: {movimientos}",
        True,
        (230, 230, 235),
    )
         #blit desenha uma imagem na tela, na posição colocada (20,20)    
    tela.blit(texto_movimentos, (20,20))
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
           