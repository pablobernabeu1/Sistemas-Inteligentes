class Nodo():
    def __init__(self, cas, origen, destino):
        self.casilla = cas
        self.g = 0
        self.h = 0
        self.f = self.g + self.h
        self.padre = None
    
    
    def getG(self):
        return self.g
    
    def getH(self):
        return self.h
    
    def getF(self):
        return self.f
    
    def getCasilla(self):
        return self.casilla
    
    def setG(self, newG):
        self.g = newG
    
    def esMeta(self, destino):
        return (self.casilla.getFila() == destino.getFila() and self.casilla.getCol() == destino.getCol())
    
    def setPadre(self, p):
        self.padre = p