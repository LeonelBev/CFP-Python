import tkinter as tk

def conversor():
    try:
        kilometros = float(entry_kilometros.get())
        millas = kilometros*0.621371
        label_resultado.config(text=f"La conversión a millas es: {millas}")
    except:
        label_resultado.config(text="Por favor, ingrese un valor válido.")
        
ventana = tk.Tk()
ventana.title("Convertidor de KM a MILE")

label_instruccion  = tk.Label(ventana,text="Ingrese los kilómetros a convertir:")
label_instruccion.pack()

entry_kilometros = tk.Entry(ventana)
entry_kilometros.pack()

boton_convertir = tk.Button(ventana,text="Convertir", command=conversor)
boton_convertir.pack()

label_resultado = tk.Label(ventana,text="")
label_resultado.pack()

ventana.mainloop()
