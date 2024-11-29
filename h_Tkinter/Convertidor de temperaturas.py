import tkinter as tk

def conversor():
    celsius = float(entry_celcius.get())
    fahrenheit = celsius*9/5+32
    label_resultado.config(text=f"La temperatura convertida a ahrenheit es: {fahrenheit: .2f}")

ventana=tk.Tk()
ventana.title("Convertidor de temperaturas")

label_instruccion = tk.Label(ventana,text="Ingrese la temperatura en celcius: ")
label_instruccion.pack()

entry_celcius = tk.Entry(ventana)
entry_celcius.pack()

boton_convertir = tk.Button(ventana, text="Convertir",command=conversor)
boton_convertir.pack()

label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

ventana.mainloop()
