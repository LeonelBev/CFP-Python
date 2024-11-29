contador = 0
ingreso = int(input("Ingrese numeros: "))

while(ingreso != -1 ):
    if(ingreso == 0):
        contador += 1
    ingreso = int(input("Ingrese numeros: "))

print(f"Cantidad de 0 ingresados: {contador}")
