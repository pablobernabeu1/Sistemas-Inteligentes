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



####################### FUNCIONES PARA RELLENAR LA MATRIZ #######################################
def rellenarDeUnos(mapi, mapaParaMostrar):  # Esta función rellena la matriz que se muestra por la terminal de -1s.
    for i in range(0, mapi.getAlto()):
        for j in range(0, mapi.getAncho()):
            mapaParaMostrar[i][j] = -1


def mostrarElMapa(mapaParaMostrar, mapi):
    for i in range(mapi.getAlto()):
        cadena = ""
        for j in range(mapi.getAncho()):
            cadena = cadena + " " + str(mapaParaMostrar[i][j])
            
        print(cadena)


<<<<<<< HEAD
def rellenarDeUnos(mapi, mapaParaMostrar):  # Esta función rellena la matriz que se muestra por la terminal de -1s.
    for i in range(0, mapi.getAlto()):
        for j in range(0, mapi.getAncho()):
            mapaParaMostrar[i][j] = -1
<<<<<<< HEAD
            

######################################################################################################################################
def obtenerVecinos(mapi, origen, destino, camino): # Esta función rellena bien el mapa para mostrar por la terminal y calcula el vecino más cercano al destino.
    distancia = 1000 # Distancia entre el mejor vecino y el destino.
    listaFront = []
=======
def rellenarMapa(mapi, origen, destino, camino, mapaParaMostrar): # Funcion para rellenar la matriz que se muestra por la terminal
    cont = 0
    rellenarDeUnos(mapi, mapaParaMostrar)
    
    for i in range(origen.getFila() - 1, origen.getFila() + 2): # Recorremos las filas adyacentes al origen.
        for j in range(origen.getCol() - 1, origen.getCol() + 2): # Recorremos las columnas adyacentes al origen.
            cas = Casilla(i, j)
            
            if bueno(mapi, cas) and esOrigen(i, j, origen) == False:
                cont += 1
                mapaParaMostrar[i][j] = cont
                distanciaAux = abs(destino.getFila() - i) + abs(destino.getCol() - j)
                    
            elif esOrigen(i, j, origen): # Si la casilla es el origen marcamos en el mapa a mostrar por terminal lo dicho.
                mapaParaMostrar[i][j] = 'O'
######################################################################################################################################


def obtenerVecinos(mapi, origen, destino, camino): # Esta función rellena bien el mapa para mostrar por la terminal y calcula el vecino más cercano al destino.
    distancia = 1000 # Distancia entre el mejor vecino y el destino.
    listaFront = []
    
>>>>>>> parent of cedc903 (Terminando el trabajo para la sesión 3.)
=======
            

######################################################################################################################################
def obtenerVecinos(mapi, origen, destino, camino): # Esta función rellena bien el mapa para mostrar por la terminal y calcula el vecino más cercano al destino.
    distancia = 1000 # Distancia entre el mejor vecino y el destino.
    listaFront = []
>>>>>>> 656bbae7c1340b9245cbd865c31adb2c56e99c6a
    for i in range(origen.getFila() - 1, origen.getFila() + 2): # Recorremos las filas adyacentes al origen.
        for j in range(origen.getCol() - 1, origen.getCol() + 2): # Recorremos las columnas adyacentes al origen.
            cas = Casilla(i, j) # Creamos un objeto Casilla con los puntos actuales.
            
            if bueno(mapi, cas) and esOrigen(i, j, origen) == False: # Si el punto no es una pared y no es el origen.
                nodo = Nodo(cas, origen, destino) # Creación de un nodo.
                listaFront.append(nodo)
<<<<<<< HEAD
<<<<<<< HEAD
=======
                
                distanciaAux = abs(destino.getFila() - i) + abs(destino.getCol() - j) # Calculamos la distancia de Manhattan de un vecino al destino.
                camino[i][j] = 'X'
                if distanciaAux <= distancia: # Si la nueva distancia es mayor que la anterior actualizamos el mejor punto.
                    distancia = distanciaAux # Actualizamos la nueva mejor distancia
                    filAux = i # Almacenamos la fila del mejor vecino.
                    colAux = j # Almacenamos la columna del mejor vecino.
>>>>>>> parent of cedc903 (Terminando el trabajo para la sesión 3.)
=======
>>>>>>> 656bbae7c1340b9245cbd865c31adb2c56e99c6a
                    
                
    mapi.origen = destino # Cambiamos en que casilla se encuentra actualmente el cerdito.
    # camino[filAux][colAux] = 'X' # Marcamos en la matriz 'camino' el mejor vecino. 
            
    return listaFront

<<<<<<< HEAD
"""
def filtrarHijosEnListaInterior(listaInterior, hijos):
    listaResultado = []
    for x in listaInterior:
        for y in hijos:
            if x.getCasilla().getFila() == y.getCasilla().getFila() and x.getCasilla().getCol() == y.getCasilla().getCol():
                print("")
            else:
                listaResultado.append(y)
                for z in listaResultado:
                    
                        
    return listaResultado
"""

=======
>>>>>>> 656bbae7c1340b9245cbd865c31adb2c56e99c6a




# Función principal a programar
def aEstrella(mapi, origen, destino, camino):
    mapaParaMostrar = inic(mapi)
    rellenarMapa(mapi, origen, destino, camino, mapaParaMostrar)
    nodoOrigen = Nodo(origen, origen, destino)
    nodoOrigen.setG(0)
    
    
    listaInterior = []
<<<<<<< HEAD
    listaInterior.append(nodoOrigen)
    listaFrontera = obtenerVecinos(mapi, origen, destino, camino)
=======
    listaFrontera = []
    listaFrontera.append(nodoOrigen)
>>>>>>> 656bbae7c1340b9245cbd865c31adb2c56e99c6a
    
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
            print("IMPRIMIR EL CAMINO RECORRIDO HASTA LLEGAR A LA META")
            return 1
            
        else:
            listaFrontera.pop(0)
            listaInterior.append(n)
            
<<<<<<< HEAD
<<<<<<< HEAD
            mapaParaMostrar[n.getCasilla().getFila()][n.getCasilla().getCol()] = cont
            cont += 1
            
=======
>>>>>>> parent of cedc903 (Terminando el trabajo para la sesión 3.)
=======
            mapaParaMostrar[n.getCasilla().getFila()][n.getCasilla().getCol()] = cont
            cont += 1
            
>>>>>>> 656bbae7c1340b9245cbd865c31adb2c56e99c6a
            vecinos = obtenerVecinos(mapi, n.getCasilla(), destino, camino)
            hijosNoEnListaInterior = filtrarHijosEnListaInterior(listaInterior, vecinos)
            for m in hijosNoEnListaInterior:
                gPrima = n.getG() + calcularG(n.getCasilla(), m.getCasilla())
                
                found = False
                for x in listaFrontera:
                    if x == m:
                        found = True
                    
                
                if found == False:
                    # Almacenar en el nodo m sus valores de f, g, etc...
                    m.setG(gPrima)
                    # m.setH(destino)
                    m.h = 0
                    m.setF(m.getG() + m.getH())
                    m.setPadre(n)
                    listaFrontera.append(m)
                    
                elif gPrima < m.getG():
                    m.setPadre(n)
                    # recalcular f y g del nodo m
                    m.setG(gPrima)
                    m.setF(m.getG() + m.getH())
        
     
    mostrarElMapa(mapaParaMostrar, mapi)
    
    return 1





