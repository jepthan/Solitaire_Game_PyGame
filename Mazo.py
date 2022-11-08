import time

import pygame

from Carta import Carta
import random


class Mazo:
    def __init__(self, posx, posy, offset):
        self.cartas = []
        self.posx = posx
        self.posy = posy
        self.offset = offset
        self.grup = pygame.sprite.Group()
        self.placeholder = pygame.sprite.Sprite()

    def generate_card_grup(self) -> pygame.sprite.Group:
        self.grup = pygame.sprite.Group()
        self.grup.__init__()
        self.placeholder.__init__()
        img = pygame.Surface([98, 135])
        img.fill((200, 200, 200))
        self.placeholder.image = img
        self.placeholder.rect = img.get_rect()
        self.placeholder.rect.center = [self.posx, self.posy]
        self.grup.add(self.placeholder)

        for x in self.cartas:
            x.rect.center = [self.posx, self.posy]
            self.grup.add(x)
        return self.grup


    def updateposCartas(self):
        i = 0
        for x in self.cartas:
            x.rect.center = [self.posx, self.posy + self.offset * i]
            i += 1

    def llenarmazo(self):
        self.inittipo("♣", 1, 4)
        self.inittipo("♦", 2, 4)
        self.inittipo("♠", 3, 4)
        self.inittipo("♥", 4, 4)

    def repartirmazo(self, mazo, cantidad: int):
        for x in range(0, cantidad):
            # print("index", x)
            mazo.cartas.append(self.cartas.pop())
        temp = mazo.cartas.pop()
        temp.oculto = False
        temp.updatevis()
        mazo.cartas.append(temp)

    def inittipo(self, _simbolo, offset: int, off2: int):
        for i in range(1, 14):
            pos = ((i - 1) * off2) + offset  # calcula el nombre de la imagen
            path = f'Imagenes/({str(pos)}).png'
            if i == 1:
                self.cartas.append(Carta(True, i, _simbolo, "A", path))
            elif i <= 10:
                self.cartas.append(Carta(True, i, _simbolo, str(i), path))
            elif i == 11:
                self.cartas.append(Carta(True, i, _simbolo, "J", path))
            elif i == 12:
                self.cartas.append(Carta(True, i, _simbolo, "Q", path))
            elif i == 13:
                self.cartas.append(Carta(True, i, _simbolo, "K", path))

    def desordenar(self):
        random.seed(time.gmtime())
        random.shuffle(self.cartas)

    def imprimircartas(self):
        for x in self.cartas:
            print(x)

    def recibircarta(self, _carta: Carta):
        self.cartas.append(_carta)

    def popcarta(self):

        if self.cartas:
            return self.cartas.pop()
        else:
            return None

    def getlistclicked(self, pos):
        listclick = []

        while self.cartas:
            temp = self.cartas.pop()
            if not temp.oculto:
                listclick.append(temp)
                if temp.rect.collidepoint(pos):
                    return listclick
            else:
                self.cartas.append(temp)
                break

        listclick.reverse()
        for carta in listclick:
            self.cartas.append(carta)

        return []


    def chagevis(self):
        if self.cartas:
            temp = self.cartas.pop()
            temp.oculto = False
            temp.updatevis()
            self.cartas.append(temp)

    def OcultarTop(self):
        if self.cartas:
            carta = self.cartas.pop()
            carta.oculto = True
            carta.updatevis()
            self.recibircarta(carta)

    def MostrarTop(self):
        if self.cartas:
            carta = self.cartas.pop()
            carta.oculto = False
            carta.updatevis()
            self.recibircarta(carta)

    def colisiona(self, pos):
        if self.placeholder.rect.collidepoint(pos):
            return True
        else:
            return False

# Done Cargar imagenes para cada una de las cartas
# Done Renderizar las imagenes utilizando la lista de python
# INPROGRESS poder habilitar o des habilitar el renderizado de las imagenes
# Done Detectar si se esta haciendo click en una imagen en especifico
# Done Mover la imagen que esta en click stado y todas las imagenes asociadas
# Done Poner los diferentes mazos de cartas en determinadas posiciones
# Done sortoff Detectar si una imagen que esta en estado click esta dentro del area de los mazos
# Done Mazo que tiene una cola en vez de un stack que tiene las cartas sobrantes
