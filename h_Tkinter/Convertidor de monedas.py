import tkinter as tk
import requests

class ConversorMonedasApp():
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Conversor de monedas")
        
        self.label_titulo = tk.Label(ventana,text="Convertidor de monedas")
        self.label_titulo.pack()
        self.entry_monto = tk.Entry(ventana)
        self.entry_monto.pack()
                
        self.label_origen = tk.Label(ventana, text="Moneda de origen: ")
        self.label_origen.pack()
        self.combo_origen = tk.StringVar()
        self.combo_origen.set("USD")
        self.entry_origen = tk.Entry(ventana, textvariable=self.combo_origen)
        self.entry_origen.pack()
        
        self.label_destino = tk.Label(ventana, text="Moneda destino: ")
        self.label_destino.pack()
        self.combo_destino = tk.StringVar()
        self.combo_destino.set("ARS")
        self.entry_destino = tk.Entry(ventana, textvariable=self.combo_destino)
        self.entry_destino.pack()
        
        self.label_resultado = tk.Label(ventana, text="")
        self.label_resultado.pack()
        
        self.boton_convertir = tk.Button(ventana, text="Convertir", command=self.conversor)
        self.boton_convertir.pack()
        
    def conversor(self):
        monto = self.entry_monto.get()
        moneda_Origen = self.combo_origen.get()
        moneda_Destino = self.combo_destino.get()
        
        url = f"https://api.exchangerate-api.com/v4/latest/{moneda_Origen}"
        response = requests.get(url)
        data = response.json()
        
        if moneda_Destino in data["rates"]:
            tasa_conversion = data["rates"][moneda_Destino]
            monto_convertido = float(monto) * tasa_conversion
            self.label_resultado.config(text=f"{monto} {moneda_Origen} = {monto_convertido: .2f} {moneda_Destino}")
        else:
            self.label_resultado.config(text="Moneda no válida.")

ventana = tk.Tk()
ventana.geometry("250x300")
app = ConversorMonedasApp(ventana)
ventana.mainloop()
