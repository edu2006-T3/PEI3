# physics.py 

import numpy as np
import matplotlib.pyplot as plt

#======================================================================================

# Coordenadas iniciales del triángulo principal

longitud_lado = 1
altura = np.sqrt(3) / 2 * longitud_lado  # Altura y longitud de lado del triángulo equilátero
A = np.array([0, 0])
C = np.array([longitud_lado / 2, altura])
B = np.array([longitud_lado, 0])

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

    area_inicial = (np.sqrt(3) / 4) * longitud_lado**2              # Área inicial del triángulo equilátero
    
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

            angle = np.pi / 3  # Se usa una matriz de rotación de 60 grados para situar el siguiente triángulo equilátero
            rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
            p4 = p3 + np.dot(rotation_matrix, delta) #Se sustituye la parte cental por un triángulo equilátero

            return (
                koch_recursivo(p1, p3, nivel - 1) +
                koch_recursivo(p3, p4, nivel - 1)[1:] +
                koch_recursivo(p4, p5, nivel - 1)[1:] +
                koch_recursivo(p5, p2, nivel - 1)[1:]
            )

    return koch_recursivo(A, B, iteraciones)

    
    return area_final

