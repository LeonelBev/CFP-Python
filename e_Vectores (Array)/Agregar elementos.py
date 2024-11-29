arrayElementos = []

cantElementos = int(input("Ingrese la cantidad de elementos: "))

for i in range(1,cantElementos+1):
    elemento = input("Ingrese el elemento: ")
    arrayElementos.append(elemento)
    
print(arrayElementos)