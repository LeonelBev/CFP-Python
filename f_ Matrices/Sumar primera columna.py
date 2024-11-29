columnas = int(input("Ingrese las columnas: "))
filas = int(input("Ingrese las filas: "))

matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
suma = 0


for i in range (0,filas):
    for j in range (0,columnas):
        matriz[i][j] = int(input("Ingrese un numero: "))
    suma += matriz[i][0]

for filas in matriz:
    for columnas in filas:
        print(columnas, end=' ')
    print()
print(suma)