from tkinter import messagebox, Frame, Label, Button, Tk, Scale, Entry, Toplevel, BOTH
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

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

    def actualizar_gui(label_N, label_l, figura, canvas, label_a):  
        # Actualiza la interfaz gráfica con la información actualizada de iteraciones y longitud del lado

        label_N.config(text=f"Iteraciones: {N}")            # Actualiza el texto de la etiqueta para mostrar el número actual de iteraciones
        label_l.config(text=f"Longitud Lado: {l:.2f}")      # Actualiza la etiqueta con la longitud del lado con 2 decimales
        actualizar_triangulo(figura, canvas, label_a)       # Llama a la función que redibuja el triángulo en el lienzo

    def sumar_N(label_N, label_l, figura, canvas, label_a):  
        # Incrementa el número de iteraciones y actualiza la interfaz gráfica.

        nonlocal N                                                 # modifica la variable N (iteraciones) definida fuera del ámbito de esta función
        N += 1   
        actualizar_gui(label_N, label_l, figura, canvas, label_a)  # Actualiza la interfaz gráfica y redibuja el triángulo

    def restar_N(label_N, label_l, figura, canvas, label_a):  
        # Decrementa el número de iteraciones, sin bajar del cero

        nonlocal N                          # Permite modificar el número de iteraciones
        if N > 0:                           # Verifica que N no sea menor que 0 antes de restar
            N -= 1                          # Disminuye el valor de N en 1
        actualizar_gui(label_N, label_l, figura, canvas, label_a)                      # Actualiza la interfaz gráfica y redibuja el triángulo

    def cambiar_l(entry_l, label_l, figura, canvas, label_a):  
        # Cambia la longitud del lado en función al valor que se ingrese

        nonlocal l                                              # Permite modificar la longitud del lado
        try:
            l = float(entry_l.get())                            # Obtiene el valor ingresado en el cuadro de texto y lo convierte a un foat
            if l <= 0:                                          # Verifica que la longitud del lado sea mayor que 0
                raise ValueError                                # Error si no es asi

            actualizar_gui(label_N, label_l, figura, canvas, label_a)                  # Actualiza la interfaz gráfica y redibuja el triángulo.
        except ValueError:                                                             # Captura un error si la entrada no es válida (N<0)
            messagebox.showerror("Valor Inválido", "La longitud del lado debe ser un número mayor que 0.")  
            # Muestra un mensaje de error 
            entry_l.delete(0, 'end')                             # Borra el valor incorrecto 
            entry_l.insert(0, f"{l:.2f}")                        # Restaura el valor anterior 

    # Función para cambiar el color usando la barra deslizante
    def cambiar_color(valor):
        nonlocal color
        # Obtener el valor de la barra deslizante para rojo (R)
        rojo = int(valor)
        # El valor de azul (B) es complementario al rojo
        azul = 255 - rojo
        verde = 0  # No se cambia el verde
        color = f"#{rojo:02x}{verde:02x}{azul:02x}"  # Crear el color en formato hexadecimal
        actualizar_gui(label_N, label_l, figura, canvas, label_a)

    # Crear la ventana principal
    ventana = Tk()  # Inicializa una ventana principal de la aplicación.
    ventana.title("Triángulo de Sierpinski")  # Asigna un título a la ventana.

    # Ventana a pantalla completa
    ventana.attributes('-fullscreen', True)

    # Configurar el color de fondo gris oscuro
    ventana.configure(bg='#2e2e2e')  # Gris oscuro

    # Etiqueta para iteraciones
    label_N = Label(ventana, text=f"Iteraciones: {N}", font=("Arial", 14), fg='white', bg='#2e2e2e')
    label_N.pack(pady=10)   # Empaqueta la etiqueta con un margen superior e inferior de 10

    # Botones para iteraciones
    frame_N = Frame(ventana, bg='#2e2e2e')        # Crea un marco para organizar los botones
    frame_N.pack()                                # Empaqueta el marco dentro de la ventana principal

    boton_sumar = Button(frame_N, text="+", command=lambda: sumar_N(label_N, label_l, figura, canvas, label_a), width=4, height=1, font=("Arial", 12), fg='black', bg='white')
    boton_sumar.grid(row=0, column=0, padx=10)     # Ubica el botón en la primera columna del marco con un margen horizontal

    boton_restar = Button(frame_N, text="-", command=lambda: restar_N(label_N, label_l, figura, canvas, label_a), width=4, height=1, font=("Arial", 12), fg='black', bg='white')
    boton_restar.grid(row=0, column=1, padx=10)    # Ubica el botón en la segunda columna del marco con un margen horizontal
 
    # Etiqueta y entrada para la longitud del lado
    frame_l = Frame(ventana, bg='#2e2e2e')         # Crea un marco para organizar la etiqueta y la entrada de texto
    frame_l.pack(pady=10)                          # Empaqueta el marco con un margen vertical

    label_l = Label(frame_l, text=f"Longitud Lado: {l:.2f}", font=("Arial", 14), fg='white', bg='#2e2e2e')
    label_l.grid(row=0, column=0)

    # Entrada de texto para cambiar la longitud del lado

    entry_l = Entry(frame_l, font=("Arial", 12), width=8)
    entry_l.grid(row=0, column=1)
    entry_l.insert(0, f"{l:.2f}")

    # Botón para confirmar el cambio de longitud del lado

    boton_cambiar_l = Button(frame_l, text="Cambiar", command=lambda: cambiar_l(entry_l, label_l, figura, canvas, label_a), width=8, height=1, font=("Arial", 12), fg='black', bg='white')
    boton_cambiar_l.grid(row=0, column=2)

    # Etiqueta para el área
    label_a = Label(ventana, text="Área: 0.00000", font=("Arial", 14), fg='white', bg='#2e2e2e')
    label_a.pack(pady=10)

    # Espacio para el gráfico
    frame_grafico = Frame(ventana, bg='#2e2e2e')
    frame_grafico.pack()

    # Crear el gráfico con Matplotlib
    figura = Figure(figsize=(5, 5), dpi=100)  # Crea una figura Matplotlib con definido tamaño y resolución 
    canvas = FigureCanvasTkAgg(figura, master=frame_grafico)  # Vincula la figura con Tkinter para ser mostrada en la GUI
    canvas_widget = canvas.get_tk_widget()  # Convierte la figura en un widget compatible con Tkinter
    canvas_widget.pack()  # Empaqueta el widget para mostrar el gráfico

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
    root.attributes('-fullscreen', True)
    root.geometry("800x600")
    root.configure(bg='#2e2e2e')

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

    boton_cerrar = Button(root, text="Volver", command=root.destroy, font=("Arial", 14), width=20, fg='black', bg='white')
    boton_cerrar.pack(side='bottom', pady=20)

    # Start the GUI loop
    root.mainloop()


