from physics import generar_puntos_sierpinski, calcular_area_sierpinski, generar_conjunto_mandelbrot, contar_puntos_dentro, generar_segmentos_koch, calcular_longitud_koch
from gui import pantalla_principal
from numpy import array
from math import sqrt


# #=======================================================================================


# Valores iniciales sierpinski


N = 0                                 # número de iteraciones iniciales
l = 1.0                               # longitud del lado inicial del triángulo
color = 'blue'
   
# GENERACIÓN DEL TRIÁNGULO INICIAL


h = (sqrt(3) / 2) * l                 # altura
A = array([0, 0])
B = array([l, 0])                     # Coordenadas de los puntos A, B, y C y altura del triángulo
C = array([l / 2, h])


# #=======================================================================================


# Valores iniciales Koch


iteraciones_koch = 0                  # número de iteraciones iniciales
longitud_inicial = 1.0                # longitud del segmento inicial
color_koch = 'red'                    # color inicial del fractal de Koch


# Coordenadas iniciales de los extremos del segmento
extremo1 = array([0, 0])
extremo2 = array([longitud_inicial, 0])


# #=======================================================================================


# Parámetros de entrada - CONJUNTO DE MANDELBROT


plano_inicial = (-2.0, 1.0, -1.5, 1.5)
resolucion_inicial = (800, 800)
iteraciones_iniciales = 0


# #=======================================================================================


pantalla_principal(
    generar_puntos_sierpinski, calcular_area_sierpinski, N, l, color, A, B, C, 
    generar_conjunto_mandelbrot, contar_puntos_dentro, plano_inicial, resolucion_inicial, iteraciones_iniciales,  
    generar_segmentos_koch, calcular_longitud_koch, iteraciones_koch, longitud_inicial, color_koch, extremo1, extremo2
)





