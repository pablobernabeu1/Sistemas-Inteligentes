from main import *
from casilla import *
from nodo import *
import math

# Funciones auxiliares
def esOrigen(i, j, origen): # Esta función te dice si un punto (i, j) es el origen o no.
    return (i == origen.getFila() and j == origen.getCol())


def filtrarHijosEnListaInterior(listaInterior, hijos):
    listaResultado = []
    for x in hijos:
        if x not in listaInterior:
            listaResultado.append(x)
                        
    return listaResultado


def calcularG(casillaActual, casillaAnterior):
    if casillaActual.getFila() != casillaAnterior.getFila() and casillaActual.getCol() != casillaAnterior.getCol():
        return 1.5
    else:
        return 1
####################################################################################################################


####################### FUNCIONES PARA LA MATRIZ #######################################
def mostrarElMapa(mapaParaMostrar, mapi):
    print("\n")
    for i in range(mapi.getAlto()):
        cadena = ""
        for j in range(mapi.getAncho()):
            cadena = cadena + " " + str(mapaParaMostrar[i][j])
            
        print(cadena)


def rellenarDeUnos(mapi, mapaParaMostrar):  # Esta función rellena la matriz que se muestra por la terminal de -1s.
    for i in range(0, mapi.getAlto()):
        for j in range(0, mapi.getAncho()):
            mapaParaMostrar[i][j] = -1

######################################################################################################################################


############################################ Función para obtener a los vecinos de un nodo #########################################
def obtenerVecinos(mapi, origen, destino, camino, lastG): # Esta función rellena bien el mapa para mostrar por la terminal y calcula el vecino más cercano al destino.
    distancia = 1000 # Distancia entre el mejor vecino y el destino.
    listaFront = []
    for i in range(origen.getFila() - 1, origen.getFila() + 2): # Recorremos las filas adyacentes al origen.
        for j in range(origen.getCol() - 1, origen.getCol() + 2): # Recorremos las columnas adyacentes al origen.
            cas = Casilla(i, j) # Creamos un objeto Casilla con los puntos actuales.
            
            if bueno(mapi, cas) and esOrigen(i, j, origen) == False: # Si el punto no es una pared y no es el origen.
                nodo = Nodo(cas, origen, destino, lastG) # Creación de un nodo.
                listaFront.append(nodo)
                    
                
    mapi.origen = destino # Cambiamos en que casilla se encuentra actualmente el cerdito. 
            
    return listaFront

######################################################################################################################################


# Función principal a programar
def aEstrella(mapi, origen, destino, camino):
    cont = 0
    nodosExpandidos = 0
    mapaParaMostrar = inic(mapi)
    rellenarDeUnos(mapi, mapaParaMostrar)
    
    nodoOrigen = Nodo(origen, origen, destino, 0)
    nodoOrigen.setG(0)
    
    
    listaInterior = []
    listaFrontera = []
    listaFrontera.append(nodoOrigen)
    
    while listaFrontera != []:
        
        # Coger el nodo con la 'f' más pequeña.
        fMasPequeña = listaFrontera[0].getF()
        mejorNodo = listaFrontera[0]
        for x in listaFrontera:
            if x.getF() < fMasPequeña:
                fMasPequeña = x.getF()
                mejorNodo = x
        
        n = mejorNodo
        if n.esMeta(destino):
            print("\nNodos expandidos:" + str(nodosExpandidos))
            listaCamino = []
            listaCamino.append(n)
            
            hijo = n.getPadre()
            while hijo != nodoOrigen:
                listaCamino.append(hijo)
                hijo = hijo.getPadre()
                
            for c in listaCamino:
                camino[c.getCasilla().getFila()][c.getCasilla().getCol()] = 'X'
                
            mostrarElMapa(mapaParaMostrar, mapi)
            return n.getG()
            
        else:
            listaFrontera.remove(n)
            listaInterior.append(n)
            
            cont += 1
            mapaParaMostrar[n.getCasilla().getFila()][n.getCasilla().getCol()] = cont
            
            vecinos = obtenerVecinos(mapi, n.getCasilla(), destino, camino, n.getG())
            hijosNoEnListaInterior = filtrarHijosEnListaInterior(listaInterior, vecinos)
            nodosExpandidos += 1
            for m in hijosNoEnListaInterior:
                gPrima = n.getG() + calcularG(n.getCasilla(), m.getCasilla())
                
                found = False
                for x in listaFrontera:
                    if x == m:
                        found = True
                        m = x
                        break
                    
                
                if found == False:
                    # Almacenar en el nodo m sus valores de f, g, etc...
                    m.setG(gPrima)
                    m.setH(destino)
                    m.setF(m.getG() + m.getH())
                    m.setPadre(n)
                    listaFrontera.append(m)
                    
                elif gPrima <= m.getG():
                    m.setPadre(n)
                    # recalcular f y g del nodo m
                    m.setG(gPrima)
                    m.setF(m.getG() + m.getH())
        
     
    mostrarElMapa(mapaParaMostrar, mapi)
    print("\nNodos expandidos:" + str(nodosExpandidos))
    
    return None






