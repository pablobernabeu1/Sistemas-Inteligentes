# Importamos las librerias que necesitaremos
import numpy as np
import matplotlib.pyplot as plt
import math
import utils
import adaboost
import clasificador_debil as cd

# Cargamos la base de datos
npzfile = np.load("mnist.npz")
mnist_X = npzfile['x']
mnist_Y = npzfile['y']

# Declaramos una variable con el número de elementos de Mnist
N = len(mnist_Y)

# Variable del número que queremos entrenar
VALOR = 5

# Adaptar los conjuntos X e Y a AdaBoost
# (X0, Y0) = utils.adaptar_conjuntos(mnist_X, mnist_Y, VALOR) # Se le pasa el valor para el cual queremos entrenar

# Adaptamos el conjunto, con el objetivo de cuando usemos la imagen, tenga forma de vector
# y no forma de 28*28 para que nuestro algoritmo no de error.
(X, Y) = utils.adaptar_conjuntos(mnist_X, mnist_Y, VALOR)
# Obtenemos la imagen con forma de vecor
imagen = X[0]
# Mostramos la imagen con forma de 28*28 
#utils.mostrar_imagen(mnist_X[0])

# Imprimimos el valor correcto de la imagen
print("El número correcto que contiene la imagen es " + str(mnist_Y[0]))

# Creamos todos los conjuntos para todos los valores posibles 0-9
conjuntos = list()
for i in range(10):
    conjuntos.append(utils.adaptar_conjuntos(mnist_X, mnist_Y, i))

# Veces a iterar el bucle exterior del algoritmo (clasificadores débiles que formarán el fuerte)
T = 2
# Veces a iterar el bucle interior del algoritmo (clasificadores débiles aleatorios generados para elegir el mejor)
A = 2

# Obtenemos los mejores clasificadores débiles después de entrenar
# (h, alphas) = adaboost.entrenar(X0, Y0, T, A)
clasificadores_fuertes = list()
for i in range(10):
    clasificadores_fuertes.append(adaboost.entrenar(conjuntos[i][0], conjuntos[i][1], T, A))

# Obtenemos el clasificador fuerte
"""
cont = 0
for i in range(len(Y0)): # Esto es para sacar el procentaje de aciertos, si quiero ver si un número lo clasifica bien lo cojo directamente del array y le paso el clasificador
    signo = cd.aplicarClasificadorFuerteSigno((h, alphas), X0[i])
    if (signo == 1 and Y0[i] == 1) or (signo == -1 and Y0[i] == -1):
        cont += 1

# Obtenemos el porcentaje
acierto = (cont * 100) / N

print("El clasificador fuerte clasifica bien el " + str(acierto) + " de los números con T = " + str(T) + " y A = " + str(A))
"""
mejor_valor = -1
for i in range(10):
    x = cd.aplicarClasificadorFuerte(clasificadores_fuertes[i], imagen)
    if x > mejor_valor:
        mejor_valor = x
        numero_resultado = i

print("AdaBoost determina que la imagen contiene el número " + str(numero_resultado))


"""
# Almacenamos los valores obtenidos a ejecutar el algoritmo 
valores = ["2*2", "4*4", "6*6", "8*8", "10*10", "20*20", "30*30"]
resultados = [90.11, 90.5, 90.2, 92.9, 94.03, 94.97, 95.84]

# Imprimimos la gráfica
utils.plot_arrays(valores, resultados, "AdaBoost para '0'")
"""
