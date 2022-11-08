from Mazo import *


class MazoEscalera(Mazo):
    def __init__(self, posx, posy, offset):
        super().__init__(posx, posy, offset)

    def generate_card_grup_lader(self) -> pygame.sprite.Group:
        self.grup = pygame.sprite.OrderedUpdates()
        self.grup.__init__()
        self.placeholder.__init__()
        img = pygame.Surface([98, 135])
        img.fill((200, 200, 200))
        self.placeholder.image = img
        self.placeholder.rect = img.get_rect()
        self.placeholder.rect.center = [self.posx, self.posy]
        self.grup.add(self.placeholder)
        i = 0
        for x in self.cartas:
            x.rect.center = [self.posx, self.posy + self.offset * i]
            i += 1
            self.grup.add(x)

        return self.grup

    def recibirCartaEscalera(self, carta):
        if self.cartas:
            cartatop = self.cartas.pop()
        else:
            if carta.valor == 13:
                self.cartas.append(carta)
                return True
            return False

        if cartatop.Color == carta.Color:
            self.cartas.append(cartatop)
            return False
        else:
            if cartatop.valor - 1 == carta.valor:
                self.cartas.append(cartatop)
                self.cartas.append(carta)
                return True
        self.cartas.append(cartatop)
        return False
