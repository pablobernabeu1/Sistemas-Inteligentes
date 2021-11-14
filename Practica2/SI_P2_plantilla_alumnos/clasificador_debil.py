import random
import Clasificador as clas


def obtenerPixel(pix):
    cont = 0
    for i in range(28):
        for j in range (28):
            cont += 1
            if cont == pix:
                pos = (i, j)
                break
            
    return pos

# Dimension con la que vamos a trabajar. En nuestro caso 28*28
def generar_clasificador_debil(dimension_datos):    
    clasificador = clas.Clasificador(random.randint(0, 783), random.randint(0, 255), random.randint(0, 1))
    return clasificador


def aplicar_clasificador_debil(clasificador, imagen): # Modificar para hacerlo con un array de imagenes en vez de con 1 solo.
    
    
    posicion = obtenerPixel(clasificador.pixel) # Obtenemos la posicion que ocupa el pizel en la matriz de 28x28.
    valorImagen = imagen[posicion[0]][posicion[1]] # Almacenamos el valor dentro de la escala de grises correspondiente al pixel.
    
    if clasificador.direccion == 0:
        if clasificador.umbral < valorImagen:
            return True
        else:
            return False
    else:
        if clasificador.umbral > valorImagen:
            return True
        else:
            return False


def obtener_error(clasificador, X, Y, D):
    # Aplicamos el clasificador a una imagen
    for i in range(len(Y)):
        res = aplicar_clasificador_debil(clasificador, X[i])
        result = 0
        if Y[i] == 1 and res == True:
            result += D[i]
            
        elif Y[i] == 1 and res == False:
            result += D[i] * Y[i]
            
        elif Y[i] == -1 and res == True:
            result += D[i] * Y[i]
        
        elif Y[i] == -1 and res == False:
            result += D[i]

    return result







