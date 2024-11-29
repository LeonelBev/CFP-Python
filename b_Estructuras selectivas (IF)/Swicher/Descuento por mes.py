switcher = {
    1:"Enero",
    2:"Febrero",
    3:"Marzo",
    4:"Abril",
    5:"Mayo",
    6:"Junio",
    7:"Julio",
    8:"Agosto",
    9:"Septiembre",
    10:"Octubre",
    11:"Noviembre",
    12:"Diciembre"
}
print("Ingrese el monto: ")
monto = float(input())
print("Ingrese la cantidad: ")
cantidad = int(input())
print("Mes de la compra realizada: ")
mesIngresado = int(input())
# diccionario.get(argumento, mensaje por defecto)
mes = switcher.get(mesIngresado, "Mes no válido")
if mes == "Octubre":
    precioDescuento = (monto*cantidad)*0.85
    print("Precio final con descuento: ", precioDescuento)
else:
    precioFinal = monto*cantidad
    print("Precio final sin descuento: ",precioFinal)