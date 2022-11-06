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
        self.rect.center = [random.randint(0, 700), random.randint(0, 700)]

    def __str__(self):
        return f'Carta {self.nombre}{self.simbolo} Valor: {self.valor}'



