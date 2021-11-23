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
N = len(mnist_Y)

# Adaptar los conjuntos X e Y a AdaBoost
(X0, Y0) = utils.adaptar_conjuntos(mnist_X, mnist_Y, 0) # Se le pasa el 0 porque por ahora solo se pide completar para el 0, posteriormente se generaran los demás.

# Veces a iterar el bucle exterior del algoritmo (clasificadores débiles que formarán el fuerte)
T = 3
# Veces a iterar el bucle interior del algoritmo (clasificadores débiles aleatorios generados para elegir el mejor)
A = 3 

# Obtenemos los mejores clasificadores débiles después de entrenar
(h, alphas) = adaboost.entrenar(X0, Y0, T, A)

# Obtenemos el clasificador fuerte
cont = 0
for i in range(len(Y0)):
    signo = cd.obtenerClasificadorFuerte((h, alphas), X0[i])
    if (signo == 1 and Y0[i] == 1) or (signo == -1 and Y0[i] == -1):
        cont += 1

acierto = (cont * 100) / N

print("El clasificador fuerte clasifica bien el " + str(acierto) + " de los números.")



"""
# Analisis y resultados de las pruebas realizadas
T = [0, 100, 200, 300, 400]      # Numero de clasificadores 
resultados = [0, 20, 35, 56, 68] # Resultados obtenidos de clasificacion
utils.plot_arrays(T, resultados, "Porcentajes con valores de T")
"""