# #===============================================================================================================
# #===============================================================================================================

# GUI CONJUNTO DE MANDELBROT

#Función principal del programa, se definen los parámetros "generar conjunto", la función que genera el conjunto de Mandelbrot
 
def crear_gui_mandelbrot(generar_conjunto_func, contar_puntos_dentro_func, plano_inicial, resolucion_inicial, iteraciones_iniciales):   
    # Variables locales sincronizadas con main.py
    x_min, x_max, y_min, y_max = plano_inicial  #Conjunto de valores iniciales para el rango del plano
    resolucion = resolucion_inicial  #La resolución inicial para el rango del plano 
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
        ax.imshow(mandelbrot_matrix, cmap=color_mandelbrot, extent=(x_min, x_max, y_min, y_max))  #Dibujar la nueva imagen del conjunto, con el color seleccionado y el rango definido
        ax.set_title(f'Conjunto de Mandelbrot (Iteraciones: {max_iteraciones})')  #Función para incluir el número de iteraciones actuales en el título del gráfico
        ax.set_aspect('equal')  #Configura la relación de aspecto del gráfico, asegura que el conjunto se vea correctamente sin distorsión
        ax.axis('off') #Esta línea oculta los ejes del gráfico, mostrando solo la imagen del conjunto de Mandelbrot 
        canvas.draw()  #Actualizar la visualización en la interfaz gráfica

    def actualizar_gui(label_iteraciones, figura, canvas, label_area):  #Función que actualiza los elementos de la interfaz, como etiquetas y el gráfico
        label_iteraciones.config(text=f"Iteraciones: {max_iteraciones}")
        actualizar_mandelbrot(figura, canvas, label_area)   #Se muestra el gráfico con los valores actuales

    def sumar_iteracion(label_iteraciones, figura, canvas, label_area):  #Función que aumenta el número de iteraciones y actualiza la gui con el nuevo valor de iteraciones
        nonlocal max_iteraciones  #Sirve para decirle a python que max_ite no es una variable local
        max_iteraciones += 1
        actualizar_gui(label_iteraciones, figura, canvas, label_area)   #Se actualiza la gui con el nuevo valor de iteraciones

    def restar_iteracion(label_iteraciones, figura, canvas, label_area): #Disminuye el número de iteraciones pero no deja que sea negativo
        nonlocal max_iteraciones
        if max_iteraciones > 0:
            max_iteraciones -= 1
        actualizar_gui(label_iteraciones, figura, canvas, label_area)  #Se actualiza la gui con el nuevo valor de iteraciones

    def cambiar_rango(entry_x_min, entry_x_max, entry_y_min, entry_y_max, label_area, figura, canvas):   #Obtiene nuevos valores de rango de las entradas de texto y si los valores de entrada no son válidos muestra un mensaje de error
        nonlocal x_min, x_max, y_min, y_max
        try:
            x_min = float(entry_x_min.get())
            x_max = float(entry_x_max.get())
            y_min = float(entry_y_min.get())
            y_max = float(entry_y_max.get())
            actualizar_gui(label_iteraciones, figura, canvas, label_area)   #Se vuelve a dibujar el conjunto con el nuevo rango
        except ValueError:
            messagebox.showerror("Valor Inválido", "Los valores de rango deben ser números válidos.")

    # Crear la ventana principal
    ventana = Toplevel()
    ventana.title("Conjunto de Mandelbrot")

    # Configurar la ventana en pantalla completa
    ventana.attributes('-fullscreen', True)

    # Cambiar el fondo de la ventana a gris oscuro
    ventana.config(bg='#2e2e2e')

    # Etiqueta que muestra cuántas iteraciones se están dando
    label_iteraciones = Label(ventana, text=f"Iteraciones: {max_iteraciones}", font=("Arial", 14), bg='#2e2e2e', fg='white')
    label_iteraciones.pack(pady=10)

    # Botones para aumentar o disminuir iteraciones
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
    label_x_min.grid(row=0, column=0)   #Coloca los widgets en una cuadricula, lo coloca en la fila(row) 0 columna 0 de la cuadricula dentro de frame_rango
    entry_x_min = Entry(frame_rango, font=("Arial", 12))  #Se crea un campo de entrada donde el usuario puede escribir en ella
    entry_x_min.insert(0, f"{x_min}")  #Se establece un valor predeterminado en el campo de entrada "x min"
    entry_x_min.grid(row=0, column=1)  #Posicionamiento del campo de entrada dentro de frame_rango, justo al lado de la etiqueta "x_min"

    label_x_max = Label(frame_rango, text="X max:", font=("Arial", 12), bg='#2e2e2e', fg='white')  #Se hace lo mismo con la etiqueta de x_max
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

