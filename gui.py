import tkinter as tk
from tkinter import messagebox, Frame, Label, Button, Tk, Scale, Entry, Toplevel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

# # ======================================================================================================================================================================
# # ======================================================================================================================================================================

# Función para crear la GUI para el triángulo de Sierpinski

def gui_triangulo_sierpinski(f, g, N, l, color, A, B, C):   # ARGUMENTOS: función que cálcula los vértices, función que calcula el área en la n iteración, longitud de lado, color del triángulo, y vertices iniciales
  
    def actualizar_triangulo(figura, canvas, label_a):    #  Actualiza el triángulo en el gráfico y muestra el área actual.
                                                             # figura = donde se dibujará el lienzo; canvas lienzo donde se mostrará la figura; label_a = eiqueta que muestra el área
        
        # Llamamos a la función generadora de puntos de Sierpinski
        P = f(A, B, C, N)              # P = lista de vértices

        # Calcular el área
        a = g(l, N)                                        # a = área en la n iteració
        label_a.config(text=f"Área: {a:.5f}")              # muestra el área en la etiqueta con una precisión de 5 decimales 

        # Limpiar el gráfico anterior
        figura.clear()

        # Dibujar los triángulos con el color seleccionado
        ax = figura.add_subplot(111)        # subplot se refiere a una gráfica que forma parte de una cuadrícula de gráficos dentro de una misma figura
        for triangulo in P:
            x = [triangulo[0][0], triangulo[1][0], triangulo[2][0], triangulo[0][0]]   # triángulo = cada triángulo generado en P
            y = [triangulo[0][1], triangulo[1][1], triangulo[2][1], triangulo[0][1]]   # las coordenadas de cada uno de sus vértices
            ax.fill(x, y, color=color, edgecolor='black', alpha=0.5)      # Dibuja el triángulo
                                                                         # edge color = color del borde; beta = opacidad
        
        ax.set_aspect('equal')           # asegura que la relación entre los ejes x y y sea igual
        ax.axis('off')                   # desactiva los ejes y las etiquetas del gráfico
        canvas.draw()                    # actualiza y redibuja el gráfico en el lienzo

    def actualizar_gui(label_N, label_l, figura, canvas, label_a):  # Actualiza la interfaz gráfica con la información de las iteraciones y la longitud del lado

        label_N.config(text=f"Iteraciones: {N}")
        label_l.config(text=f"Longitud Lado: {l:.2f}")
        actualizar_triangulo(figura, canvas, label_a)

    def sumar_N(label_N, label_l, figura, canvas, label_a):
        nonlocal N
        N += 1
        actualizar_gui(label_N, label_l, figura, canvas, label_a)

    def restar_N(label_N, label_l, figura, canvas, label_a):
        nonlocal N
        if N > 0:  # Asegurarse de que no baje de 0
            N -= 1
        actualizar_gui(label_N, label_l, figura, canvas, label_a)

    def cambiar_l(entry_l, label_l, figura, canvas, label_a):
        nonlocal l
        try:
            l = float(entry_l.get())
            if l <= 0:
                raise ValueError
            actualizar_gui(label_N, label_l, figura, canvas, label_a)
        except ValueError:
            messagebox.showerror("Valor Inválido", "La longitud del lado debe ser un número mayor que 0.")
            entry_l.delete(0, 'end')
            entry_l.insert(0, f"{l:.2f}")

    # Función para cambiar el color usando la barra deslizante
    def cambiar_color(valor):
        nonlocal color
        # Obtener el valor de la barra deslizante para rojo (R)
        rojo = int(valor)
        # El valor de azul (B) es complementario al rojo
        azul = 255 - rojo
        verde = 0  # No se cambia el verde, se mantiene en 0
        color = f"#{rojo:02x}{verde:02x}{azul:02x}"  # Crear el color en formato hexadecimal
        actualizar_gui(label_N, label_l, figura, canvas, label_a)

    # Crear la ventana principal
    ventana = Tk()
    ventana.title("Triángulo de Sierpinski")

    # Ventana a pantalla completa
    ventana.attributes('-fullscreen', True)

    # Configurar el color de fondo gris oscuro
    ventana.configure(bg='#2e2e2e')  # Gris oscuro

    # Etiqueta para iteraciones
    label_N = Label(ventana, text=f"Iteraciones: {N}", font=("Arial", 14), fg='white', bg='#2e2e2e')
    label_N.pack(pady=10)

    # Botones para iteraciones
    frame_N = Frame(ventana, bg='#2e2e2e')
    frame_N.pack()

    boton_sumar = Button(frame_N, text="+", command=lambda: sumar_N(label_N, label_l, figura, canvas, label_a), width=4, height=1, font=("Arial", 12), fg='black', bg='white')
    boton_sumar.grid(row=0, column=0, padx=10)

    boton_restar = Button(frame_N, text="-", command=lambda: restar_N(label_N, label_l, figura, canvas, label_a), width=4, height=1, font=("Arial", 12), fg='black', bg='white')
    boton_restar.grid(row=0, column=1, padx=10)

    # Etiqueta y entrada para la longitud del lado
    frame_l = Frame(ventana, bg='#2e2e2e')
    frame_l.pack(pady=10)

    label_l = Label(frame_l, text=f"Longitud Lado: {l:.2f}", font=("Arial", 14), fg='white', bg='#2e2e2e')
    label_l.grid(row=0, column=0)

    entry_l = Entry(frame_l, font=("Arial", 12), width=8)
    entry_l.grid(row=0, column=1)
    entry_l.insert(0, f"{l:.2f}")

    boton_cambiar_l = Button(frame_l, text="Cambiar", command=lambda: cambiar_l(entry_l, label_l, figura, canvas, label_a), width=8, height=1, font=("Arial", 12), fg='black', bg='white')
    boton_cambiar_l.grid(row=0, column=2)

    # Etiqueta para el área
    label_a = Label(ventana, text="Área: 0.00000", font=("Arial", 14), fg='white', bg='#2e2e2e')
    label_a.pack(pady=10)

    # Espacio para el gráfico
    frame_grafico = Frame(ventana, bg='#2e2e2e')
    frame_grafico.pack()

    # Crear el gráfico con Matplotlib
    figura = Figure(figsize=(5, 5), dpi=100)
    canvas = FigureCanvasTkAgg(figura, master=frame_grafico)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    # Barra deslizante para cambiar el color del triángulo (de azul a rojo)
    frame_color = Frame(ventana, bg='#2e2e2e')
    frame_color.pack(pady=20)

    label_color = Label(frame_color, text="Color Rojo-Azul", font=("Arial", 14), fg='white', bg='#2e2e2e')
    label_color.grid(row=0, column=0)

    # Barra deslizante para el color rojo (que también controla el azul)
    color_slider_rojo = Scale(frame_color, from_=0, to=255, orient='horizontal', label="Rojo", command=cambiar_color, length=350)
    color_slider_rojo.set(0)  # Valor inicial (azul)
    color_slider_rojo.grid(row=1, column=0, columnspan=3, pady=10)

    # Botón de cerrar en la parte inferior
    boton_cerrar = Button(ventana, text="Volver", command=ventana.destroy, font=("Arial", 14), width=20, fg='black', bg='white')
    boton_cerrar.pack(side='bottom', pady=20)

    # Actualizar la GUI por primera vez
    actualizar_gui(label_N, label_l, figura, canvas, label_a)

    # Ejecutar la ventana principal
    ventana.mainloop()

