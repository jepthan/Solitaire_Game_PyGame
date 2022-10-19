from Carta import Carta
from Mazo import *


class JuegoControlador:

    def __init__(self):
        # inicializar mazo principal
        self.MazoPrincipal = Mazo()
        self.MazoPrincipal.llenarmazo()
        self.MazoPrincipal.desordenar()
        # inicializar mazo de corazones
        self.MazoCorazones = MazoTipo("♥")
        # inicializar mazo de Diamantes
        self.MazoDiamantes = MazoTipo("♦")
        # inicializar mazo de picas
        self.MazoPicas = MazoTipo("♠")
        # inicializar mazo de treboles
        self.MazoTrebol = MazoTipo("♣")
        self.MazoTrebol.imprimircartas()

    def start(self):
        while True:
            print("agregar ciclo")



