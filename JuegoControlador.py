from Carta import Carta
from Mazo import *
from tkinter import *

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
        self.MazoEscalera = []
        for i in range(0, 7):
            self.MazoEscalera.append(Mazo())
            self.MazoPrincipal.repartirmazo(self.MazoEscalera[i], i+1)

        for mazo in self.MazoEscalera:
            print("")
            mazo.imprimircartas()



    def start(self):
        window = Tk()
        canva = Canvas(window, height=700, width=700, bg='lightblue')
        rec = canva.create_rectangle(5, 5, 100, 100, fill='black')

        def motion(event):
            x, y = event.x, event.y
            print('{}, {}'.format(x, y))
            canva.coords(rec, x, y, x+100, y+100)
        canva.pack()
        window.bind('<Motion>', motion)
        window.mainloop()






