import tkinter as tk

#Ventana
root = tk.Tk()

#Titulo ventana
root.title("Hola mundo con Tkinter.")

#Tamaño ventana
root.geometry("300x300")

#Crear etiqueta
label = tk.Label(root, text="Hola mundo.")
label.pack(expand=True)
label.configure(label,justify="left")

#Ejecutar ventana en bucle
root.mainloop()