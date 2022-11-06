from Carta import Carta
from Mazo import *
import pygame
def main():
    # inicializar mazo principal
    MazoPrincipal = Mazo()
    MazoPrincipal.llenarmazo()
    MazoPrincipal.imprimircartas()
    MazoPrincipal.desordenar()
    # inicializar mazo de corazones
    MazoCorazones = MazoTipo("♥")
    # inicializar mazo de Diamantes
    MazoDiamantes = MazoTipo("♦")
    # inicializar mazo de picas
    MazoPicas = MazoTipo("♠")
    # inicializar mazo de treboles
    MazoTrebol = MazoTipo("♣")
    # self.MazoTrebol.imprimircartas()
    MazoEscalera = []
    for i in range(0, 7):
        MazoEscalera.append(Mazo())
        MazoPrincipal.repartirmazo(MazoEscalera[i], i + 1)

    for mazo in MazoEscalera:
        print("")
        mazo.imprimircartas()

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([700, 700])
    running = True
    grup = MazoPrincipal.generate_card_grup()


    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        grup.draw(screen)
        screen.fill((255, 255, 255))
        grup.draw(screen)
        pygame.display.flip()

    # Done! Time to quit.

    pygame.quit()
