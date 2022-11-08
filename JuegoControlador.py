from Carta import *
from MazoTipo import *
from MazoEscalera import *
import pygame


def checkwin(mazo1, mazo2, mazo3, mazo4):
    if mazo1.fill() and mazo2.fill and mazo3.fill() and mazo4.fill:
        return True
    else:
        return False


def main():
    Again = False
    # inicializar pygame
    pygame.init()
    # inicializar pantalla de py game
    screen = pygame.display.set_mode([1000, 700])
    # runnig es variable que mantiene el game loop activo
    running = True
    font = pygame.font.SysFont('freesansbold.ttf', 50)
    img = font.render('Jugar otra vez', True, (200, 200, 100), (100, 200, 50))
    jugarotravez = img.get_rect()
    jugarotravez.center = (300, 350)

    font = pygame.font.SysFont('freesansbold.ttf', 50)
    img2 = font.render('Salir', True, (200, 200, 100), (100, 200, 50))
    salir = img.get_rect()
    salir.center = (700, 350)

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
    mazo_escalera = []

    for i in range(0, 7):
        mazo_escalera.append(MazoEscalera(100 * i + 300, 250, 25))
        MazoPrincipal.repartirmazo(mazo_escalera[i], i + 1)
        mazo_escalera[i].generate_card_grup_lader()

    MazoPrincipal.generate_card_grup()

    click = False
    listaonclick = []
    listaclickgrup = pygame.sprite.Group()
    MazoSegundario = Mazo(220, 100, 0)
    listaindex = 0
    listaEscalera = False
    Mazo_picas = False
    Mazo_corazones = False
    Mazo_diamantes = False
    Mazo_trebol = False
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # on click
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                pos = pygame.mouse.get_pos()
                for mazo in mazo_escalera:
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
                if MazoPicas.colisiona(pos):
                    if MazoPicas.cartas:
                        listaonclick.append(MazoPicas.popcarta())
                        Mazo_picas = True

                elif MazoDiamantes.colisiona(pos):
                    if MazoDiamantes.cartas:
                        listaonclick.append(MazoDiamantes.popcarta())
                        Mazo_diamantes = True
                elif MazoCorazones.colisiona(pos):
                    if MazoCorazones.cartas:
                        listaonclick.append(MazoCorazones.popcarta())
                        Mazo_corazones = True

                elif MazoTrebol.colisiona(pos):
                    if MazoTrebol.cartas:
                        listaonclick.append(MazoTrebol.popcarta())
                        Mazo_trebol = True

            # on click realise
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                click = False
                coliccion = False
                if MazoPicas.colisiona(pos):
                    if listaonclick:
                        carta = listaonclick.pop()
                        if not MazoPicas.recibircartatipo(carta):
                            listaonclick.append(carta)
                        else:
                            mazo_escalera[listaindex - 1].MostrarTop()

                elif MazoDiamantes.colisiona(pos):
                    if listaonclick:
                        carta = listaonclick.pop()
                        if not MazoDiamantes.recibircartatipo(carta):
                            listaonclick.append(carta)
                        else:
                            mazo_escalera[listaindex - 1].MostrarTop()

                elif MazoCorazones.colisiona(pos):
                    if listaonclick:
                        carta = listaonclick.pop()
                        if not MazoCorazones.recibircartatipo(carta):
                            listaonclick.append(carta)
                        else:
                            mazo_escalera[listaindex - 1].MostrarTop()

                elif MazoTrebol.colisiona(pos):
                    if listaonclick:
                        carta = listaonclick.pop()
                        if not MazoTrebol.recibircartatipo(carta):
                            listaonclick.append(carta)
                        else:
                            mazo_escalera[listaindex - 1].MostrarTop()

                for mazo in mazo_escalera:

                    if mazo.placeholder.rect.collidepoint(pos):
                        listaonclick.reverse()
                        for carta in listaonclick:
                            coliccion = mazo.recibirCartaEscalera(carta)
                        listaonclick.reverse()

                if not coliccion:
                    listaonclick.reverse()
                    for carta in listaonclick:
                        if listaEscalera:
                            mazo_escalera[listaindex - 1].recibircarta(carta)
                            mazo_escalera[listaindex - 1].updateposCartas()
                        elif Mazo_picas:
                            MazoPicas.recibircartatipo(listaonclick.pop())
                        elif Mazo_corazones:
                            MazoCorazones.recibircartatipo(listaonclick.pop())
                        elif Mazo_trebol:
                            MazoTrebol.recibircartatipo(listaonclick.pop())
                        elif Mazo_diamantes:
                            MazoDiamantes.recibircartatipo(listaonclick.pop())
                        else:
                            MazoSegundario.recibircarta(carta)
                else:
                    mazo_escalera[listaindex - 1].chagevis()
                for mazo in mazo_escalera:
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
            mazo_escalera[i].generate_card_grup_lader()
            mazo_escalera[i].grup.draw(screen)

        # Genera el grupo de cartas Trebol y las dibuja en pantalla
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

        if checkwin(MazoDiamantes, MazoTrebol, MazoCorazones, MazoPicas):
            screen.blit(img, jugarotravez)
            screen.blit(img2, salir)
            pos = pygame.mouse.get_pos()
            if salir.collidepoint(pos):
                running = False
            elif jugarotravez.collidepoint(pos):
                running = False
                Again = True
        pygame.display.flip()

    pygame.quit()
    if Again:
        main()
