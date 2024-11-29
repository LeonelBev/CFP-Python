matriz = [
            [10,20],
            [30,40]
]

for i in range (0,len(matriz)):
    for j in range (0,len(matriz)):
        ingreso = int(input(f"Ingrese el elemento para la fila {i}, columna {j}: "))
        matriz[i][j] = ingreso

print(matriz)