def gui_información_relativa_fractales():
    # Crear la ventana principal
    ventana = Tk()  
    ventana.title("Información sobre Fractales")  # Título de la ventana

    # Hacer que la ventana sea pantalla completa
    ventana.attributes('-fullscreen', True)  # pantalla completa

    # fondo gris oscuro
    ventana.config(bg="#2E2E2E")  

    # texto (Label) con información sobre fractales
    informacion = """
    Los fractales son estructuras geométricas que se repiten a diferentes escalas, con patrones auto-simililares que se
    encuentran en la naturaleza, como en las ramas de los árboles, las hojas de las plantas o las formaciones de montañas.
    El concepto de fractales fue desarrollado por Benoît B. Mandelbrot, quien abrió nuevas áreas en matemáticas, física y
    arte computacional. Los fractales tienen aplicaciones en diversas áreas, siendo fundamentales para estudiar fenómenos
    complejos y patrones repetitivos en sistemas naturales y artificiales.

    Entre los fractales más conocidos se encuentran el Triángulo de Sierpinski, el Copo de Nieve de Koch y el Conjunto de
    Mandelbrot. El Triángulo de Sierpinski se genera eliminando recursivamente el triángulo central de un triángulo equilátero,
    lo que da lugar a una figura auto-similar a diferentes escalas. El Copo de Nieve de Koch se construye dividiendo cada
    lado de un triángulo equilátero en tres segmentos y añadiendo un triángulo adicional en el centro, repitiendo este proceso
    recursivamente, lo que genera una figura compleja con cada iteración.

    El Conjunto de Mandelbrot es uno de los fractales más complejos, basado en una función iterativa con números complejos.
    A medida que se realiza un zoom en la figura, se descubren patrones auto-similares infinitos, y su frontera tiene una estructura
    fractal con una dimensión cercana a 2, lo que lo hace visualmente impresionante. La creación de estos fractales a través de
    programación permite explorar estos patrones de forma visual e interactiva.

    En este trabajo se implementarán estos tres fractales en Python, utilizando una interfaz gráfica de usuario (GUI) que
    permitirá al usuario visualizar los fractales, ajustar parámetros como el número de iteraciones y realizar zoom para
    explorar los detalles de cada uno. Esta experiencia proporcionará una comprensión más profunda de los fractales y sus
    aplicaciones, además de fortalecer las habilidades en programación y diseño de interfaces gráficas.
    """

    etiqueta = Label(ventana, text=informacion, font=("Arial", 15), bg="#2E2E2E", fg="white", justify="left", padx=20, pady=20)
    # fuente y estilo
    etiqueta.pack(fill=BOTH, expand=True)  # Expande el widget para llenar el espacio disponible

    # Botón "Volver" 
    boton_volver = Button(ventana, text="Volver", command=ventana.destroy, font=("Arial", 14), width=20, fg='black', bg='white')
    # Botón para cerrar la ventana al ser presionado
    boton_volver.pack(side='bottom', pady=20)  # Posiciona el botón al final de la ventana

    # Ejecutar la ventana
    ventana.mainloop()  # Inicia el bucle principal de la interfaz gráfica

