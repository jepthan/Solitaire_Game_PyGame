from Carta import Carta
import random


class Mazo:
    def __init__(self):
        self.cartas = []

    def llenarmazo(self):
        self.inittipo("♦")
        self.inittipo("♥")
        self.inittipo("♣")
        self.inittipo("♠")

    def inittipo(self, _simbolo):

        for i in range(1, 14):
            if i == 1:
                self.cartas.append(Carta(False, i, _simbolo, "A"))
            elif i <= 10:
                self.cartas.append(Carta(False, i, _simbolo, str(i)))
            elif i == 11:
                self.cartas.append(Carta(False, i, _simbolo, "J"))
            elif i == 12:
                self.cartas.append(Carta(False, i, _simbolo, "Q"))
            elif i == 13:
                self.cartas.append(Carta(False, i, _simbolo, "K"))

    def desordenar(self):
        random.shuffle(self.cartas)

    def imprimircartas(self):
        for x in self.cartas:
            print(x)

    def recibircarta(self, _carta: Carta):
        self.cartas.append(_carta)

    def popcarta(self):
        return self.cartas.pop()


class MazoTipo(Mazo):
    def __init__(self, _simbolo: str):
        super().__init__()
        self.simbolo = _simbolo

    def recibircartatipo(self, _carta: Carta):
        if _carta.simbolo != self.simbolo:
            return False
        if self.cartas:
            temp = self.cartas.pop()
            if temp.valor+1 == _carta.valor:
                self.cartas.append(temp)
                self.cartas.append(_carta)
                return False
            else:
                self.cartas.append(temp)
                return False
        else:
            if _carta.valor == 1:# append the A#
                self.cartas.append(_carta)
                return True
            else:
                return False
