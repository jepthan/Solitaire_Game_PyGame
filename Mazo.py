from Carta import Carta


class Mazo:
    def __init__(self):
        self.cartas = []
        self.llenarmazo()

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

    def imprimircartas(self):
        for x in self.cartas:
            print(x)



