import pygame.sprite
import random
from pygame import *


class Carta(pygame.sprite.Sprite):
    def __init__(self, _oculto: bool, _valor: int, _simbolo: str, _nombre: str, _path :str):
        super().__init__()
        self.path = _path
        self.image = pygame.image.load(self.path)
        self.rect = self.image.get_rect()
        self.oculto = _oculto
        self.valor = _valor
        self.simbolo = _simbolo
        self.nombre = _nombre
        random.seed(_path)
        if self.oculto == True:
            self.image = pygame.image.load("Imagenes/Back.png")
            size = (98, 135)
            self.image = pygame.transform.scale(self.image, size)
        self.rect.center = [500, 100]

    def update(self):

        pass

    def updatevis(self):
        if self.oculto == True:
            self.image = pygame.image.load("Imagenes/Back.png")
            size = (98, 135)
            self.image = pygame.transform.scale(self.image, size)
        else:
            self.image = pygame.image.load(self.path)

    def __str__(self):
        return f'Carta {self.nombre}{self.simbolo} Valor: {self.valor}'



