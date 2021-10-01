from main import bueno
from casilla import *
import math

def rellenarDeUnos(mapi, mapaParaMostrar):  # Esta función rellena la matriz que se muestra por la terminal de -1s.
    for i in range(0, mapi.getAlto()):
        for j in range(0, mapi.getAncho()):
            mapaParaMostrar[i][j] = -1
            
            
            
def esOrigen(i, j, origen): # Esta función te dice si un punto (i, j) es el origen o no.
    return (i == origen.getFila() and j == origen.getCol())



def obtenerVecinos(mapi, origen, destino, camino, mapaParaMostrar): # Esta función rellena bien el mapa para mostrar por la terminal y calcula el vecino más cercano al destino.
    cont = 0 # Numero de vecinos que se pueden visitar, osea que no son pared.
    distancia = 1000 # Distancia entre el mejor vecino y el destino.
    
    rellenarDeUnos(mapi, mapaParaMostrar) # Llamamos a la función declarada arriba para rellenarla de -1s
    
    for i in range(origen.getFila() - 1, origen.getFila() + 2): # Recorremos las filas adyacentes al origen.
        for j in range(origen.getCol() - 1, origen.getCol() + 2): # Recorremos las columnas adyacentes al origen.
            cas = Casilla(i, j) # Creamos un objeto Casilla con los puntos actuales.
            
            if bueno(mapi, cas) and esOrigen(i, j, origen) == False: # Si el punto no es una pared y no es el origen.
                cont += 1 # Aumentamos el contador de vecinos que se pueden visitar.
                mapaParaMostrar[i][j] = cont # Actualizamos el mapa a mostrar por terminal.
                distanciaAux = abs(destino.getFila() - i) + abs(destino.getCol() - j) # Calculamos la distancia de Manhattan de un vecino al destino.
                
                if distanciaAux <= distancia: # Si la nueva distancia es mayor que la anterior actualizamos el mejor punto.
                    distancia = distanciaAux # Actualizamos la nueva mejor distancia
                    filAux = i # Almacenamos la fila del mejor vecino.
                    colAux = j # Almacenamos la columna del mejor vecino.
                    
            elif esOrigen(i, j, origen): # Si la casilla es el origen marcamos en el mapa a mostrar por teminal lo dicho.
                mapaParaMostrar[i][j] = 'O'
                
    mapi.origen = destino # Cambiamos en que casilla se encuentra actualmente el cerdito.
    camino[filAux][colAux] = 'X' # Marcamos en la matriz 'camino' el mejor vecino. 
            
    print(cont) # Mostramos el numero de vecinos visitados.
    return cont # Y devolvemos ese número, en el futuro se cambiará por el coste.


