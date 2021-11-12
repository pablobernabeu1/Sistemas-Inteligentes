import random

# Dimension con la que vamos a trabajar. En nuestro caso 28*28
def generar_clasificador_debil(dimension_datos):

    pixel = random.randint(0, 783) # 0-783
    umbral = random.randint(0, 255) # 0-255
    direccion = random.randint(0, 1) # 0 - 1. Si es 0 es <, y si es 1 es >.

    return (pixel,umbral,direccion) # Devolvemos el clasificador debil generado

def aplicar_clasificador_debil(clasificador, imagen): # Modificar para hacerlo con un array de imagenes en vez de con 1 solo.
    
    valorImagen = imagen[clasificador.pixel] # Almacenamos el valor dentro de la escala de grises correspondiente al pixel.
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

#### Cambiar clasificador de tupla a clase

def obtener_error(clasificador, X, Y, D):
    # Aplicamos el clasificador a una imagen
    for i in range(len(D)):
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







