import matplotlib.pyplot as plt
import numpy

def mostrar_imagen(imagen):
    plt.figure()
    plt.imshow(imagen)
    plt.show()

def adaptar_conjuntos(mnist_X, mnist_Y, n):
    Y = list()
    X = list()
    
    for i in range(len(mnist_Y)):
        if mnist_Y[i] == n:
            Y.append(1)
        else:
            Y.append(-1)
            
        arr = numpy.array(mnist_X[i])
        X.append(arr.flatten())
    
    return (X, Y)

def plot_arrays(X, Y, title):
    plt.title(title)
    plt.plot(X, Y)
    plt.show()