# # ======================================================================================================================================================================
# # ======================================================================================================================================================================

# #GUI DE COPO DE NIEVE DE KOCH

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def create_gui_Koch(generate_koch, calculate_area, calculate_perimeter):
    """
    Create the GUI for interacting with the Koch snowflake generator.
    """
    def update_plot():
        # Get user input
        try:
            order = int(iterations_var.get())
            scale = float(scale_var.get())
        except ValueError:
            error_label.config(text="Por favor, ingresa valores válidos.")
            return

        # Generate snowflake points
        points = generate_koch(order, scale)

        # Calculate perimeter and area
        perimeter = calculate_perimeter(points)
        area = calculate_area(order, scale)

        # Update labels
        perimeter_var.set(f"Perímetro: {perimeter:.2f}")
        area_var.set(f"Área: {area:.2f}")

        # Plot the snowflake
        ax.clear()
        ax.plot(points[:, 0], points[:, 1], color='blue', lw=1)
        ax.axis('equal')
        ax.set_title(f"Copo de Nieve de Koch (Orden {order})")
        canvas.draw()

    # Create the main window
    root = tk.Tk()
    root.title("Generador del Copo de Nieve de Koch")
    root.geometry("800x600")

    # Input variables
    iterations_var = tk.StringVar(value="3")
    scale_var = tk.StringVar(value="5")
    perimeter_var = tk.StringVar(value="Perímetro: N/A")
    area_var = tk.StringVar(value="Área: N/A")

    # Create input frame
    input_frame = ttk.Frame(root)
    input_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

    ttk.Label(input_frame, text="Iteraciones:").pack(side=tk.LEFT, padx=5)
    ttk.Entry(input_frame, textvariable=iterations_var, width=5).pack(side=tk.LEFT, padx=5)

    ttk.Label(input_frame, text="Escala:").pack(side=tk.LEFT, padx=5)
    ttk.Entry(input_frame, textvariable=scale_var, width=5).pack(side=tk.LEFT, padx=5)

    generate_button = ttk.Button(input_frame, text="Generar", command=update_plot)
    generate_button.pack(side=tk.LEFT, padx=10)

    error_label = ttk.Label(input_frame, text="", foreground="red")
    error_label.pack(side=tk.LEFT, padx=10)

    # Display perimeter and area
    ttk.Label(root, textvariable=perimeter_var).pack(pady=5)
    ttk.Label(root, textvariable=area_var).pack(pady=5)

    # Create plot frame
    figure, ax = plt.subplots(figsize=(6, 6))
    canvas = FigureCanvasTkAgg(figure, master=root)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Start the GUI loop
    root.mainloop()


