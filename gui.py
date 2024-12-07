import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# Función para crear la GUI
def crear_gui(generar_puntos_func, calcular_area_func):
    # Variables locales
    iteraciones = 0  # La iteración inicial será 0
    longitud_lado = 1.0
    color_triangulo = 'blue'  # Color por defecto

    def actualizar_triangulo(figura, canvas, label_area):
        # Generar puntos del triángulo de Sierpinski
        altura = (np.sqrt(3) / 2) * longitud_lado
        A = np.array([0, 0])
        C = np.array([longitud_lado / 2, altura])
        B = np.array([longitud_lado, 0])
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
            actualizar_gui(label_longitud_lado, label_longitud_lado, figura, canvas, label_area)
        except ValueError:
            messagebox.showerror("Valor Inválido", "La longitud del lado debe ser un número mayor que 0.")
            entry_longitud_lado.delete(0, 'end')
            entry_longitud_lado.insert(0, f"{longitud_lado:.2f}")

    # Función para cambiar el color usando la barra deslizante
    def cambiar_color(valor):
        nonlocal color_triangulo
        # Obtener los valores RGB del slider
        r = int(valor)
        g = int(color_slider_verde.get())
        b = int(color_slider_azul.get())
        color_triangulo = f"#{r:02x}{g:02x}{b:02x}"  # Crear color hexadecimal
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

    # Barra deslizante para cambiar el color del triángulo
    frame_color = tk.Frame(ventana)
    frame_color.pack(pady=20)

    label_color = tk.Label(frame_color, text="Color del Triángulo", font=("Arial", 14))
    label_color.grid(row=0, column=0)

    # Barra deslizante para el color rojo
    color_slider_rojo = tk.Scale(frame_color, from_=0, to=255, orient='horizontal', label="Rojo", command=cambiar_color, length=350)
    color_slider_rojo.set(128)  # Valor inicial
    color_slider_rojo.grid(row=1, column=0, columnspan=3, pady=10)

    # Barra deslizante para el color verde
    color_slider_verde = tk.Scale(frame_color, from_=0, to=255, orient='horizontal', label="Verde", command=cambiar_color, length=350)
    color_slider_verde.set(128)  # Valor inicial
    color_slider_verde.grid(row=2, column=0, columnspan=3, pady=10)

    # Barra deslizante para el color azul
    color_slider_azul = tk.Scale(frame_color, from_=0, to=255, orient='horizontal', label="Azul", command=cambiar_color, length=350)
    color_slider_azul.set(255)  # Valor inicial
    color_slider_azul.grid(row=3, column=0, columnspan=3, pady=10)

    # Actualizar la GUI por primera vez
    actualizar_gui(label_iteraciones, label_longitud_lado, figura, canvas, label_area)

    # Ejecutar la ventana
    ventana.mainloop()





#===============================================================================================================
#===============================================================================================================
# Función para crear la GUI de Mandelbrot
def crear_gui_mandelbrot(generar_conjunto_func,contar_puntos_dentro):
    # Variables locales
    x_min, x_max, y_min, y_max = -2.0, 1.0, -1.5, 1.5
    resolucion = (800, 800)
    max_iteraciones = 0  # El valor inicial es 0
    color_mandelbrot = 'inferno'  # Color por defecto

    def actualizar_mandelbrot(figura, canvas, label_area):
        # Generar el conjunto de Mandelbrot
        mandelbrot_matrix = generar_conjunto_func((x_min, x_max, y_min, y_max), resolucion, max_iteraciones)

        # Calcular el área (número de puntos dentro del conjunto de Mandelbrot)
        puntos_dentro = contar_puntos_dentro(mandelbrot_matrix, max_iteraciones)
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
        if max_iteraciones > 0:  # Asegurarse de que no baje de 0
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

    # Barra deslizante para cambiar el color del conjunto de Mandelbrot
    frame_color = tk.Frame(ventana)
    frame_color.pack(pady=20)

    label_color = tk.Label(frame_color, text="Color del Conjunto", font=("Arial", 14))
    label_color.grid(row=0, column=0)

    color_slider = tk.Scale(frame_color, from_=0, to=255, orient='horizontal', label="Color", command=cambiar_color, length=350)
    color_slider.set(128)  # Valor inicial
    color_slider.grid(row=1, column=0, columnspan=3, pady=10)

    # Actualizar la GUI por primera vez
    actualizar_gui(label_iteraciones, figura, canvas, label_area)

    # Ejecutar la ventana
    ventana.mainloop()
