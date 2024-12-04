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



