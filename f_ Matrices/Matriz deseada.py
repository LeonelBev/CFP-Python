filas = int(input("Ingrese las filas: "))
columnas = int(input("Ingrese las columnas: "))

matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

for i in range (0,len(matriz)):
    for j in range (0,len(matriz)):
        matriz[i][j] = int(input("Ingrese un numero: "))

for filas in matriz:
    for columnas in filas:
        print(columnas, end=' ')
    print()