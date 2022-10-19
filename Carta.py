class Carta:
    def __init__(self, _oculto: bool, _valor: int, _simbolo: str, _nombre: str):
        self.oculto = _oculto
        self.valor = _valor
        self.simbolo = _simbolo
        self.nombre = _nombre

    def __str__(self):
        return f'Carta {self.nombre}{self.simbolo} Valor: {self.valor}'
