from Carta import Carta
from Mazo import *
import pygame


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([1000, 700])
    running = True
    # inicializar mazo principal
    MazoPrincipal = Mazo(100, 100, 0)
    MazoPrincipal.llenarmazo()
    MazoPrincipal.imprimircartas()
    MazoPrincipal.desordenar()
    # inicializar mazo de corazones
    MazoCorazones = MazoTipo("♥", 200, 100, 0)
    # inicializar mazo de Diamantes
    MazoDiamantes = MazoTipo("♦", 300, 100, 0)
    # inicializar mazo de picas
    MazoPicas = MazoTipo("♠", 400, 100, 0)
    # inicializar mazo de treboles
    MazoTrebol = MazoTipo("♣", 500, 100, 0)
    # self.MazoTrebol.imprimircartas()
    MazoEscalera = []

    for i in range(0, 7):
        MazoEscalera.append(Mazo(100 * i + 300, 250, 25))
        MazoPrincipal.repartirmazo(MazoEscalera[i], i + 1)
        MazoEscalera[i].generate_card_grup_lader()

    for mazo in MazoEscalera:
        print("")
        mazo.imprimircartas()

    MazoPrincipal.generate_card_grup()

    click = False
    listaonclick = []
    listaindex = 0
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                pos = pygame.mouse.get_pos()
                for mazo in MazoEscalera:
                    listaonclick = mazo.getlistclicked(pos)
                    listaindex += 1
                    if listaonclick: break

            if event.type == pygame.MOUSEBUTTONUP:
                click = False
                listaonclick.reverse()
                for carta in listaonclick:
                    MazoEscalera[listaindex-1].recibircarta(carta)
                    MazoEscalera[listaindex-1].updateposCartas()
                listaindex = 0

            if click:
                if event.type == pygame.MOUSEMOTION:
                    x, y = event.pos
                    count = 0
                    for carta in listaonclick:
                        carta.rect.center = [x, y - 25 * count]
                        count += 1

        screen.fill((255, 255, 255))
        MazoPrincipal.grup.draw(screen)
        for i in range(0, 7):
            MazoEscalera[i].grup.draw(screen)

        pygame.display.flip()

    # Done! Time to quit.

    pygame.quit()