def abrir_informacion_fractales():
    # Llama a la función que muestra la ventana con información sobre fractales
    gui_información_relativa_fractales()

def abrir_sierpinski(generar_puntos_sierpinski, calcular_area_sierpinski, N, l, color, A, B, C):
    # Abre una ventana para visualizar el Triángulo de Sierpinski
    gui_triangulo_sierpinski(generar_puntos_sierpinski, calcular_area_sierpinski, N, l, color, A, B, C)

def abrir_mandelbrot(generar_conjunto_func, contar_puntos_dentro_func, plano_inicial, resolucion_inicial, iteraciones_iniciales):
    # Abre una ventana para visualizar el Conjunto de Mandelbrot
    crear_gui_mandelbrot(generar_conjunto_func, contar_puntos_dentro_func, plano_inicial, resolucion_inicial, iteraciones_iniciales)

def abrir_koch(generate_koch, calculate_area, calculate_perimeter):
    # Abre una ventana para visualizar el Copo de Nieve de Koch
    create_gui_Koch(generate_koch, calculate_area, calculate_perimeter)

def pantalla_principal(generar_puntos_sierpinski, calcular_area_sierpinski, N, l, color, A, B, C, generar_conjunto_mandelbrot, contar_puntos_dentro, plano_inicial, resolucion_inicial, iteraciones_iniciales, generate_koch, calculate_area, calculate_perimeter):
    # Crear la ventana principal
    ventana_principal = Tk()  # Inicializa la ventana principal
    ventana_principal.title("Pantalla Principal")  # Título de la ventana

    # Ventana a pantalla completa
    ventana_principal.attributes('-fullscreen', True)  # Configura la ventana a pantalla completa

    # Configurar el color de fondo gris oscuro
    ventana_principal.configure(bg='#2e2e2e')  # Fondo gris oscuro

    # Etiqueta de bienvenida
    label_bienvenida = Label(ventana_principal, text="PEI 3 - Bienvenido, a nuestro trabajo", font=("Arial", 14), fg='white', bg='#2e2e2e')
    label_bienvenida.pack(pady=20)  # Posiciona la etiqueta con margen vertical

    # Segunda etiqueta debajo de la primera
    label_sub_bienvenida = Label(ventana_principal, text="En este programa se estudiarán de forma gráfica algunos de los fractales más conocidos y algunas de sus características así como el perímetro o el área.", font=("Arial", 12), fg='white', bg='#2e2e2e')
    label_sub_bienvenida.pack(pady=10)  # Posiciona la etiqueta con margen vertical

    # Botón para abrir la información sobre fractales
    boton_quinto = Button(ventana_principal, text="Información relativa a los fractales y la motivación de nuestro trabajo", font=("Arial", 14), width=60, fg='black', bg='white', command=abrir_informacion_fractales)
    boton_quinto.pack(pady=10)

    # Etiqueta instructiva
    label_bajo_quinto = Label(ventana_principal, text="Por favor, escoja uno de los siguientes fractales:", font=("Arial", 12), fg='white', bg='#2e2e2e')
    label_bajo_quinto.pack(pady=10)

    # Botones para cada fractal
    boton_sierpinski = Button(ventana_principal, text="Triángulo de Sierpinski", command=lambda: abrir_sierpinski(generar_puntos_sierpinski, calcular_area_sierpinski, N, l, color, A, B, C), font=("Arial", 14), width=20, fg='black', bg='white')
    boton_sierpinski.pack(pady=10)

    boton_info = Button(ventana_principal, text="Conjunto de Mandelbrot", command=lambda: abrir_mandelbrot(generar_conjunto_mandelbrot, contar_puntos_dentro, plano_inicial, resolucion_inicial, iteraciones_iniciales), font=("Arial", 14), width=20, fg='black', bg='white')
    boton_info.pack(pady=10)

    boton_configuracion = Button(ventana_principal, text="Copo de nieve de Koch", command=lambda: abrir_koch(generate_koch, calculate_area, calculate_perimeter), font=("Arial", 14), width=20, fg='black', bg='white')
    boton_configuracion.pack(pady=10)

    # Etiquetas de crédito
    label_encima_cerrar_1 = Label(ventana_principal, text="Trabajo realizado por: Eduardo Gómez, Lidia Lázaro, Weiwei Yang, Sandra García", font=("Arial", 12), fg='white', bg='#2e2e2e')
    label_encima_cerrar_1.pack(pady=10)

    label_encima_cerrar_2 = Label(ventana_principal, text="Esperemos que te haya gustado", font=("Arial", 12), fg='white', bg='#2e2e2e')
    label_encima_cerrar_2.pack(pady=10)

    # Botón para cerrar la ventana principal
    boton_cerrar = Button(ventana_principal, text="Cerrar", command=ventana_principal.destroy, font=("Arial", 14), width=20, fg='black', bg='white')
    boton_cerrar.pack(side='bottom', pady=10)

    # Ejecutar la ventana principal
    ventana_principal.mainloop()

    

# ======================================================
# ======================================================
# ======================================================
# ======================================================