# #===============================================================================================================
# #===============================================================================================================

# GUI CONJUNTO DE MANDELBROT

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
    ventana = Toplevel()
    ventana.title("Conjunto de Mandelbrot")

    # Configurar la ventana en pantalla completa
    ventana.attributes('-fullscreen', True)

    # Cambiar el fondo de la ventana a gris oscuro
    ventana.config(bg='#2e2e2e')

    # Etiqueta para iteraciones
    label_iteraciones = Label(ventana, text=f"Iteraciones: {max_iteraciones}", font=("Arial", 14), bg='#2e2e2e', fg='white')
    label_iteraciones.pack(pady=10)

    # Botones para iteraciones
    frame_iteraciones = Frame(ventana, bg='#2e2e2e')
    frame_iteraciones.pack()

    boton_sumar = Button(frame_iteraciones, text="+", command=lambda: sumar_iteracion(label_iteraciones, figura, canvas, label_area), width=4, height=1, font=("Arial", 12))
    boton_sumar.grid(row=0, column=0, padx=10)

    boton_restar = Button(frame_iteraciones, text="-", command=lambda: restar_iteracion(label_iteraciones, figura, canvas, label_area), width=4, height=1, font=("Arial", 12))
    boton_restar.grid(row=0, column=1, padx=10)

    # Etiquetas y entradas para el rango del conjunto
    frame_rango = Frame(ventana, bg='#2e2e2e')
    frame_rango.pack(pady=10)

    label_x_min = Label(frame_rango, text="X min:", font=("Arial", 12), bg='#2e2e2e', fg='white')
    label_x_min.grid(row=0, column=0)
    entry_x_min = Entry(frame_rango, font=("Arial", 12))
    entry_x_min.insert(0, f"{x_min}")
    entry_x_min.grid(row=0, column=1)

    label_x_max = Label(frame_rango, text="X max:", font=("Arial", 12), bg='#2e2e2e', fg='white')
    label_x_max.grid(row=1, column=0)
    entry_x_max = Entry(frame_rango, font=("Arial", 12))
    entry_x_max.insert(0, f"{x_max}")
    entry_x_max.grid(row=1, column=1)

    label_y_min = Label(frame_rango, text="Y min:", font=("Arial", 12), bg='#2e2e2e', fg='white')
    label_y_min.grid(row=2, column=0)
    entry_y_min = Entry(frame_rango, font=("Arial", 12))
    entry_y_min.insert(0, f"{y_min}")
    entry_y_min.grid(row=2, column=1)

    label_y_max = Label(frame_rango, text="Y max:", font=("Arial", 12), bg='#2e2e2e', fg='white')
    label_y_max.grid(row=3, column=0)
    entry_y_max = Entry(frame_rango, font=("Arial", 12))
    entry_y_max.insert(0, f"{y_max}")
    entry_y_max.grid(row=3, column=1)

    boton_cambiar_rango = Button(frame_rango, text="Cambiar Rango", command=lambda: cambiar_rango(entry_x_min, entry_x_max, entry_y_min, entry_y_max, label_area, figura, canvas), width=20, height=1, font=("Arial", 12))
    boton_cambiar_rango.grid(row=4, column=0, columnspan=2, pady=10)

    # Etiqueta para los puntos dentro del conjunto
    label_area = Label(ventana, text="Puntos dentro: 0", font=("Arial", 14), bg='#2e2e2e', fg='white')
    label_area.pack(pady=10)

    # Espacio para el gráfico
    frame_grafico = Frame(ventana, bg='#2e2e2e')
    frame_grafico.pack()

    # Crear el gráfico con Matplotlib
    figura = Figure(figsize=(6, 6), dpi=100)
    canvas = FigureCanvasTkAgg(figura, master=frame_grafico)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    # Botón de cerrar en la parte inferior
    boton_cerrar = Button(ventana, text="Volver", command=ventana.destroy, font=("Arial", 14), width=20, fg='black', bg='white')
    boton_cerrar.pack(side='bottom', pady=20)

    # Actualizar la GUI por primera vez
    actualizar_gui(label_iteraciones, figura, canvas, label_area)

    # Ejecutar la ventana
    ventana.mainloop()
# # ======================================================================================================================================================================
# # ======================================================================================================================================================================

