from physics import generar_puntos_sierpinski, calcular_area_sierpinski, contar_puntos_dentro, generar_conjunto_mandelbrot
from gui import gui_triangulo_sierpinski, pantalla_principal
from numpy import array
from math import sqrt

# #=======================================================================================
# #=======================================================================================

# Valores iniciales
iteraciones = 0
longitud_lado = 1.0
color_triangulo = 'blue'
    
# GENERACIÓN DEL TRIÁNGULO INICIAL 
altura = (sqrt(3) / 2) * longitud_lado
A = array([0, 0])
B = array([longitud_lado, 0])                     # Coordenadas de los puntos A, B, y C y altura del triángulo
C = array([longitud_lado / 2, altura])

# #=======================================================================================

# Parámetros de entrada - CONJUNTO DE MANDELBROT
plano_inicial = (-2.0, 1.0, -1.5, 1.5)
resolucion_inicial = (800, 800)
iteraciones_iniciales = 0

# #=======================================================================================

pantalla_principal (generar_puntos_sierpinski, calcular_area_sierpinski, iteraciones, longitud_lado, color_triangulo, A, B, C, generar_conjunto_mandelbrot, contar_puntos_dentro, plano_inicial, resolucion_inicial, iteraciones_iniciales)

# Dar a correr


#=======================================================================================
#COPO DE NIEVE KOCH

from physics import generate_koch_snowflake, calculate_perimeter_koch, calculate_area_koch
from gui import create_gui_Koch
from numpy import array
from math import sqrt

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

# EJECUCIÓN DE LA INTERFAZ GRÁFICA
if __name__ == "__main__":
    # Pasa las funciones necesarias a la GUI
    create_gui_Koch(generate_koch_snowflake, calculate_area_koch, calculate_perimeter_koch)
    
#==========================================================================================
#CONJUNTO DE MANDELBROT

from physics import generar_conjunto_mandelbrot, contar_puntos_dentro
from gui import crear_gui_mandelbrot

if __name__ == "__main__":
    # Configuración inicial
    plano = (-2.0, 1.0, -1.5, 1.5)  # Rango del plano complejo
    resolucion = (800, 800)  # Resolución inicial para la GUI
    max_iteraciones = 0  # Iteraciones iniciales para que se visualice algo

    # Llamar a la GUI, pasando los valores iniciales
    crear_gui_mandelbrot(generar_conjunto_mandelbrot, contar_puntos_dentro, plano, resolucion, max_iteraciones)


