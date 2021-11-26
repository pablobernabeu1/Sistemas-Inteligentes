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
VALOR = 0

# Adaptar los conjuntos X e Y a AdaBoost
(X0, Y0) = utils.adaptar_conjuntos(mnist_X, mnist_Y, VALOR) # Se le pasa el valor para el cual queremos entrenar

# Veces a iterar el bucle exterior del algoritmo (clasificadores débiles que formarán el fuerte)
T = 10
# Veces a iterar el bucle interior del algoritmo (clasificadores débiles aleatorios generados para elegir el mejor)
A = 10

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

valores = ["2*2", "4*4", "6*6", "8*8", "10*10"]
resultados = [90, 90.5, 9.2, 92.9, 93.34]

utils.plot_arrays(valores, resultados, "AdaBoost para '0'")











"""
# Analisis y resultados de las pruebas realizadas
T = [0, 100, 200, 300, 400]      # Numero de clasificadores 
resultados = [0, 20, 35, 56, 68] # Resultados obtenidos de clasificacion
utils.plot_arrays(T, resultados, "Porcentajes con valores de T")
"""



"""

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
N = len(mnist_Y)

# Adaptar los conjuntos X e Y a AdaBoost para cada posible valor
(X0, Y0) = utils.adaptar_conjuntos(mnist_X, mnist_Y, 0)
(X1, Y1) = utils.adaptar_conjuntos(mnist_X, mnist_Y, 1)
(X2, Y2) = utils.adaptar_conjuntos(mnist_X, mnist_Y, 2)
(X3, Y3) = utils.adaptar_conjuntos(mnist_X, mnist_Y, 3)
(X4, Y4) = utils.adaptar_conjuntos(mnist_X, mnist_Y, 4)
(X5, Y5) = utils.adaptar_conjuntos(mnist_X, mnist_Y, 5)
(X6, Y6) = utils.adaptar_conjuntos(mnist_X, mnist_Y, 6)
(X7, Y7) = utils.adaptar_conjuntos(mnist_X, mnist_Y, 7)
(X8, Y8) = utils.adaptar_conjuntos(mnist_X, mnist_Y, 8)
(X9, Y9) = utils.adaptar_conjuntos(mnist_X, mnist_Y, 9) 

# Veces a iterar el bucle exterior del algoritmo (clasificadores débiles que formarán el fuerte)
T = 3
# Veces a iterar el bucle interior del algoritmo (clasificadores débiles aleatorios generados para elegir el mejor)
A = 3

# Declaramos las variables que cuentan el número de veces
# Contamos las veces que aparece cada número
for i in range(N):
    

# Obtenemos los mejores clasificadores débiles después de entrenar
(h0, alphas0) = adaboost.entrenar(X0, Y0, T, A)
(h1, alphas1) = adaboost.entrenar(X1, Y1, T, A)
(h2, alphas2) = adaboost.entrenar(X2, Y2, T, A)
(h3, alphas3) = adaboost.entrenar(X3, Y3, T, A)
(h4, alphas4) = adaboost.entrenar(X4, Y4, T, A)
(h5, alphas5) = adaboost.entrenar(X5, Y5, T, A)
(h6, alphas6) = adaboost.entrenar(X6, Y6, T, A)
(h7, alphas7) = adaboost.entrenar(X7, Y7, T, A)
(h8, alphas8) = adaboost.entrenar(X8, Y8, T, A)
(h9, alphas9) = adaboost.entrenar(X9, Y9, T, A)

# Declaramos las variables que almacenarán los aciertos para cada número
cont0 = 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0
cont6 = 0
cont7 = 0
cont8 = 0
cont9 = 0
contGlobal = 0
# Generamos y usamos el clasificador fuerte
for i in range(N):
    # Comprobamos si la clasificación es correcta para todos los valores
    if cd.obtenerClasificadorFuerte((h0, alphas0), X0[i]) == 1 and Y0[i] == 1:
        cont0 += 1
    if cd.obtenerClasificadorFuerte((h1, alphas1), X1[i]) == 1 and Y1[i] == 1:
        cont1 += 1
    if cd.obtenerClasificadorFuerte((h2, alphas2), X2[i]) == 1 and Y2[i] == 1:
        cont2 += 1
    if cd.obtenerClasificadorFuerte((h3, alphas3), X3[i]) == 1 and Y3[i] == 1:
        cont3 += 1
    if cd.obtenerClasificadorFuerte((h4, alphas4), X4[i]) == 1 and Y4[i] == 1:
        cont4 += 1
    if cd.obtenerClasificadorFuerte((h5, alphas5), X5[i]) == 1 and Y5[i] == 1:
        cont5 += 1
    if cd.obtenerClasificadorFuerte((h6, alphas6), X6[i]) == 1 and Y6[i] == 1:
        cont6 += 1
    if cd.obtenerClasificadorFuerte((h7, alphas7), X7[i]) == 1 and Y7[i] == 1:
        cont7 += 1
    if cd.obtenerClasificadorFuerte((h8, alphas8), X8[i]) == 1 and Y8[i] == 1:
        cont8 += 1
    if cd.obtenerClasificadorFuerte((h9, alphas9), X9[i]) == 1 and Y9[i] == 1:
        cont9 += 1

acierto0 = (cont0 * 100) / N
acierto1 = (cont1 * 100) / N
acierto2 = (cont2 * 100) / N
acierto3 = (cont3 * 100) / N
acierto4 = (cont4 * 100) / N
acierto5 = (cont5 * 100) / N
acierto6 = (cont6 * 100) / N
acierto7 = (cont7 * 100) / N
acierto8 = (cont8 * 100) / N
acierto9 = (cont9 * 100) / N

print("El clasificador fuerte clasifica bien el " + str(acierto0) + " de los números para el valor 0")
print("El clasificador fuerte clasifica bien el " + str(acierto1) + " de los números para el valor 1")
print("El clasificador fuerte clasifica bien el " + str(acierto2) + " de los números para el valor 2")
print("El clasificador fuerte clasifica bien el " + str(acierto3) + " de los números para el valor 3")
print("El clasificador fuerte clasifica bien el " + str(acierto4) + " de los números para el valor 4")
print("El clasificador fuerte clasifica bien el " + str(acierto5) + " de los números para el valor 5")
print("El clasificador fuerte clasifica bien el " + str(acierto6) + " de los números para el valor 6")
print("El clasificador fuerte clasifica bien el " + str(acierto7) + " de los números para el valor 7")
print("El clasificador fuerte clasifica bien el " + str(acierto8) + " de los números para el valor 8")
print("El clasificador fuerte clasifica bien el " + str(acierto9) + " de los números para el valor 9")

"""

