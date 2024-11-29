import tkinter as tk

def convertor_Galon():
    try:
        galones = float(entrada.get())
        litros = galones*3.78541
        label_resultado.config(text=f"La conversión a litros es: {litros: .4f}")
    except:
        label_resultado.config(text="Por favor, ingrese un valor válido.")
     
def convertor_Litro():
    try:
        litros = float(entrada.get())
        galones = litros/3.785
        label_resultado.config(text=f"La conversión a galones es: {galones: .4f}") 
    except:
        label_resultado.config(text="Por favor, ingrese un valor válido.")
       
ventana = tk.Tk()
ventana.title("Convertidor de Galon a Litro")

ventana.geometry("250x300")

label_instruccion  = tk.Label(ventana,text="Ingrese los galones/litros a convertir:")
label_instruccion.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton_convertir_galon = tk.Button(ventana,text="Galones a litros", command=convertor_Galon)
boton_convertir_galon.pack()

boton_convertir_litro = tk.Button(ventana, text="Litros a galones", command=convertor_Litro)
boton_convertir_litro.pack()

label_resultado = tk.Label(ventana,text="")
label_resultado.pack()

ventana.mainloop()