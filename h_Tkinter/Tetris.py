import tkinter as tk
import random
from tkinter import messagebox as mb
import time

# Dimensiones del tablero de juego
ANCHO = 10  # Número de columnas del tablero
ALTO = 20   # Número de filas del tablero

# Velocidad de caída inicial de las piezas (en milisegundos)
VELOCIDAD_CAIDA_INICIAL = 500

# Clase principal que representa el juego Tetris
class TetrisApp:
    def __init__(self, root):
        # Inicialización de la ventana principal del juego
        self.root = root
        self.root.title("Tetris")
        
        # Creación del tablero, que es una matriz de 0's de tamaño ANCHO x ALTO
        self.tablero = [[0] * ANCHO for _ in range(ALTO)]
        self.pieza_actual = None  # Variable que almacenará la pieza que está cayendo
        self.color_actual = None  # Color de la pieza actual
        self.timer_id = None  # Almacena el temporizador de la caída automática
        self.direccion = None  # Variable para controlar la dirección de movimiento de la pieza
        self.rotar = False  # Controla la rotación de las piezas
        self.puntaje = 0  # Almacena el puntaje del jugador
        
        # Velocidad de caída inicial
        self.velocidad_caida = VELOCIDAD_CAIDA_INICIAL

        # Colores posibles para las piezas
        self.colores = ["purple"]
        
        # Creación del canvas donde se dibujará el tablero y las piezas
        self.canvas = tk.Canvas(root, width=ANCHO * 30, height=ALTO * 30, bg="black")
        self.canvas.pack()  # Empaqueta el canvas en la ventana
        
        # Crear una etiqueta para mostrar el puntaje
        self.label_puntaje = tk.Label(root, text=f"Puntaje: {self.puntaje}", font=("Arial", 12), bg="black", fg="white")
        self.label_puntaje.pack()

        # Hacer que el canvas reciba eventos del teclado
        self.canvas.focus_set()

        # Asignación de las teclas para mover las piezas
        self.root.bind("<Left>", self.mover_izquierda)  # Tecla izquierda mueve la pieza hacia la izquierda
        self.root.bind("<Right>", self.mover_derecha)   # Tecla derecha mueve la pieza hacia la derecha
        self.root.bind("<Down>", self.mover_abajo)      # Tecla abajo acelera la caída de la pieza
        self.root.bind("<Up>", self.rotar_pieza)        # Tecla arriba rota la pieza
        
        # Crear la primera pieza y actualizar el tablero visualmente
        self.crear_pieza()
        self.actualizar_tablero()
        
        # Iniciar el juego
        self.iniciar_juego()
        
    def crear_pieza(self):
        # Definir las posibles piezas (tetrominós)
        piezas = [
            [[1, 1, 1, 1]],  # Pieza en línea
            [[1, 1], [1, 1]],  # Cuadrado
            [[1, 1, 1], [0, 1, 0]],  # Pieza en T
            [[1, 1, 1], [1, 0, 0]],  # L invertida
            [[1, 1, 1], [0, 0, 1]],  # L
            [[1, 1, 0], [0, 1, 1]],  # Z
            [[0, 1, 1], [1, 1, 0]]   # S
        ]
        # Elegir una pieza aleatoria
        self.pieza_actual = random.choice(piezas)
        # Asignar un color aleatorio a la pieza
        self.color_actual = random.choice(self.colores)
        # Posicionar la pieza en el centro horizontal del tablero
        self.x_pieza = ANCHO // 2 - len(self.pieza_actual[0]) // 2
        # Posicionar la pieza en la parte superior del tablero
        self.y_pieza = 0

    def temporizador(segundos):
        while segundos > 0:
            mins, secs = divmod(segundos, 60)  # Convierte los segundos a minutos y segundos
            tiempo_formateado = '{:02}:{:02}'.format(mins, secs)
            print(tiempo_formateado, end='\r')  # Muestra el tiempo de forma dinámica en la misma línea
            time.sleep(1)  # Espera 1 segundo
            segundos -= 1
        
        print("¡Tiempo agotado!")

    def actualizar_tablero(self):
        # Borrar el contenido anterior del canvas
        self.canvas.delete("all")
        
        # Dibujar las piezas ya fijadas en el tablero
        for y, fila in enumerate(self.tablero):
            for x, valor in enumerate(fila):
                if valor:  # Si hay una parte de una pieza en esa posición
                    self.canvas.create_rectangle(x * 30, y * 30, (x + 1) * 30, (y + 1) * 30, fill="purple")

        # Dibujar la pieza actual que está cayendo (con color aleatorio)
        for y, fila in enumerate(self.pieza_actual):
            for x, valor in enumerate(fila):
                if valor:  # Si hay una parte de la pieza en esa posición
                    self.canvas.create_rectangle((x + self.x_pieza) * 30, (y + self.y_pieza) * 30,
                                                 (x + self.x_pieza + 1) * 30, (y + self.y_pieza + 1) * 30, fill=self.color_actual)
        
    def actualizar_puntaje(self):
        # Actualizar el puntaje en la etiqueta
        self.label_puntaje.config(text=f"Puntaje: {self.puntaje}")

    # Ajustar la velocidad de caída en función del puntaje
    def ajustar_velocidad(self):
        # A medida que el puntaje aumenta, la velocidad de caída se reduce
        self.velocidad_caida = max(100, VELOCIDAD_CAIDA_INICIAL + (self.puntaje // 500) * 50)

    # Movimiento hacia la izquierda
    def mover_izquierda(self, event):
        if self.puede_mover(-1, 0):  # Verificar si la pieza puede moverse a la izquierda
            self.x_pieza -= 1  # Actualizar la posición
            self.actualizar_tablero()  # Redibujar el tablero

    # Movimiento hacia la derecha
    def mover_derecha(self, event):
        if self.puede_mover(1, 0):  # Verificar si la pieza puede moverse a la derecha
            self.x_pieza += 1  # Actualizar la posición
            self.actualizar_tablero()  # Redibujar el tablero

    # Movimiento hacia abajo
    def mover_abajo(self, event):
        if self.puede_mover(0, 1):  # Verificar si la pieza puede moverse hacia abajo
            self.y_pieza += 1  # Acelerar la caída
            self.actualizar_tablero()  # Redibujar el tablero

    # Rotación de la pieza
    def rotar_pieza(self, event):
        # Rotar la pieza 90 grados
        pieza_rotada = list(zip(*reversed(self.pieza_actual)))
        if self.puede_rotar(pieza_rotada):  # Verificar si la rotación es válida
            self.pieza_actual = pieza_rotada  # Actualizar la pieza con su nueva forma rotada
            self.actualizar_tablero()  # Redibujar el tablero

    # Verificación si la pieza puede moverse a una nueva posición
    def puede_mover(self, dx, dy):
        for y, fila in enumerate(self.pieza_actual):
            for x, valor in enumerate(fila):
                if valor:  # Si es una parte de la pieza
                    nuevo_x = x + self.x_pieza + dx  # Nueva posición X
                    nuevo_y = y + self.y_pieza + dy  # Nueva posición Y
                    # Verificar si la nueva posición está fuera del tablero o colisiona con otra pieza
                    if (nuevo_x < 0 or nuevo_x >= ANCHO or nuevo_y >= ALTO or
                            (nuevo_y >= 0 and self.tablero[nuevo_y][nuevo_x])):
                        return False  # No puede moverse
        return True  # Puede moverse

    # Verificación si la pieza puede rotar sin colisionar
    def puede_rotar(self, nueva_pieza):
        for y, fila in enumerate(nueva_pieza):
            for x, valor in enumerate(fila):
                if valor:  # Si es una parte de la pieza
                    nuevo_x = x + self.x_pieza  # Nueva posición X
                    nuevo_y = y + self.y_pieza  # Nueva posición Y
                    # Verificar si la rotación estaría fuera del tablero o colisionaría
                    if (nuevo_x < 0 or nuevo_x >= ANCHO or nuevo_y >= ALTO or
                            (nuevo_y >= 0 and self.tablero[nuevo_y][nuevo_x])):
                        return False  # No puede rotar
        return True  # Puede rotar

    # Fija la pieza actual en el tablero cuando ya no puede moverse más
    def fijar_pieza(self):
        for y, fila in enumerate(self.pieza_actual):
            for x, valor in enumerate(fila):
                if valor:  # Si es una parte de la pieza
                    self.tablero[y + self.y_pieza][x + self.x_pieza] = 1  # Fijar la pieza en el tablero

    # Elimina las filas completas del tablero y actualiza el puntaje
    def eliminar_filas_completas(self):
        filas_completas = []  # Almacena las filas que están completas
        for y, fila in enumerate(self.tablero):
            if all(fila):  # Si la fila está llena
                filas_completas.append(y)  # Añadir la fila completa a la lista
        for y in filas_completas:
            del self.tablero[y]  # Eliminar la fila completa
            self.tablero.insert(0, [0] * ANCHO)  # Insertar una fila vacía en la parte superior
        # Aumentar el puntaje en función de cuántas filas se han eliminado
        self.puntaje += len(filas_completas) * 100  # 100 puntos por cada fila eliminada
        self.actualizar_puntaje()  # Actualizar el puntaje visualmente
        self.ajustar_velocidad()  # Ajustar la velocidad de caída según el puntaje

    # Control de la caída automática de la pieza
    def caida_automatica(self):
        if self.puede_mover(0, 1):  # Verificar si la pieza puede caer
            self.y_pieza += 1  # Mover la pieza hacia abajo
            self.actualizar_tablero()  # Redibujar el tablero
            self.canvas.create_rectangle(x * 30, y * 30, (x + 1) * 30, (y + 1) * 30, fill="black")
        else:
            self.fijar_pieza()  # Fijar la pieza en el tablero
            self.eliminar_filas_completas()  # Eliminar las filas completas
            self.crear_pieza()  # Crear una nueva pieza
            # Verificar si la nueva pieza puede aparecer en el tablero
            if not self.puede_mover(0, 0):  # Si no puede moverse, significa que no hay espacio
                mb.showinfo("Fin del Juego", f"Has llenado el tablero.Tu Puntaje final es: {self.puntaje} puntos." )  # Mostrar mensaje de fin de juego con el puntaje final
                self.root.quit()  # Cerrar el juego
                return
        # Programar la siguiente caída automática con la nueva velocidad
        self.timer_id = self.root.after(self.velocidad_caida, self.caida_automatica)

    # Iniciar el ciclo de caída automática
    def iniciar_juego(self):
        self.caida_automatica()

# Crear ventana principal y ejecutar el juego
root = tk.Tk()
app = TetrisApp(root)
root.mainloop()  # Iniciar el bucle de eventos de tkinter