import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# # ======================================================================================================================================================================
# # ======================================================================================================================================================================

# Función para crear la GUI
def gui_triangulo_sierpinski(generar_puntos_func, calcular_area_func, iteraciones, longitud_lado, color_triangulo, A, B, C):
    """
    Función para crear la GUI, donde las variables 'iteraciones', 'longitud_lado', 'color_triangulo', 'A', 'B', 'C' son argumentos.
    """

    def actualizar_triangulo(figura, canvas, label_area):
        """
        Actualiza el triángulo en el gráfico y muestra el área actual.
        """
        
        # Llamamos a la función generadora de puntos de Sierpinski
        puntos = generar_puntos_func(A, B, C, iteraciones)

        # Calcular el área
        area = calcular_area_func(longitud_lado, iteraciones)
        label_area.config(text=f"Área: {area:.5f}")

        # Limpiar el gráfico anterior
        figura.clear()

        # Dibujar los triángulos con el color seleccionado
        ax = figura.add_subplot(111)
        for tri in puntos:
            x = [tri[0][0], tri[1][0], tri[2][0], tri[0][0]]
            y = [tri[0][1], tri[1][1], tri[2][1], tri[0][1]]
            ax.fill(x, y, color=color_triangulo, edgecolor='black', alpha=0.5)

        ax.set_aspect('equal')
        ax.axis('off')
        canvas.draw()

    def actualizar_gui(label_iteraciones, label_longitud_lado, figura, canvas, label_area):
        """
        Actualiza la interfaz gráfica con la información de las iteraciones y la longitud del lado.
        """
        label_iteraciones.config(text=f"Iteraciones: {iteraciones}")
        label_longitud_lado.config(text=f"Longitud Lado: {longitud_lado:.2f}")
        actualizar_triangulo(figura, canvas, label_area)

    def sumar_iteracion(label_iteraciones, label_longitud_lado, figura, canvas, label_area):
        nonlocal iteraciones
        iteraciones += 1
        actualizar_gui(label_iteraciones, label_longitud_lado, figura, canvas, label_area)

    def restar_iteracion(label_iteraciones, label_longitud_lado, figura, canvas, label_area):
        nonlocal iteraciones
        if iteraciones > 0:  # Asegurarse de que no baje de 0
            iteraciones -= 1
        actualizar_gui(label_iteraciones, label_longitud_lado, figura, canvas, label_area)

    def cambiar_longitud_lado(entry_longitud_lado, label_longitud_lado, figura, canvas, label_area):
        nonlocal longitud_lado
        try:
            longitud_lado = float(entry_longitud_lado.get())
            if longitud_lado <= 0:
                raise ValueError
            actualizar_gui(label_iteraciones, label_longitud_lado, figura, canvas, label_area)
        except ValueError:
            messagebox.showerror("Valor Inválido", "La longitud del lado debe ser un número mayor que 0.")
            entry_longitud_lado.delete(0, 'end')
            entry_longitud_lado.insert(0, f"{longitud_lado:.2f}")

    # Función para cambiar el color usando la barra deslizante
    def cambiar_color(valor):
        nonlocal color_triangulo
        # Obtener el valor de la barra deslizante para rojo (R)
        rojo = int(valor)
        # El valor de azul (B) es complementario al rojo
        azul = 255 - rojo
        verde = 0  # No se cambia el verde, se mantiene en 0
        color_triangulo = f"#{rojo:02x}{verde:02x}{azul:02x}"  # Crear el color en formato hexadecimal
        actualizar_gui(label_iteraciones, label_longitud_lado, figura, canvas, label_area)

    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Triángulo de Sierpinski")

    # Etiqueta para iteraciones
    label_iteraciones = tk.Label(ventana, text=f"Iteraciones: {iteraciones}", font=("Arial", 14))
    label_iteraciones.pack(pady=10)

    # Botones para iteraciones
    frame_iteraciones = tk.Frame(ventana)
    frame_iteraciones.pack()

    boton_sumar = tk.Button(frame_iteraciones, text="+", command=lambda: sumar_iteracion(label_iteraciones, label_longitud_lado, figura, canvas, label_area), width=4, height=1, font=("Arial", 12))
    boton_sumar.grid(row=0, column=0, padx=10)

    boton_restar = tk.Button(frame_iteraciones, text="-", command=lambda: restar_iteracion(label_iteraciones, label_longitud_lado, figura, canvas, label_area), width=4, height=1, font=("Arial", 12))
    boton_restar.grid(row=0, column=1, padx=10)

    # Etiqueta y entrada para la longitud del lado
    frame_longitud = tk.Frame(ventana)
    frame_longitud.pack(pady=10)

    label_longitud_lado = tk.Label(frame_longitud, text=f"Longitud Lado: {longitud_lado:.2f}", font=("Arial", 14))
    label_longitud_lado.grid(row=0, column=0)

    entry_longitud_lado = tk.Entry(frame_longitud, font=("Arial", 12), width=8)
    entry_longitud_lado.grid(row=0, column=1)
    entry_longitud_lado.insert(0, f"{longitud_lado:.2f}")

    boton_cambiar_longitud = tk.Button(frame_longitud, text="Cambiar", command=lambda: cambiar_longitud_lado(entry_longitud_lado, label_longitud_lado, figura, canvas, label_area), width=8, height=1, font=("Arial", 12))
    boton_cambiar_longitud.grid(row=0, column=2)

    # Etiqueta para el área
    label_area = tk.Label(ventana, text="Área: 0.00000", font=("Arial", 14))
    label_area.pack(pady=10)

    # Espacio para el gráfico
    frame_grafico = tk.Frame(ventana)
    frame_grafico.pack()

    # Crear el gráfico con Matplotlib
    figura = plt.Figure(figsize=(5, 5), dpi=100)
    canvas = FigureCanvasTkAgg(figura, master=frame_grafico)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    # Barra deslizante para cambiar el color del triángulo (de azul a rojo)
    frame_color = tk.Frame(ventana)
    frame_color.pack(pady=20)

    label_color = tk.Label(frame_color, text="Color Rojo-Azul", font=("Arial", 14))
    label_color.grid(row=0, column=0)

    # Barra deslizante para el color rojo (que también controla el azul)
    color_slider_rojo = tk.Scale(frame_color, from_=0, to=255, orient='horizontal', label="Rojo", command=cambiar_color, length=350)
    color_slider_rojo.set(0)  # Valor inicial (azul)
    color_slider_rojo.grid(row=1, column=0, columnspan=3, pady=10)

    # Actualizar la GUI por primera vez
    actualizar_gui(label_iteraciones, label_longitud_lado, figura, canvas, label_area)

