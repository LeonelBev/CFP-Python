contador = 0

for i in range(1,51):
    ingreso = input(f"Ingrese el {i}° caracter: ")
    if(ingreso.casefold() == "a"):
        contador+=1

print(f"Cantidad de A ingresadas: {contador}")
    