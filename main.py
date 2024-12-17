from physics import generar_puntos_sierpinski, calcular_area_sierpinski, contar_puntos_dentro, generar_conjunto_mandelbrot, generate_koch_snowflake,generate_koch_snowflake, calculate_perimeter_koch, calculate_area_koch
from gui import pantalla_principal
from numpy import array
from math import sqrt

# #=======================================================================================
# #=======================================================================================

# Valores iniciales
N = 0                                 # número de iteraciones iniciales
l = 1.0                               # longitud del lado inicial del triángulo
color = 'blue'
    
# GENERACIÓN DEL TRIÁNGULO INICIAL 
h = (sqrt(3) / 2) * l                 # altura
A = array([0, 0])
B = array([l, 0])                     # Coordenadas de los puntos A, B, y C y altura del triángulo
C = array([l / 2, h])

# #=======================================================================================

# Parámetros de entrada - CONJUNTO DE MANDELBROT
plano_inicial = (-2.0, 1.0, -1.5, 1.5)
resolucion_inicial = (800, 800)
iteraciones_iniciales = 0

# #=======================================================================================

# VALORES INICIALES DEL COPO DE NIEVE DE KOCH

iteraciones = 0  # Número de iteraciones (puede ser modificado desde la GUI)
escala = 1.0  # Tamaño del fractal
color_fractal = 'blue'  # Color del fractal

# GENERACIÓN DEL TRIÁNGULO BASE
# Coordenadas iniciales del triángulo equilátero que define la base del copo
altura = (sqrt(3) / 2) * escala
A = array([0, 0])
B = array([escala, 0])  # Lado horizontal del triángulo
C = array([escala / 2, altura])  # Punto superior

# #=======================================================================================

pantalla_principal(generar_puntos_sierpinski, calcular_area_sierpinski, N, l, color, A, B, C, generar_conjunto_mandelbrot, contar_puntos_dentro, plano_inicial, resolucion_inicial, iteraciones_iniciales,generate_koch_snowflake, calculate_area_koch, calculate_perimeter_koch)
