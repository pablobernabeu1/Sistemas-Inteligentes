from main import *
from casilla import *
from nodo import *
import math


# Funciones auxiliares
def rellenarDeUnos(mapi, mapaParaMostrar):  # Esta función rellena la matriz que se muestra por la terminal de -1s.
    for i in range(0, mapi.getAlto()):
        for j in range(0, mapi.getAncho()):
            mapaParaMostrar[i][j] = -1
            
            
            
def esOrigen(i, j, origen): # Esta función te dice si un punto (i, j) es el origen o no.
    return (i == origen.getFila() and j == origen.getCol())


def mostrarElMapa(mapaParaMostrar, mapi):
    for i in range(mapi.getAlto()):
        cadena = ""
        for j in range(mapi.getAncho()):
            
            cadena = cadena + " " + str(mapaParaMostrar[i][j])
            
        print(cadena)




def rellenarMapa(mapi, origen, destino, camino, mapaParaMostrar):
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



def obtenerVecinos(mapi, origen, destino, camino): # Esta función rellena bien el mapa para mostrar por la terminal y calcula el vecino más cercano al destino.
    cont = 0 # Numero de vecinos que se pueden visitar, osea que no son pared.
    distancia = 1000 # Distancia entre el mejor vecino y el destino.
    listaFront = []
    
    for i in range(origen.getFila() - 1, origen.getFila() + 2): # Recorremos las filas adyacentes al origen.
        for j in range(origen.getCol() - 1, origen.getCol() + 2): # Recorremos las columnas adyacentes al origen.
            cas = Casilla(i, j) # Creamos un objeto Casilla con los puntos actuales.
            
            if bueno(mapi, cas) and esOrigen(i, j, origen) == False: # Si el punto no es una pared y no es el origen.
                cont += 1 # Aumentamos el contador de vecinos que se pueden visitar.
                distanciaAux = abs(destino.getFila() - i) + abs(destino.getCol() - j) # Calculamos la distancia de Manhattan de un vecino al destino.
                
                nodo = Nodo(cas, origen, destino) # Creación de un nodo.
                listaFront.append(nodo)
                
                if distanciaAux <= distancia: # Si la nueva distancia es mayor que la anterior actualizamos el mejor punto.
                    distancia = distanciaAux # Actualizamos la nueva mejor distancia
                    filAux = i # Almacenamos la fila del mejor vecino.
                    colAux = j # Almacenamos la columna del mejor vecino.
                    
                
    mapi.origen = destino # Cambiamos en que casilla se encuentra actualmente el cerdito.
    # camino[filAux][colAux] = 'X' # Marcamos en la matriz 'camino' el mejor vecino. 
            
    return listaFront


def aEstrella(mapi, origen, destino, camino):
    mapaParaMostrar = inic(mapi)
    rellenarMapa(mapi, origen, destino, camino, mapaParaMostrar)
    
    listaInterior = []
    listaFrontera = obtenerVecinos(mapi, origen, destino, camino)
    
    while listaFrontera !=[]:
        n = listaFrontera[0]
        casillaActual = n.getCasilla()
        
        if n.esMeta(destino):
            # Hacer algo
            print("Has llegado al destino")
            
        else:
            listaFrontera.pop(0)
            listaInterior.append(casillaActual)
            
            for m in obtenerVecinos(mapi, origen, destino, camino)            
        
     
    mostrarElMapa(mapaParaMostrar, mapi)

