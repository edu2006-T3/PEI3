# physics.py 

from math import sqrt

from numpy import array,linspace, meshgrid, zeros_like, abs, zeros, sum

#======================================================================================
#======================================================================================

# TRIÁNGULO DE SIERPINSKI
#======================================================================================

# Función para la generación de los vértices

def generar_puntos_sierpinski(A, B, C, N):        # A, B y C son los vértices iniciales
                                                  # N es el número de iteraciones

    P = []       # Crea una lista donde se meten todos los puntos

    def sierpinski_recursivo(A, B, C, n):           # n es el nivel de generación, es decir, el número de iteraciones
        if n == 0:                                      
            P.append((list(A), list(B), list(C)))   # el .append añade los puntos a la lista P de puntos
        else:                                       # Esto ocurre cuando se llega al nivel 0, es decir a la última iteración N
            AB_medio = (A + B) / 2
            AC_medio = (A + C) / 2                  # Calcula los puntos de cada triángulo en cada iteración
            BC_medio = (B + C) / 2

            sierpinski_recursivo(A, AB_medio, AC_medio, n - 1)
            sierpinski_recursivo(AB_medio, B, BC_medio, n - 1)          # se vuelve a aplicar la función en cada triángulo, aplicando el método recursivo
            sierpinski_recursivo(AC_medio, BC_medio, C, n - 1)

    sierpinski_recursivo(A, B, C, N)            # se aplica la función para N iteraciones y se devuelve la lista de vértices del fractal

    return P                                    # se juntan ambas funciones para así importar el menor número de funciones a main.py

#======================================================================================

def calcular_area_sierpinski(l, N):

    return (sqrt(3) / 4) * l**2 * (3 / 4) ** N        # Función optimizada (antes ocupaba 10 líneas de código)
                                                      # Calcula el área del triángulo inicial y la multiplica por 3/4 N veces

#======================================================================================
#======================================================================================

#COPO DE NIEVE DE KOCH
#======================================================================================

# Función para la generación de los segmentos del fractal de Koch

def generar_segmentos_koch(extremo1, extremo2, iteraciones_koch):  
    # extremo1 y extremo2 son los extremos iniciales del segmento
    # iteraciones_koch es el número de iteraciones
    
    segmentos = []  # Lista para almacenar los segmentos resultantes

    def koch_recursivo(punto1, punto2, nivel):  
        if nivel == 0:
            segmentos.append((list(punto1), list(punto2)))  # Añade el segmento final a la lista
        else:
            # División del segmento en 3 partes
            punto_m1 = punto1 + (punto2 - punto1) / 3
            punto_m2 = punto1 + 2 * (punto2 - punto1) / 3
            punto_pico = rotar_60_grados(punto_m1, punto_m2)

            # Llamadas recursivas
            koch_recursivo(punto1, punto_m1, nivel - 1)
            koch_recursivo(punto_m1, punto_pico, nivel - 1)
            koch_recursivo(punto_pico, punto_m2, nivel - 1)
            koch_recursivo(punto_m2, punto2, nivel - 1)

    def rotar_60_grados(origen, destino):
        # Función auxiliar para rotar un punto 60 grados
        x, y = destino - origen
        nuevo_x = x * 0.5 - y * (3**0.5) / 2
        nuevo_y = x * (3**0.5) / 2 + y * 0.5
        return array([nuevo_x, nuevo_y]) + origen

    koch_recursivo(array(extremo1), array(extremo2), iteraciones_koch)
    return segmentos

#======================================================================================

# Función para calcular la longitud del fractal del Copo de Nieve de Koch
def calcular_longitud_koch(longitud_inicial, iteraciones_koch):  
    # longitud_inicial: longitud del segmento inicial
    # iteraciones_koch: número de iteraciones
    return longitud_inicial * (4 / 3) ** iteraciones_koch

#======================================================================================
#======================================================================================

# CONJUNTO DE MANDELBROT
#======================================================================================

# Función que genera matriz de puntos del plano complejo
def generar_conjunto_mandelbrot(plano, resolucion, max_iteraciones):
   
    x_min, x_max, y_min, y_max = plano # Límites plano complejo
    ancho, alto = resolucion # Número de puntos en cada eje 
    # max_iteraciones: nº máximo de iteraciones para determinar si un punto escapa o pertenece al conjunto

    # Definición plano complejo
    x = linspace(x_min, x_max, ancho)
    y = linspace(y_min, y_max, alto)
    X, Y = meshgrid(x, y)  # Matrices de coordenadas
    # Meshgrid combina los vectores x e y para formar matrices bidimensionales que representan una grilla de coordenadas cartesianas

    # Inicializamos las matrices
    c = X + 1j * Y  # Cada punto de la grilla es representado como un número complejo c = X + iY
    z = zeros_like(c, dtype=complex)  # Matriz inicializada en ceros que guarda el valor actual de la iteración z_n
    mandelbrot_matrix = zeros(c.shape, dtype=int)  # Matriz que almacena el número de iteraciones hasta que un punto escape o 0 si no escapa

    # Cálculo iterativo del conjunto de Mandelbrot
    # Se realiza un bucle hasta alcanzar el número máximo de iteraciones
    for x_i in range(max_iteraciones):
        mask = abs(z) <= 2  # Identifica los puntos que siguen dentro del límite para iterar
        z[mask] = z[mask] ** 2 + c[mask]  # Aplicamos la fórmula solo a puntos dentro del límite
        mandelbrot_matrix[mask] += 1  # Incrementamos las iteraciones

    return mandelbrot_matrix # Contiene el nº de iteraciones para cada punto de la grilla.

#======================================================================================

# Función para contar los puntos dentro del conjunto de Mandelbrot
def contar_puntos_dentro(mandelbrot_matrix, max_iteraciones):
    
    return sum(mandelbrot_matrix == max_iteraciones)

