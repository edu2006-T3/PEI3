from physics import generar_puntos_sierpinski, calcular_area_sierpinski
from gui import crear_gui

if __name__ == "__main__":
    crear_gui(generar_puntos_sierpinski, calcular_area_sierpinski)


# Para ejecutar la gui escribir "python main.py" en la terminal


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


