import pygame

from Carta import Carta
import random


class Mazo:
    def __init__(self, posx , posy, offset):
        self.cartas = []
        self.posx = posx
        self.posy = posy
        self.offset = offset


    def generate_card_grup(self) -> pygame.sprite.Group:
        grup = pygame.sprite.Group()
        if not self.cartas:  ##if cartas is empty
            placholer = pygame.sprite.Sprite()
            placholer.__init__()
            img = pygame.Surface([98, 135])
            img.fill((200, 200, 200))
            placholer.image = img
            placholer.rect = img.get_rect()
            placholer.rect.center = [self.posx, self.posy]
            grup.add(placholer)
        for x in self.cartas:
            x.rect.center = [self.posx, self.posy]
            grup.add(x)
        return grup
    def generate_card_grup_lader(self) -> pygame.sprite.Group:
        grup = pygame.sprite.Group()
        if(not self.cartas):##if cartas is empty
            placholer = pygame.sprite.Sprite()
            placholer.__init__()
            img = pygame.Surface([98, 135])
            img.fill((200,200,200))
            placholer.image =img
            placholer.rect = img.get_rect()
            placholer.rect.center= [self.posx, self.posy]
            grup.add(placholer)
        i = 0
        for x in self.cartas:
            x.rect.center = [self.posx, self.posy + self.offset*i]
            i += 1
            grup.add(x)

        return grup
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
        random.shuffle(self.cartas)

    def imprimircartas(self):
        for x in self.cartas:
            print(x)

    def recibircarta(self, _carta: Carta):
        self.cartas.append(_carta)

    def popcarta(self):
        size = len(self.cartas)
        if size > 0:
            return self.cartas.pop()
        else:
            return None


class MazoTipo(Mazo):
    def __init__(self, _simbolo: str, posx , posy, offset):
        super().__init__(posx, posy, offset)
        self.simbolo = _simbolo

    def recibircartatipo(self, _carta: Carta):
        if _carta.simbolo != self.simbolo:
            return False
        if self.cartas:
            temp = self.cartas.pop()
            if temp.valor + 1 == _carta.valor:
                self.cartas.append(temp)
                self.cartas.append(_carta)
                return False
            else:
                self.cartas.append(temp)
                return False
        else:
            if _carta.valor == 1:  # append the A#
                self.cartas.append(_carta)
                return True
            else:
                return False

#
# Done Cargar imagenes para cada una de las cartas
# Done Renderizar las imagenes utilizando la lista de python
# INPROGRESS poder habilitar o des habilitar el renderizado de las imagenes
# TODO Detectar si se esta haciendo click en una imagen en especifico
# TODO Mover la imagen que esta en click stado y todas las imagenes asociadas
# TODO Poner los diferentes mazos de cartas en determinadas posiciones
# TODO Detectar si una imagen que esta en estado click esta dentro del area de los mazos
# TODO Mazo que tiene una cola en vez de un stack que tiene las cartas sobrantes
