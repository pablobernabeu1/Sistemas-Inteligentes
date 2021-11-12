import matplotlib.pyplot as plt

def mostrar_imagen(imagen):
    plt.figure()
    plt.imshow(imagen)
    plt.show()

def adaptar_conjuntos(mnist_X, mnist_Y, n):
    Y = []
    
    for i in range(len(mnist_X)):
        if mnist_Y[i] == n:
            Y.append(1) # Si no funciona usar .append()
        else:
            Y.append(-1)
    
    return (mnist_X, Y)

def plot_arrays(X, Y, title):
    plt.title(title)
    plt.plot(X, Y)
    plt.show()