import tkinter as tk

def conversor():
    try:
        centimetros = float(entry_centimetros.get())
        pulgadas = centimetros / 2.54
        pies = centimetros / 30.48
        label_resultado_pulgadas.config(text=(f"La longitud en pulgadas es: {pulgadas: .2f} in."))
        label_resultado_pies.config(text=(f"La longitud en pies es: {pies: .2f} ft."))
    except:
        label_resultado_pulgadas.config(text="Por favor, ingrese una longitud válida.")

ventana = tk.Tk()
ventana.title("Conversor de longitudes")

label_instrucciones = tk.Label(ventana, text="Ingrese los centimetros: ")
label_instrucciones.pack()

entry_centimetros = tk.Entry(ventana)
entry_centimetros.pack()

boton_convertir = tk.Button(ventana,text="convertir",command=conversor)
boton_convertir.pack()

label_resultado_pulgadas = tk.Label(ventana,text="")
label_resultado_pulgadas.pack()

label_resultado_pies = tk.Label(ventana,text="")
label_resultado_pies.pack()

ventana.mainloop()