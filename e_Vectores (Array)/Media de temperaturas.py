temperaturas = []
suma = 0
contador = 0
cantElementos = int(input("Ingrese la cantidad de elementos: "))

for i in range(1,cantElementos+1):
    elemento = int(input(f"Ingrese el {i}° elemento: "))
    temperaturas.append(elemento)
    suma += elemento

media = suma/len(temperaturas)
    
for i in range(0,cantElementos):
    if(temperaturas[i] >= media):
        contador += 1

print(f"Temperaturas: {temperaturas}")
print(f"Media: {media}. Cantidad de superiores: {contador}")