# Función para abrir la ventana de Sierpinski
def abrir_sierpinski(generar_puntos_sierpinski, calcular_area_sierpinski, N, l, color, A, B, C):
    # Llamar a la función crear_gui
    gui_triangulo_sierpinski(generar_puntos_sierpinski, calcular_area_sierpinski, N, l, color, A, B, C)

# Función para abrir una ventana de información
def abrir_mandelbrot(generar_conjunto_func, contar_puntos_dentro_func, plano_inicial, resolucion_inicial, iteraciones_iniciales):
    crear_gui_mandelbrot (generar_conjunto_func, contar_puntos_dentro_func, plano_inicial, resolucion_inicial, iteraciones_iniciales)

# Función para abrir una ventana de configuración
def abrir_configuracion():
    ventana_configuracion = Toplevel()
    ventana_configuracion.title("Configuración")
    label_config = Label(ventana_configuracion, text="Aquí puedes configurar los parámetros.", font=("Arial", 12))
    label_config.pack(pady=20)
    boton_cerrar = Button(ventana_configuracion, text="Cerrar", command=ventana_configuracion.destroy, font=("Arial", 12))
    boton_cerrar.pack(pady=10)

# Función que crea la ventana principal con los botones
def pantalla_principal(generar_puntos_sierpinski, calcular_area_sierpinski, N, l, color, A, B, C, generar_conjunto_mandelbrot, contar_puntos_dentro, plano_inicial, resolucion_inicial, iteraciones_iniciales):
    ventana_principal = Tk()
    ventana_principal.title("Pantalla Principal")
    
    # Ventana a pantalla completa
    ventana_principal.attributes('-fullscreen', True)

    # Configurar el color de fondo gris oscuro
    ventana_principal.configure(bg='#2e2e2e')  # Gris oscuro

    # Etiqueta de bienvenida
    label_bienvenida = Label(ventana_principal, text="PEI 3 - Bienvenido, a nuestro trabajo", font=("Arial", 14), fg='white', bg='#2e2e2e')
    label_bienvenida.pack(pady=20)

    # Segunda etiqueta debajo de la primera
    label_sub_bienvenida = Label(ventana_principal, text="En este programa se estudiarán de forma gráfica algunos de los fractales más conocidos y algunas de sus características así como el perímetro o el área.", font=("Arial", 12), fg='white', bg='#2e2e2e')
    label_sub_bienvenida.pack(pady=10)

    # Quinto botón (ubicado arriba de los otros tres)
    boton_quinto = Button(ventana_principal, text="Información relativa a los fractales y la motivación de nuestro trabajo", font=("Arial", 14), width=60, fg='black', bg='white')
    boton_quinto.pack(pady=10)

    # Etiqueta debajo del quinto botón
    label_bajo_quinto = Label(ventana_principal, text="Por favor, escoja uno de los siguientes fractales:", font=("Arial", 12), fg='white', bg='#2e2e2e')
    label_bajo_quinto.pack(pady=10)

    # Crear los otros tres botones
    boton_sierpinski = Button(ventana_principal, text="Triángulo de Sierpinski", command=lambda: abrir_sierpinski(generar_puntos_sierpinski, calcular_area_sierpinski, N, l, color, A, B, C), font=("Arial", 14), width=20, fg='black', bg='white')
    boton_sierpinski.pack(pady=10)

    boton_info = Button(ventana_principal, text="Conjunto de Mandelbrot", command=lambda:abrir_mandelbrot(generar_conjunto_mandelbrot, contar_puntos_dentro, plano_inicial, resolucion_inicial, iteraciones_iniciales), font=("Arial", 14), width=20, fg='black', bg='white')
    boton_info.pack(pady=10)

    boton_configuracion = Button(ventana_principal, text="Copo de nieve de Koch", command=abrir_configuracion, font=("Arial", 14), width=20, fg='black', bg='white')
    boton_configuracion.pack(pady=10)

    # Etiquetas encima del botón de cerrar (antes de cerrar la ventana)
    label_encima_cerrar_1 = Label(ventana_principal, text="Trabajo realizado por: Eduardo Gómez Oliva, no me sé vuestros apellidos ", font=("Arial", 12), fg='white', bg='#2e2e2e')
    label_encima_cerrar_1.pack(pady=10)

    label_encima_cerrar_2 = Label(ventana_principal, text="Esperemos que te haya gustado", font=("Arial", 12), fg='white', bg='#2e2e2e')
    label_encima_cerrar_2.pack(pady=10)

    # Botón de cerrar (ubicado al final)
    boton_cerrar = Button(ventana_principal, text="Cerrar", command=ventana_principal.destroy, font=("Arial", 14), width=20, fg='black', bg='white')
    boton_cerrar.pack(side='bottom', pady=10)

    # Ejecutar la ventana principal
    ventana_principal.mainloop()

