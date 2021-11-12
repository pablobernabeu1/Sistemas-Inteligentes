import clasificador_debil as cd

def inicializarD(D): # Vector que inicializa el vector de probabilidades D inicialmente a 1/60000
    for i in range(60000):
        D.append(1/60000)


def entrenar(X, Y, T, A):
    clasificadores_debiles = []
    alphas = []
    D = []
    inicializarD(D)
    # print(D)
    
    for t in range(10): # numero de clasificadores debiles a crear
        clasificadores = []
        for k in range(10): # numero de pruebas aleatorias
            # Obtenemos un clasificador debil
            c_d = cd.generar_clasificador_debil(28*28)
            clasificadores.append(c_d)
            # Calculamos el error 
            error = cd.obtener_error(c_d, X, Y, D)



    
    return (clasificadores_debiles, alphas)