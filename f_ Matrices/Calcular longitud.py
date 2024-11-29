columnas = int(input("Ingrese cantidad de columnas: "))

matriz = [[' ']*columnas,[' ']*columnas]

for i in range (1):
    for j in range (0, columnas):
        matriz[i][j] = input(f"Ingrese el nombre {i}{j}: ")
        matriz[1][j] = str(len(matriz[i][j]))

for fila in matriz:
    for valor in fila:
        print(valor, end=" ")
    print()
