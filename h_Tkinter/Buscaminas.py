import tkinter as tk
import random

class BuscaminasApp:
    def __init__(self, root):
        # Constructor, inicializa la interfaz y la lógica del juego

        self.root = root
        self.root.title("Buscaminas")

        self.filas = 10  # Número de filas
        self.columnas = 10  # Número de columnas
        self.minas = 10  # Número total de minas

        # Crear un diccionario para almacenar los botones
        self.botones = {}
        self.marcadas = 0  # Contador de cuántas minas están marcadas
        self.juego_terminado = False  # Indica si el juego ha terminado

        # Crear etiqueta para mostrar cuántas minas faltan por encontrar
        self.label_minas_restantes = tk.Label(self.root, text=f"Minas restantes: {self.minas}")
        self.label_minas_restantes.grid(row=0, column=0, columnspan=self.columnas)

        # Crear botón para reiniciar el juego
        self.boton_reiniciar = tk.Button(self.root, text="Reiniciar", command=self.reiniciar_juego)
        self.boton_reiniciar.grid(row=1, column=0, columnspan=self.columnas)

        # Crear una cuadrícula con botones
        for fila in range(self.filas):
            for columna in range(self.columnas):
                # Crear cada botón y almacenarlo en el diccionario
                boton = tk.Button(self.root, width=3, height=1,command=lambda f=fila, c=columna: self.revelar(f, c),font=("Roboto Cn",14))
                boton.grid(row=fila + 2, column=columna)  # Fila + 2 para dejar espacio para las etiquetas
                boton.bind("<Button-3>", lambda event, f=fila, c=columna: self.marcar(f, c))
                self.botones[(fila, columna)] = boton

        # Inicializar el tablero con minas y números
        self.tablero = self.generar_tablero()

    def generar_tablero(self):
        # Generar un tablero con minas y números indicando cuántas minas hay alrededor

        # Crear un tablero vacío
        tablero = [[0 for _ in range(self.columnas)] for _ in range(self.filas)]

        # Colocar minas aleatoriamente
        minas_colocadas = 0
        while minas_colocadas < self.minas:
            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)
            if tablero[fila][columna] != -1:
                tablero[fila][columna] = -1  # Colocar mina (-1)
                minas_colocadas += 1

                # Incrementar el conteo en las celdas adyacentes a la mina
                for i in range(max(0, fila - 1), min(self.filas, fila + 2)):
                    for j in range(max(0, columna - 1), min(self.columnas, columna + 2)):
                        if tablero[i][j] != -1:
                            tablero[i][j] += 1

        return tablero

    def revelar(self, fila, columna):
        # Revelar la celda seleccionada por el jugador

        if self.juego_terminado:
            return  # Si el juego ha terminado, no hacer nada

        boton = self.botones[(fila, columna)]  # Obtener el botón correspondiente

        # Si es una mina, el jugador pierde
        if self.tablero[fila][columna] == -1:
            boton.config(text="X", bg="red")
            self.fin_del_juego(False)  # Terminar el juego (jugador pierde)
        else:
            # Si no es una mina, mostrar el número de minas cercanas
            if self.tablero[fila][columna] > 0:
                boton.config(text=str(self.tablero[fila][columna]), state="disabled", relief=tk.SUNKEN)
            else:
                # Si es un 0, dejar la celda vacía
                boton.config(text="", state="disabled", relief=tk.SUNKEN)

                # Revelar las celdas adyacentes si es 0
                for i in range(max(0, fila - 1), min(self.filas, fila + 2)):
                    for j in range(max(0, columna - 1), min(self.columnas, columna + 2)):
                        if self.botones[(i, j)]["state"] != "disabled":
                            self.revelar(i, j)

            # Si el jugador revela todas las celdas sin minas, gana
            if self.chequear_victoria():
                self.fin_del_juego(True)  # Terminar el juego (jugador gana)

    def marcar(self, fila, columna):
        # Marcar o desmarcar un lugar como posible mina con clic derecho

        if self.juego_terminado:
            return  # Si el juego ha terminado, no hacer nada

        boton = self.botones[(fila, columna)]  # Obtener el botón correspondiente

        if boton["text"] == "F":  # Si ya está marcada, desmarcarla
            boton.config(text="")
            self.marcadas -= 1
        elif boton["state"] == "normal":  # Si no está deshabilitada, marcarla como "F"
            boton.config(text="F", fg="red")
            self.marcadas += 1

        # Actualizar el número de minas restantes
        self.label_minas_restantes.config(text=f"Minas restantes: {self.minas - self.marcadas}")

    def chequear_victoria(self):
        # Verificar si el jugador ha ganado

        for (fila, columna), boton in self.botones.items():
            # Si hay un botón que no es mina y no ha sido revelado, aún no ha ganado
            if self.tablero[fila][columna] != -1 and boton["state"] != "disabled":
                return False
        return True  # El jugador ha revelado todas las celdas sin minas

    def fin_del_juego(self, victoria):
        # Terminar el juego y desactivar todos los botones

        self.juego_terminado = True  # Marcar el juego como terminado

        for boton in self.botones.values():
            boton.config(state="disabled")  # Desactivar todos los botones

        # Mostrar un mensaje dependiendo del resultado
        if victoria:
            self.label_minas_restantes.config(text="¡Has ganado!")
        else:
            self.label_minas_restantes.config(text="¡Has perdido!")

    def reiniciar_juego(self):
        # Reiniciar el juego para una nueva partida

        # Reiniciar variables de estado
        self.marcadas = 0
        self.juego_terminado = False
        self.label_minas_restantes.config(text=f"Minas restantes: {self.minas}")

        # Reiniciar el tablero y los botones
        self.tablero = self.generar_tablero()

        for (fila, columna), boton in self.botones.items():
            boton.config(text="", state="normal", bg="SystemButtonFace", relief=tk.RAISED)

# Crear la ventana principal
root = tk.Tk()

# Crear una instancia del juego Buscaminas
app = BuscaminasApp(root)

# Iniciar el bucle principal de la ventana
root.mainloop()