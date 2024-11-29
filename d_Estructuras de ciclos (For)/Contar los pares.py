contador = 0

for i in range (1,101):
    ingreso = int(input(f"Ingrese el {i}° numero: "))
    if(ingreso % 2 == 0):
        contador+=1

print(f"Cantidad de numeros pares ingresados: {contador}")