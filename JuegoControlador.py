from Carta import Carta
from Mazo import *
import pygame


def main():
    # inicializar pygame
    pygame.init()
    # inicializar pantalla de py game
    screen = pygame.display.set_mode([1000, 700])
    # runnig es variable que mantiene el game loop activo
    running = True
    # inicializar mazo principal
    MazoPrincipal = Mazo(100, 100, 0)
    MazoPrincipal.llenarmazo()
    MazoPrincipal.desordenar()
    # inicializar mazo de corazones
    MazoCorazones = MazoTipo("♥", 350, 100, 0)
    # inicializar mazo de Diamantes
    MazoDiamantes = MazoTipo("♦", 500, 100, 0)
    # inicializar mazo de picas
    MazoPicas = MazoTipo("♠", 650, 100, 0)
    # inicializar mazo de treboles
    MazoTrebol = MazoTipo("♣", 800, 100, 0)
    # self.MazoTrebol.imprimircartas()
    MazoEscalera = []

    for i in range(0, 7):
        MazoEscalera.append(Mazo(100 * i + 300, 250, 25))
        MazoPrincipal.repartirmazo(MazoEscalera[i], i + 1)
        MazoEscalera[i].generate_card_grup_lader()

    MazoPrincipal.generate_card_grup()

    click = False
    listaonclick = []
    listaclickgrup = pygame.sprite.Group()
    MazoSegundario = Mazo(220, 100, 0)
    listaindex = 0
    listaEscalera = False
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
                    if listaonclick:
                        listaEscalera = True
                        break
                    else:
                        listaEscalera = False
                if MazoPrincipal.placeholder.rect.collidepoint(pos):
                    if MazoPrincipal.cartas:
                        carta = MazoPrincipal.popcarta()
                        carta.oculto = False
                        carta.updatevis()
                        MazoSegundario.recibircarta(carta)
                        MazoPrincipal.OcultarTop()
                    else:
                        MazoSegundario.repartirmazo(MazoPrincipal, len(MazoSegundario.cartas))
                        MazoPrincipal.OcultarTop()
                if MazoSegundario.placeholder.rect.collidepoint(pos):
                    if MazoSegundario.cartas:
                        listaonclick.append(MazoSegundario.cartas.pop())
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                click = False
                coliccion = False
                if MazoPicas.colisiona(pos):
                    carta = listaonclick.pop()
                    if not MazoPicas.recibircartatipo(carta):
                        listaonclick.append(carta)
                    else:
                        MazoEscalera[listaindex - 1].MostrarTop()
                    print("Picas")
                elif MazoDiamantes.colisiona(pos):
                    carta = listaonclick.pop()
                    if not MazoDiamantes.recibircartatipo(carta):
                        listaonclick.append(carta)
                    else:
                        MazoEscalera[listaindex - 1].MostrarTop()
                    print("Diamantes")
                elif MazoCorazones.colisiona(pos):
                    carta = listaonclick.pop()
                    if not MazoCorazones.recibircartatipo(carta):
                        listaonclick.append(carta)
                    else:
                        MazoEscalera[listaindex - 1].MostrarTop()
                    print("Corazonas")
                elif MazoTrebol.colisiona(pos):
                    carta = listaonclick.pop()
                    if not MazoTrebol.recibircartatipo(carta):
                        listaonclick.append(carta)
                    else:
                        MazoEscalera[listaindex - 1].MostrarTop()
                    print("Trebol")
                for mazo in MazoEscalera:
                    if mazo.placeholder.rect.collidepoint(pos):
                        listaonclick.reverse()
                        for carta in listaonclick:
                            coliccion = mazo.recibirCartaEscalera(carta)
                        listaonclick.reverse()



                if not coliccion:
                    listaonclick.reverse()
                    for carta in listaonclick:
                        if listaEscalera:
                            MazoEscalera[listaindex - 1].recibircarta(carta)
                            MazoEscalera[listaindex - 1].updateposCartas()
                        else:
                            MazoSegundario.recibircarta(carta)
                else:
                    MazoEscalera[listaindex - 1].chagevis()
                for mazo in MazoEscalera:
                    mazo.updateposCartas()
                listaindex = 0

            if click:
                if event.type == pygame.MOUSEMOTION:
                    x, y = event.pos
                    count = 0
                    for carta in listaonclick:
                        carta.rect.center = [x, y - 25 * count]
                        count += 1

        screen.fill((255, 255, 255))
        listaclickgrup.__init__()
        listaonclick.reverse()
        for carta in listaonclick:
            listaclickgrup.add(carta)
        listaonclick.reverse()
        MazoSegundario.generate_card_grup()
        MazoPrincipal.generate_card_grup()
        MazoPrincipal.grup.draw(screen)
        for i in range(0, 7):
            MazoEscalera[i].generate_card_grup_lader()
            MazoEscalera[i].grup.draw(screen)

        #Genera el grupo de cartas Trebol y las dibuja en pantalla
        MazoTrebol.generate_card_grup()
        MazoTrebol.grup.draw(screen)

        # Genera el grupo de cartas Corazones y las dibuja en pantalla
        MazoCorazones.generate_card_grup()
        MazoCorazones.grup.draw(screen)
        # Genera el grupo de cartas Diamantes y las dibuja en pantalla
        MazoDiamantes.generate_card_grup()
        MazoDiamantes.grup.draw(screen)
        # Genera el grupo de cartas Trebol y las dibuja en pantalla
        MazoPicas.generate_card_grup()
        MazoPicas.grup.draw(screen)
        MazoSegundario.grup.draw(screen)
        listaclickgrup.draw(screen)
        pygame.display.flip()

    pygame.quit()
