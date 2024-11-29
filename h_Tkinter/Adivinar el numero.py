import tkinter as tk
import random

class AdivinarNumero():
    def __init__(self,ventana):
        self.ventana = ventana
        self.numero_random = random.randint(1,100)
        
        self.intentos = 0
        self.instruccion=tk.Label(ventana,text="Ingrese un numero entre 1 y 100")
        self.instruccion.pack()
        self.entrada=tk.Entry(ventana)
        self.entrada.pack()
        self.adivinar=tk.Button(ventana,text="ADIVINAR",command=self.verificar)
        self.adivinar.pack()
        self.resultado_label=tk.Label(ventana,text=(""))
        self.resultado_label.pack()

    def verificar(self):
        ingreso = int(self.entrada.get())
        self.intentos+=1
        
        if(ingreso > self.numero_random):
            resultado = "Más bajo"
        elif(ingreso < self.numero_random):
            resultado = "Más alto"
        else:
            resultado = f"Correcto!. El numero era {self.numero_random}. Intentos hechos: {self.intentos}"
            self.adivinar.config(state="disabled")
        self.resultado_label.config(text=resultado)

ventana = tk.Tk()
app = AdivinarNumero(ventana)
ventana.geometry("300x100")

ventana.mainloop()