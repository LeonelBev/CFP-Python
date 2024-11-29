matriz = []

filas = int(input("Ingrese cantidad de filas: "))
columnas = int(input("Ingrese cantidad de columnas: "))

for i in range(filas):
    fila = [0]*columnas
    matriz.append(fila)

for fila in matriz:
    for valor in fila:
        print(valor, end=" ")
    print()
