class Carta:
    def __init__(self, _oculto, _valor, _simbolo, _nombre):
        self.oculto = _oculto
        self.valor = _valor
        self.simbolo = _simbolo
        self.nombre = _nombre

    def __str__(self):
        return f'Carta {self.nombre}{self.simbolo} Valor: {self.valor}'
