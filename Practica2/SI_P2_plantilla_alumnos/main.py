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

# Mostrar una imagen y su etiqueta
# utils.mostrar_imagen(mnist_X[0])

# Adaptar los conjuntos X e Y a AdaBoost
(X0, Y0) = utils.adaptar_conjuntos(mnist_X, mnist_Y, 0) # Se le pasa el 0 porque por ahora solo se pide completar para el 0, posteriormente se generaran los demás.

# Veces a iterar el bucle exterior del algoritmo
T = 1
# Veces a iterar el bucle interior del algoritmo
A = 1 

# Obtenemos los mejores clasificadores débiles después de entrenar
(h, alphas) = adaboost.entrenar(X0, Y0, T, A)

# Obtenemos el clasificador fuerte
hx = 0
for i in range(T):
    ht = 0
    for x in range(len(Y0)):
        ht += h[i].aplicar[x]
    hx += alphas[i] * ht

signo = math.copysign(1, hx)









"""
# Analisis y resultados de las pruebas realizadas
T = [0, 100, 200, 300, 400]      # Numero de clasificadores 
resultados = [0, 20, 35, 56, 68] # Resultados obtenidos de clasificacion
utils.plot_arrays(T, resultados, "Porcentajes con valores de T")
"""