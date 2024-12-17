# physics.py 

from math import sqrt

from numpy import linspace, meshgrid, zeros_like, abs, zeros, sum

#======================================================================================
#======================================================================================

# Función para la generación de los vértices

def generar_puntos_sierpinski(A, B, C, N):        # A, B y C son los vértices iniciales
                                                  # N es el número de iteraciones

    P = []       # Crea una lista donde se meten todos los puntos

    def sierpinski_recursivo(A, B, C, n):       # n es el nivel de generación, es decir, el número de iteraciones
        if n == 0:                                      
            P.append((list(A), list(B), list(C)))   # el .append añade los puntos a la lista P de puntos
        else:                                       # Esto ocurre cuando se llega al nivel 0, es decir a la última iteración N
            AB_medio = (A + B) / 2
            AC_medio = (A + C) / 2                  # Calcula los puntos de cada triángulo en cada iteración
            BC_medio = (B + C) / 2

            sierpinski_recursivo(A, AB_medio, AC_medio, n - 1)
            sierpinski_recursivo(AB_medio, B, BC_medio, n - 1)              # se vuelve a aplicar la función en cada triángulo, aplicando el método recursivo
            sierpinski_recursivo(AC_medio, BC_medio, C, n - 1)

    sierpinski_recursivo(A, B, C, N)            # se aplica la función para N iteraciones y se devuelve la lista de vértices del fractal

    return P                                    # se juntan ambas funciones para así importar el menor número de funciones a main.py

#======================================================================================

def calcular_area_sierpinski(l, N):

    return (sqrt(3) / 4) * l**2 * (3 / 4) ** N        # Función optimizada

#======================================================================================
#======================================================================================
#======================================================================================

#COPO DE NIEVE DE KOCH

import numpy as np

def generate_koch_snowflake(order, scale=1):
    """
    Generate points for the Koch snowflake.
    """
    def koch_recursive(p1, p2, depth):
        if depth == 0:
            return [p1, p2]
        # Divide the segment into three parts
        delta = (p2 - p1) / 3
        p3 = p1 + delta
        p5 = p2 - delta

        # Calculate the peak point of the triangle
        angle = np.pi / 3  # 60 degrees
        rotation_matrix = np.array([
            [np.cos(angle), -np.sin(angle)],
            [np.sin(angle), np.cos(angle)]
        ])
        peak = p3 + np.dot(rotation_matrix, delta)

        # Recursively process each segment
        return (
            koch_recursive(p1, p3, depth - 1)[:-1] +
            koch_recursive(p3, peak, depth - 1)[:-1] +
            koch_recursive(peak, p5, depth - 1)[:-1] +
            koch_recursive(p5, p2, depth - 1)
        )

    # Define the initial triangle
    p1 = np.array([0, 0])
    p2 = np.array([scale, 0])
    p3 = np.array([scale / 2, scale * np.sqrt(3) / 2])
    triangle = [p1, p2, p3, p1]

    # Generate Koch snowflake by applying the recursive function to each side
    snowflake_points = []
    for i in range(len(triangle) - 1):
        snowflake_points += koch_recursive(triangle[i], triangle[i + 1], order)[:-1]
    snowflake_points.append(triangle[0])  # Close the snowflake

    return np.array(snowflake_points)

def calculate_perimeter_koch(snowflake_points):
    """
    Calculate the perimeter of the Koch snowflake.
    """
    perimeter = 0
    for i in range(len(snowflake_points) - 1):
        perimeter += np.linalg.norm(snowflake_points[i + 1] - snowflake_points[i])
    return perimeter

def calculate_area_koch(order, scale=1):
    """
    Calculate the area of the Koch snowflake.
    """
    base_area = (np.sqrt(3) / 4) * scale ** 2

    # Area added at each iteration
    added_area = 0
    for i in range(1, order + 1):
        num_new_triangles = 3 * (4 ** (i - 1))
        side_length = scale / (3 ** i)
        triangle_area = (np.sqrt(3) / 4) * side_length ** 2
        added_area += num_new_triangles * triangle_area

    return base_area + added_area

#======================================================================================
#======================================================================================
#======================================================================================

# Función para generar una matriz que representa el conjunto de Mandelbrot
def generar_conjunto_mandelbrot(plano, resolucion, max_iteraciones):
   
    x_min, x_max, y_min, y_max = plano #Especifica los límites del plano complejo como una tupla
    ancho, alto = resolucion #Número de puntos en cada eje como una tupla

    # Creamos las grillas para las coordenadas reales e imaginarias
    #Linspace genera un arreglo de valores equidistantes entre dos extremos
    x = linspace(x_min, x_max, ancho)
    y = linspace(y_min, y_max, alto)
    X, Y = meshgrid(x, y)  # Matrices de coordenadas
    # Meshgrid convierte dos arreglos unidimensionales en matrices bidimensionales que forman una grilla de coordenadas cartesianas.
    # Inicializamos las matrices
    c = X + 1j * Y  # Matriz de números complejos combinando X y Y con el operador +1j*
    z = zeros_like(c, dtype=complex)  # Matriz del tamaño de c, llena de ceros(números complejos), que representa las iteraciones de cada punto.
    mandelbrot_matrix = zeros(c.shape, dtype=int)  # Matriz para almacenar iteraciones

    # Vectorizamos el cálculo del escape
    for x_i in range(max_iteraciones):
        #mask: matriz booleana(True o False) que indica qué elementos cumplen la condición
        mask = abs(z) <= 2  # Identificamos puntos que aún no escapan
        z[mask] = z[mask] ** 2 + c[mask]  # Aplicamos la fórmula solo a puntos dentro del límite
        mandelbrot_matrix[mask] += 1  # Incrementamos las iteraciones

    return mandelbrot_matrix

#======================================================================================

# Función para contar los puntos dentro del conjunto de Mandelbrot
def contar_puntos_dentro(mandelbrot_matrix, max_iteraciones):
    
    return sum(mandelbrot_matrix == max_iteraciones)


##########################################################################################
##########################################################################################
##########################################################################################

