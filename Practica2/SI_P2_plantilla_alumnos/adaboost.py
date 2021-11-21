import clasificador_debil as cd
import math

##################################### Funciones auxiliares #####################################
# Vector que inicializa el vector de probabilidades D inicialmente a 1/60000
def inicializarD(D, N): 
    for i in range(N):
        D.append(1/N)

# Vector que inicializa el vector de alphas a 0
def inicializar(x, n):
    for i in range(n):
        x.append(0)

# Vector que inicializa el vector de errores a infinito
def inicializarErr(x, n):
    for i in range(n):
        x.append(float("inf"))

################################################################################################
def entrenar(X, Y, T, A):
    # Y array con -1 y 1 dependiendo de si es de la clase
    # X imagenes que le pasamos
    
    # Número de imagenes: 60.000
    N = len(X)
    # Lista con los grados de confianza de los clasificadores
    alphas = list()
    inicializar(alphas, T)
    # Lista con las probabilidades de las imagenes
    D = list()
    inicializarD(D, N) # Inicializa el vector de pesos a 1/60000 en todas las posiciones
    # Lista con los errores de todos los clasificadores generados
    errores = list()
    inicializarErr(errores, T)
    # Lista con los clasificadores debiles creados
    h = list()
    
    # numero de clasificadores debiles a usar
    for t in range(T):
        # numero de pruebas aleatorias
        for k in range(A): 
            # Obtenemos un clasificador debil
            c_d = cd.generar_clasificador_debil()
            # Calculamos el error 
            [c_d.error, y_tmp] = cd.obtener_error(c_d, X, Y, D) # almacenamos el error de cada clasificador
            
            # Obtenemos el mejor clasificador débil
            if c_d.error<errores[t]:
                mejorClasificador = c_d
                errores[t] = c_d.error
                y_t = y_tmp
  
        # Almacenamos el mejor clasificador débil
        h.append(mejorClasificador)
        # Obtenemos el alpha
        alphas[t] = 0.5 * math.log( ( (1 - errores[t]) / errores[t] ), 2)
        
        # Variable que acumula la suma de todos los elementos de D para después normalizar
        suma = 0
        # Actualizamos D para la siguiente iteración del bucle
        for i in range(N):
            D[i] = D[i] * math.exp(-alphas[t] * y_t[i] * mejorClasificador.aplicar[i]) # No se si está bien
            suma += D[i]
        
        # Normalizamos D
        for i in range(N):
            D[i] = D[i] / suma
            
    # Devolvemos los mejores clasificadores débiles y sus alphas, para posteriormente generar un clasificador fuerte
    return (h, alphas)