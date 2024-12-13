from physics import generar_puntos_sierpinski, calcular_area_sierpinski, generar_puntos_koch, calcular_perimetro_koch
from gui import pantalla_principal, gui_triangulo_sierpinski,
from numpy import array
from math import sqrt


# VALORES INICIALES TRIÁNGULOS DE SIERPINSKIL 
iteraciones = 0
longitud_lado = 1.0
color_triangulo = 'blue'
    
# GENERACIÓN DEL TRIÁNGULO INICIAL 
altura = (sqrt(3) / 2) * longitud_lado
A = array([0, 0])
B = array([longitud_lado, 0])                     # Coordenadas de los puntos A, B, y C y altura del triángulo
C = array([longitud_lado / 2, altura])

# ======================================================================================================================

# Parámetros de entrada - CONJUNTO DE MANDELBROT
    plano = (-2.0, 1.0, -1.5, 1.5)
    resolucion = (500, 500)
    max_iteraciones = 100

# ======================================================================================================================

pantalla_principal (generar_puntos_sierpinski, calcular_area_sierpinski, iteraciones, longitud_lado, color_triangulo, A, B, C)

# Dar a correr


#=======================================================================================
#COPO DE NIEVE KOCH

from physics import generar_puntos_koch, calcular_perimetro_koch
from gui import crear_gui

if __name__ == "__main__":
    # Conectamos las funciones de physics con la GUI
    crear_gui(generar_puntos_koch, calcular_perimetro_koch)

    # Instrucción para ejecutar: python main.py
#==========================================================================================
#CONJUNTO DE MANDELBROT

from physics import generar_conjunto_mandelbrot, contar_puntos_dentro
from gui import crear_gui_mandelbrot

if __name__ == "__main__":
    # Parámetros de entrada (definidos aquí)
    plano = (-2.0, 1.0, -1.5, 1.5)
    resolucion = (500, 500)
    max_iteraciones = 100

    # Generar el conjunto de Mandelbrot
    mandelbrot_matrix = generar_conjunto_mandelbrot(plano, resolucion, max_iteraciones)

    # Contar los puntos dentro del conjunto
    puntos_dentro = contar_puntos_dentro(mandelbrot_matrix, max_iteraciones)
    print(f"Puntos dentro del conjunto: {puntos_dentro}")

    crear_gui_mandelbrot(generar_conjunto_mandelbrot, contar_puntos_dentro)


