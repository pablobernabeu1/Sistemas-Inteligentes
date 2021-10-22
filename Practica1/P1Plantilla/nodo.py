def calcularG(casillaActual, casillaAnterior):
    if casillaActual.getFila() != casillaAnterior.getFila() and casillaActual.getCol() != casillaAnterior.getCol():
        return 1.5
    else:
        return 1
    

def distanciaManhattan(cas1, cas2):
    return abs(cas1.getFila() - cas2.getFila()) + abs(cas1.getCol() - cas2.getCol())
    

class Nodo():
    def __init__(self, cas, casAnterior, destino):
        self.casilla = cas
        self.g = calcularG(cas, casAnterior)
        # self.h = distanciaManhattan(destino, cas)
        self.h = 0
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
        # self.h = distanciaManhattan(destino, self.casilla)
        self.h = 0
        
    def setF(self, newF):
        self.f = newF
        
    def setPadre(self, p):
        self.padre = p
    
    def esMeta(self, destino):
        return (self.casilla.getFila() == destino.getFila() and self.casilla.getCol() == destino.getCol())
    
    
        