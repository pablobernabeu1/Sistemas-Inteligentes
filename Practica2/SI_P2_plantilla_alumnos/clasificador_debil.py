import random
import Clasificador as clas
import numpy as np

# Dimension con la que vamos a trabajar. En nuestro caso 28*28
def generar_clasificador_debil():    
    clasificador = clas.Clasificador(random.randint(0, 783), random.randint(0, 255), random.randint(0, 1))
    return clasificador


def aplicar_clasificador_debil(clasificador, imagen):
    valorImagen = imagen[clasificador.pixel] # Almacenamos el valor dentro de la escala de grises correspondiente al pixel.
    
    # Si la dirección del clasificador es <
    if clasificador.direccion == 0:
        # Si el umbral del clasificador cumple con el umbral de la imagen        
        if clasificador.umbral < valorImagen:
            return 1
        
        else:
            return -1
    # Si la dirección del clasificador es >
    else:
        # Si el umbral del clasificador cumple con el umbral de la imagen
        if clasificador.umbral > valorImagen:
            return 1
        
        else:
            return -1
        

def obtener_error(clasificador, X, Y, D):
    # Aplicamos el clasificador a todas las imagenes
    result = 0
    # Lista con todos los resultados de aplicar el clasificador a todas las imagenes
    y_d = list()
    for i in range(len(Y)):
        res = aplicar_clasificador_debil(clasificador, X[i])
        if Y[i] == 1 and res == 1:
            y_d.append(True)
            result += 0
            
        elif Y[i] == 1 and res == -1:
            y_d.append(False)
            result += D[i]
            
        elif Y[i] == -1 and res == 1:
            y_d.append(False)
            result += D[i]
        
        elif Y[i] == -1 and res == -1:
            y_d.append(True)
            result += 0

    return result



def aplicarClasificadorFuerte(classifier, imagen):
    (h, alphas) = classifier
    N = len(imagen)
    
    fuerte = []
    for i in range(len(alphas)):
        if i == 0:
            fuerte = np.double(alphas[i] * aplicar_clasificador_debil(h[i], imagen))
        
        else:
            fuerte = fuerte + np.double(alphas[i] * aplicar_clasificador_debil(h[i], imagen))
            
    #return np.sign(fuerte)
    return fuerte


def aplicarClasificadorFuerteSigno(classifier, imagen):
    (h, alphas) = classifier
    N = len(imagen)
    
    fuerte = []
    for i in range(len(alphas)):
        if i == 0:
            fuerte = np.double(alphas[i] * aplicar_clasificador_debil(h[i], imagen))
        
        else:
            fuerte = fuerte + np.double(alphas[i] * aplicar_clasificador_debil(h[i], imagen))
            
    return np.sign(fuerte)


