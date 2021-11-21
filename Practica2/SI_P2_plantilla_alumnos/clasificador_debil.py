import random
import Clasificador as clas

# Función para obtener el pixel correspondiente de la imagen, la cual está almacenada como una matriz
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
def generar_clasificador_debil():    
    clasificador = clas.Clasificador(random.randint(0, 783), random.randint(0, 255), random.randint(0, 1))
    return clasificador


def aplicar_clasificador_debil(clasificador, imagen):
    posicion = obtenerPixel(clasificador.pixel) # Obtenemos la posicion que ocupa el pixel en la matriz de 28x28.
    valorImagen = imagen[posicion[0]][posicion[1]] # Almacenamos el valor dentro de la escala de grises correspondiente al pixel.
    
    # Si la dirección del clasificador es <
    if clasificador.direccion == 0:
        # Si el umbral del clasificador cumple con el umbral de la imagen        
        if clasificador.umbral < valorImagen:
            clasificador.aplicar.append(1)
            return True
        
        else:
            clasificador.aplicar.append(-1)
            return False
    # Si la dirección del clasificador es >
    else:
        # Si el umbral del clasificador cumple con el umbral de la imagen
        if clasificador.umbral > valorImagen:
            clasificador.aplicar.append(1)
            return True
        
        else:
            clasificador.aplicar.append(-1)
            return False
        

def obtener_error(clasificador, X, Y, D):
    # Aplicamos el clasificador a todas las imagenes
    result = 0
    # Lista con todos los resultados de aplicar el clasificador a todas las imagenes
    y_d = list()
    for i in range(len(Y)):
        res = aplicar_clasificador_debil(clasificador, X[i])
        if Y[i] == 1 and res == True:
            y_d.append(True)
            result += 0
            
        elif Y[i] == 1 and res == False:
            y_d.append(False)
            result += D[i]
            
        elif Y[i] == -1 and res == True:
            y_d.append(False)
            result += D[i]
        
        elif Y[i] == -1 and res == False:
            y_d.append(True)
            result += 0

    return [result, y_d]