======================================================================================================================================================================
======================================================================================================================================================================
#GUI DE COPO DE NIEVE DE KOCH

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def crear_gui(generar_puntos_koch, calcular_perimetro_koch):
    """
    Crea la interfaz gráfica para interactuar con el fractal del copo de nieve de Koch.
    :param generar_puntos_koch: Función para calcular los puntos del fractal.
    :param calcular_perimetro_koch: Función para calcular el perímetro del fractal.
    """
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Fractal: Copo de Nieve de Koch")
    root.geometry("800x600")

    # Variables de control
    iteraciones_var = tk.IntVar(value=3)  # Número de iteraciones
    perimetro_var = tk.StringVar(value="Perímetro: N/A")

    # Función para actualizar el fractal
    def actualizar_fractal():
        # Leer el número de iteraciones
        iteraciones = iteraciones_var.get()

        # Puntos iniciales del segmento base
        A = [0, 0]
        B = [1, 0]

        # Generar los puntos del fractal
        puntos = generar_puntos_koch(A, B, iteraciones)
        x_coords = [p[0] for p in puntos]
        y_coords = [p[1] for p in puntos]

        # Calcular el perímetro
        perimetro = calcular_perimetro_koch(puntos)
        perimetro_var.set(f"Perímetro: {perimetro:.2f}")

        # Dibujar el fractal en el lienzo Matplotlib
        ax.clear()
        ax.plot(x_coords, y_coords, color="blue")
        ax.set_title(f"Fractal de Koch (Iteraciones: {iteraciones})")
        ax.axis('equal')
        canvas.draw()

    # Frame superior para controles
    controls_frame = ttk.Frame(root)
    controls_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

    # Etiqueta y entrada para iteraciones
    ttk.Label(controls_frame, text="Número de iteraciones:").pack(side=tk.LEFT, padx=5)
    iteraciones_entry = ttk.Entry(controls_frame, textvariable=iteraciones_var, width=5)
    iteraciones_entry.pack(side=tk.LEFT, padx=5)

    # Botón para generar el fractal
    generar_button = ttk.Button(controls_frame, text="Generar Fractal", command=actualizar_fractal)
    generar_button.pack(side=tk.LEFT, padx=10)

    # Etiqueta para el perímetro
    ttk.Label(controls_frame, textvariable=perimetro_var).pack(side=tk.LEFT, padx=10)

    # Área de visualización del fractal
    figure, ax = plt.subplots(figsize=(6, 6))
    canvas = FigureCanvasTkAgg(figure, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Mostrar la ventana principal
    root.mainloop()

# Placeholder functions for testing the GUI.
def generar_puntos_koch(A, B, iteraciones):
    return [A, B]  # Replace with the actual fractal generation logic

def calcular_perimetro_koch(puntos):
    return 0  # Replace with actual perimeter calculation logic

# Uncomment the following line to test the GUI (replace placeholder functions with actual implementations).
# crear_gui(generar_puntos_koch, calcular_perimetro_koch)






#===============================================================================================================
#===============================================================================================================
# Función para crear la GUI de Mandelbrot
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

def crear_gui_mandelbrot(generar_conjunto_func, contar_puntos_dentro_func, plano_inicial, resolucion_inicial, iteraciones_iniciales):
    # Variables locales sincronizadas con main.py
    x_min, x_max, y_min, y_max = plano_inicial
    resolucion = resolucion_inicial
    max_iteraciones = iteraciones_iniciales
    color_mandelbrot = 'inferno'

    def actualizar_mandelbrot(figura, canvas, label_area):
        # Generar el conjunto de Mandelbrot
        mandelbrot_matrix = generar_conjunto_func((x_min, x_max, y_min, y_max), resolucion, max_iteraciones)

        # Calcular el área (número de puntos dentro del conjunto)
        puntos_dentro = contar_puntos_dentro_func(mandelbrot_matrix, max_iteraciones)
        label_area.config(text=f"Puntos dentro: {puntos_dentro}")

        # Limpiar el gráfico anterior
        figura.clear()

        # Dibujar el conjunto de Mandelbrot con el color seleccionado
        ax = figura.add_subplot(111)
        ax.imshow(mandelbrot_matrix, cmap=color_mandelbrot, extent=(x_min, x_max, y_min, y_max))
        ax.set_title(f'Conjunto de Mandelbrot (Iteraciones: {max_iteraciones})')
        ax.set_aspect('equal')
        ax.axis('off')
        canvas.draw()

    def actualizar_gui(label_iteraciones, figura, canvas, label_area):
        label_iteraciones.config(text=f"Iteraciones: {max_iteraciones}")
        actualizar_mandelbrot(figura, canvas, label_area)

    def sumar_iteracion(label_iteraciones, figura, canvas, label_area):
        nonlocal max_iteraciones
        max_iteraciones += 1
        actualizar_gui(label_iteraciones, figura, canvas, label_area)

    def restar_iteracion(label_iteraciones, figura, canvas, label_area):
        nonlocal max_iteraciones
        if max_iteraciones > 0:
            max_iteraciones -= 1
        actualizar_gui(label_iteraciones, figura, canvas, label_area)

    def cambiar_color(valor):
        nonlocal color_mandelbrot
        color_mandelbrot = valor
        actualizar_gui(label_iteraciones, figura, canvas, label_area)

    def cambiar_rango(entry_x_min, entry_x_max, entry_y_min, entry_y_max, label_area, figura, canvas):
        nonlocal x_min, x_max, y_min, y_max
        try:
            x_min = float(entry_x_min.get())
            x_max = float(entry_x_max.get())
            y_min = float(entry_y_min.get())
            y_max = float(entry_y_max.get())
            actualizar_gui(label_iteraciones, figura, canvas, label_area)
        except ValueError:
            messagebox.showerror("Valor Inválido", "Los valores de rango deben ser números válidos.")

    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Conjunto de Mandelbrot")

    # Etiqueta para iteraciones
    label_iteraciones = tk.Label(ventana, text=f"Iteraciones: {max_iteraciones}", font=("Arial", 14))
    label_iteraciones.pack(pady=10)

    # Botones para iteraciones
    frame_iteraciones = tk.Frame(ventana)
    frame_iteraciones.pack()

    boton_sumar = tk.Button(frame_iteraciones, text="+", command=lambda: sumar_iteracion(label_iteraciones, figura, canvas, label_area), width=4, height=1, font=("Arial", 12))
    boton_sumar.grid(row=0, column=0, padx=10)

    boton_restar = tk.Button(frame_iteraciones, text="-", command=lambda: restar_iteracion(label_iteraciones, figura, canvas, label_area), width=4, height=1, font=("Arial", 12))
    boton_restar.grid(row=0, column=1, padx=10)

    # Etiquetas y entradas para el rango del conjunto
    frame_rango = tk.Frame(ventana)
    frame_rango.pack(pady=10)

    label_x_min = tk.Label(frame_rango, text="X min:", font=("Arial", 12))
    label_x_min.grid(row=0, column=0)
    entry_x_min = tk.Entry(frame_rango, font=("Arial", 12))
    entry_x_min.insert(0, f"{x_min}")
    entry_x_min.grid(row=0, column=1)

    label_x_max = tk.Label(frame_rango, text="X max:", font=("Arial", 12))
    label_x_max.grid(row=1, column=0)
    entry_x_max = tk.Entry(frame_rango, font=("Arial", 12))
    entry_x_max.insert(0, f"{x_max}")
    entry_x_max.grid(row=1, column=1)

    label_y_min = tk.Label(frame_rango, text="Y min:", font=("Arial", 12))
    label_y_min.grid(row=2, column=0)
    entry_y_min = tk.Entry(frame_rango, font=("Arial", 12))
    entry_y_min.insert(0, f"{y_min}")
    entry_y_min.grid(row=2, column=1)

    label_y_max = tk.Label(frame_rango, text="Y max:", font=("Arial", 12))
    label_y_max.grid(row=3, column=0)
    entry_y_max = tk.Entry(frame_rango, font=("Arial", 12))
    entry_y_max.insert(0, f"{y_max}")
    entry_y_max.grid(row=3, column=1)

    boton_cambiar_rango = tk.Button(frame_rango, text="Cambiar Rango", command=lambda: cambiar_rango(entry_x_min, entry_x_max, entry_y_min, entry_y_max, label_area, figura, canvas), width=20, height=1, font=("Arial", 12))
    boton_cambiar_rango.grid(row=4, column=0, columnspan=2, pady=10)

    # Etiqueta para los puntos dentro del conjunto
    label_area = tk.Label(ventana, text="Puntos dentro: 0", font=("Arial", 14))
    label_area.pack(pady=10)

    # Espacio para el gráfico
    frame_grafico = tk.Frame(ventana)
    frame_grafico.pack()

    # Crear el gráfico con Matplotlib
    figura = plt.Figure(figsize=(6, 6), dpi=100)
    canvas = FigureCanvasTkAgg(figura, master=frame_grafico)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    # Actualizar la GUI por primera vez
    actualizar_gui(label_iteraciones, figura, canvas, label_area)

    # Ejecutar la ventana
    ventana.mainloop()




# # ======================================================================================================================================================================
# # ======================================================================================================================================================================

# Función para abrir la ventana de Sierpinski
def abrir_sierpinski(generar_puntos_sierpinski, calcular_area_sierpinski, iteraciones, longitud_lado, color_triangulo, A, B, C):
    # Llamar a la función crear_gui 
    gui_triangulo_sierpinski(generar_puntos_sierpinski, calcular_area_sierpinski, iteraciones, longitud_lado, color_triangulo, A, B, C)

# Función para abrir una ventana de información
def abrir_info():
    ventana_info = tk.Toplevel()
    ventana_info.title("Información")
    label_info = tk.Label(ventana_info, text="Esta es una ventana de información.", font=("Arial", 12))
    label_info.pack(pady=20)
    boton_cerrar = tk.Button(ventana_info, text="Cerrar", command=ventana_info.destroy, font=("Arial", 12))
    boton_cerrar.pack(pady=10)

# Función para abrir una ventana de configuración
def abrir_configuracion():
    ventana_configuracion = tk.Toplevel()
    ventana_configuracion.title("Configuración")
    label_config = tk.Label(ventana_configuracion, text="Aquí puedes configurar los parámetros.", font=("Arial", 12))
    label_config.pack(pady=20)
    boton_cerrar = tk.Button(ventana_configuracion, text="Cerrar", command=ventana_configuracion.destroy, font=("Arial", 12))
    boton_cerrar.pack(pady=10)

# Función que crea la ventana principal con tres botones
def pantalla_principal(generar_puntos_sierpinski, calcular_area_sierpinski, iteraciones, longitud_lado, color_triangulo, A, B, C):
    ventana_principal = tk.Tk()
    ventana_principal.title("Pantalla Principal")

    # Etiqueta de bienvenida
    label_bienvenida = tk.Label(ventana_principal, text="Bienvenido, selecciona una opción:", font=("Arial", 14))
    label_bienvenida.pack(pady=20)

    # Crear los tres botones
    boton_sierpinski = tk.Button(ventana_principal, text="Abrir Sierpinski", command=lambda: abrir_sierpinski(generar_puntos_sierpinski, calcular_area_sierpinski, iteraciones, longitud_lado, color_triangulo, A, B, C), font=("Arial", 14), width=20)
    boton_sierpinski.pack(pady=10)

    boton_info = tk.Button(ventana_principal, text="Abrir Información", command=abrir_info, font=("Arial", 14), width=20)
    boton_info.pack(pady=10)

    boton_configuracion = tk.Button(ventana_principal, text="Abrir Configuración", command=abrir_configuracion, font=("Arial", 14), width=20)
    boton_configuracion.pack(pady=10)

    # Ejecutar la ventana principal
    ventana_principal.mainloop()

