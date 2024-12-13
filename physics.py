# physics.py 

from numpy import sqrt, array, pi, dot, sin, cos
import matplotlib.pyplot as plt

#======================================================================================
#======================================================================================

# Función para la generación de los vértices

def generar_puntos_sierpinski(A, B, C, iteraciones):
 
    puntos = []

    def sierpinski_recursivo(A, B, C, nivel):
        if nivel == 0:
            puntos.append((A.tolist(), B.tolist(), C.tolist()))
        else:
            AB_medio = (A + B) / 2
            AC_medio = (A + C) / 2
            BC_medio = (B + C) / 2

            sierpinski_recursivo(A, AB_medio, AC_medio, nivel - 1)
            sierpinski_recursivo(AB_medio, B, BC_medio, nivel - 1)
            sierpinski_recursivo(AC_medio, BC_medio, C, nivel - 1)

    sierpinski_recursivo(A, B, C, iteraciones)
    return puntos

#======================================================================================

# Función para calcular el área del fractal

def calcular_area_sierpinski(longitud_lado, iteraciones):

    area_inicial = (sqrt(3) / 4) * longitud_lado**2              # Área inicial del triángulo equilátero
    
    factor_reduccion = (3 / 4)        # Factor de conservación de área por iteración
    
    area_final = area_inicial * (factor_reduccion ** iteraciones)   # Área total después de las iteraciones
 #==========================================================================================================================
 #COPO DE NIEVE DE KOCH

#Lógica recursiva
 def generar_puntos_koch(A, B, iteraciones): 
    def koch_recursivo(p1, p2, nivel): 
        if nivel == 0:
            return [p1, p2]
        else:
            delta = (p2 - p1) / 3  #Cada elemento se divide en 3 partes iguales
            p3 = p1 + delta
            p5 = p2 - delta 

            angle = pi / 3  # Se usa una matriz de rotación de 60 grados para situar el siguiente triángulo equilátero
            rotation_matrix = array([[np.cos(angle), -sin(angle)], [sin(angle), cos(angle)]])
            p4 = p3 + dot(rotation_matrix, delta) #Se sustituye la parte cental por un triángulo equilátero

            return (
                koch_recursivo(p1, p3, nivel - 1) +
                koch_recursivo(p3, p4, nivel - 1)[1:] +
                koch_recursivo(p4, p5, nivel - 1)[1:] +
                koch_recursivo(p5, p2, nivel - 1)[1:]
            )

    return koch_recursivo(A, B, iteraciones)

    
    return area_final

#VERSIÓN 2


# physics.py
import numpy
import numpy as np

def generate_koch_snowflake(order, scale=1):
    """
    Generate points for the Koch snowflake.
    :param order: Recursion depth.
    :param scale: Size scaling factor.
    :return: Numpy array of points representing the snowflake.
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
    :param snowflake_points: Numpy array of points.
    :return: Total perimeter length.
    """
    perimeter = 0
    for i in range(len(snowflake_points) - 1):
        perimeter += np.linalg.norm(snowflake_points[i + 1] - snowflake_points[i])
    return perimeter

def calculate_area_koch(order, scale=1):
    """
    Calculate the area of the Koch snowflake.
    :param order: Recursion depth.
    :param scale: Size scaling factor.
    :return: Total area of the snowflake.
    """
    # Area of the initial triangle
    base_area = (np.sqrt(3) / 4) * scale ** 2

    # Area added at each iteration
    added_area = 0
    for i in range(1, order + 1):
        num_new_triangles = 3 * (4 ** (i - 1))
        side_length = scale / (3 ** i)
        triangle_area = (np.sqrt(3) / 4) * side_length ** 2
        added_area += num_new_triangles * triangle_area

    return base_area + added_area

#=====================================================================================
#=====================================================================================

# #CONJUNTO DE MANDELBROT

from numpy import linspace, meshgrid, zeros_like, abs, zeros, sum

#======================================================================================

# Función para generar el conjunto de Mandelbrot usando NumPy
def generar_conjunto_mandelbrot(plano, resolucion, max_iteraciones):
    """
    Genera el conjunto de Mandelbrot utilizando operaciones vectorizadas con NumPy.
    """
    x_min, x_max, y_min, y_max = plano
    ancho, alto = resolucion

    # Creamos las grillas para las coordenadas reales e imaginarias
    x = linspace(x_min, x_max, ancho)
    y = linspace(y_min, y_max, alto)
    X, Y = meshgrid(x, y)  # Matrices de coordenadas

    # Inicializamos las matrices
    c = X + 1j * Y  # Matriz de números complejos
    z = zeros_like(c, dtype=complex)  # Matriz de iteración
    mandelbrot_matrix = zeros(c.shape, dtype=int)  # Matriz para almacenar iteraciones

    # Vectorizamos el cálculo del escape
    for i in range(max_iteraciones):
        mask = abs(z) <= 2  # Identificamos puntos que aún no escapan
        z[mask] = z[mask] ** 2 + c[mask]  # Aplicamos la fórmula solo a puntos dentro del límite
        mandelbrot_matrix[mask] += 1  # Incrementamos las iteraciones

    return mandelbrot_matrix

#======================================================================================

# Función para contar los puntos dentro del conjunto de Mandelbrot
def contar_puntos_dentro(mandelbrot_matrix, max_iteraciones):
    """
    Cuenta los puntos que permanecen dentro del conjunto de Mandelbrot.
    """
    return sum(mandelbrot_matrix == max_iteraciones)

