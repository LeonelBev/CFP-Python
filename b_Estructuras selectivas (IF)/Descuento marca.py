#-10% si >= 2000 -5% si == marca +10%
precio = float(input("Ingrese el precio de su compra: "))
marcaingreso = str(input("Ingrese la marca de su compra: "))
MARCA = "NOSY"
if(precio >= 2000):
    precioDescuento = precio*0.9
    if(marcaingreso.upper() == MARCA):
        precioDescuento = precioDescuento*0.95
else:
    if(marcaingreso.upper() == MARCA):
        precioDescuento = precio*0.95
    else:
        precioDescuento = precio
precioFinal = precioDescuento*1.2
print(f"Precio inicial: {precio}")
print(f"Marca del producto: {marcaingreso}")
print(f"Precio final: {precioFinal}")