import math
from scipy.spatial import distance
# distance.chebyshev([1, 0, 0], [0, 1, 0])


def calcularG(casillaActual, casillaAnterior):
    if casillaActual.getFila() != casillaAnterior.getFila() and casillaActual.getCol() != casillaAnterior.getCol():
        return 1.5
    else:
        return 1
    

def distanciaManhattan(cas1, cas2):
    return abs(cas1.getFila() - cas2.getFila()) + abs(cas1.getCol() - cas2.getCol())


def euclidean_distance(cas1, cas2):
    return math.sqrt((cas2.getFila() - cas1.getFila())**2 + (cas2.getCol() - cas1.getCol())**2)


def pitagoras(cas1, cas2):
    return (cas2.getFila() - cas1.getFila())**2 + (cas2.getCol() - cas1.getCol())**2


def chebyshev(cas1, cas2):
    result = 0
    for i in range(2):
        d = abs(cas1[i] - cas2[i])
        result = max(result, d)
        
    return result


class Nodo():
    def __init__(self, cas, casAnterior, destino, newG):
        self.casilla = cas
        self.g = newG + calcularG(cas, casAnterior)
        # self.h = 0
        # self.h = distanciaManhattan(destino, cas)
        # self.h = pitagoras(self.casilla, destino)
        # self.h = chebyshev(self.casilla, destino)
        self.h = euclidean_distance(self.casilla, destino)
        self.f = self.g + self.h
        self.padre = None
        
    def __eq__(self, nodo2):
        return (self.casilla.getFila() == nodo2.getCasilla().getFila() and self.casilla.getCol() == nodo2.getCasilla().getCol())

    def getG(self):
        return self.g
    
    def getH(self):
        return self.h
    
    def getF(self):
        return self.f
    
    def getCasilla(self):
        return self.casilla
    
    def getPadre(self):
        return self.padre
    
    def setG(self, newG):
        self.g = newG
        
    def setH(self, destino):
        # self.h = 0
        # self.h = distanciaManhattan(destino, self.casilla)
        # self.h = pitagoras(self.casilla, destino)
        # self.h = chebyshev(self.casilla, destino)
        self.h = euclidean_distance(self.casilla, destino)
        
    def setF(self, newF):
        self.f = newF
        
    def setPadre(self, p):
        self.padre = p
    
    def esMeta(self, destino):
        return (self.casilla.getFila() == destino.getFila() and self.casilla.getCol() == destino.getCol())
    
    
        
