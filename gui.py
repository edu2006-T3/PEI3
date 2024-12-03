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