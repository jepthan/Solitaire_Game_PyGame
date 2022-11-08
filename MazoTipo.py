from Mazo import *


class MazoTipo(Mazo):
    def __init__(self, _simbolo: str, posx, posy, offset):
        super().__init__(posx, posy, offset)
        self.simbolo = _simbolo
        self.placeholder.__init__()
        img = pygame.Surface([98, 135])
        img.fill((200, 200, 200))
        self.placeholder.image = img
        self.placeholder.rect = img.get_rect()
        self.placeholder.rect.center = [self.posx, self.posy]
        self.grup.add(self.placeholder)

    def recibircartatipo(self, _carta: Carta):
        if _carta.simbolo != self.simbolo:
            return False
        if self.cartas:
            temp = self.cartas.pop()
            if temp.valor + 1 == _carta.valor:
                self.cartas.append(temp)
                self.cartas.append(_carta)
                return True
            else:
                self.cartas.append(temp)
                return False
        else:
            if _carta.valor == 1:  # append the A#
                self.cartas.append(_carta)
                return True
            else:
                return False

    def fill(self):
        if self.cartas:
            carta = self.cartas.pop()
            if carta.valor == 13:
                return True
            else:
                return False
        else:
            return False
