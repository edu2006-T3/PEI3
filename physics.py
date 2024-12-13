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

#=====================================================================================
#=====================================================================================

#CONJUNTO DE MANDELBROT

from numpy import linspace, zeros, abs, sum

#======================================================================================

# Función para generar el conjunto de Mandelbrot
def generar_conjunto_mandelbrot(plano, resolucion, max_iteraciones):
  
    x_min, x_max, y_min, y_max = plano
    ancho, alto = resolucion

    mandelbrot_matrix = zeros((alto, ancho), dtype=int)

    # Creamos las grillas para las coordenadas reales e imaginarias
    x = linspace(x_min, x_max, ancho)
    y = linspace(y_min, y_max, alto)

    for i, imag in enumerate(y):
        for j, real in enumerate(x):
            c = complex(real, imag)
            z = 0 + 0j
            iteraciones = 0

            # Iteramos para determinar si el punto escapa
            while abs(z) <= 2 and iteraciones < max_iteraciones:
                z = z**2 + c
                iteraciones += 1

            # Guardamos el número de iteraciones en la matriz
            mandelbrot_matrix[i, j] = iteraciones

    return mandelbrot_matrix

#======================================================================================

# Función para contar los puntos dentro del conjunto de Mandelbrot
def contar_puntos_dentro(mandelbrot_matrix, max_iteraciones):

    puntos_dentro = sum(mandelbrot_matrix == max_iteraciones)
    return puntos_dentro

def generar_conjunto_mandelbrot(plano, resolucion, max_iteraciones):
    """
    Genera el conjunto de Mandelbrot utilizando operaciones vectorizadas con NumPy.
    """
    x_min, x_max, y_min, y_max = plano
    ancho, alto = resolucion

    # Creamos las grillas para las coordenadas reales e imaginarias
    x = np.linspace(x_min, x_max, ancho)
    y = np.linspace(y_min, y_max, alto)
    X, Y = np.meshgrid(x, y)  # Matrices de coordenadas

    # Inicializamos las matrices
    c = X + 1j * Y  # Matriz de números complejos
    z = np.zeros_like(c, dtype=complex)  # Matriz de iteración
    mandelbrot_matrix = np.zeros(c.shape, dtype=int)  # Matriz para almacenar iteraciones

    # Vectorizamos el cálculo del escape
    for i in range(max_iteraciones):
        mask = np.abs(z) <= 2  # Identificamos puntos que aún no escapan
        z[mask] = z[mask] ** 2 + c[mask]  # Aplicamos la fórmula solo a puntos dentro del límite
        mandelbrot_matrix[mask] += 1  # Incrementamos las iteraciones

    return mandelbrot_matrix

