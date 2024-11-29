def rellenar_Tabla (matriz):
    for i in range (0, len(matriz)):
        multiplicador = 1
        indice = i+1
        for j in range (0,len(matriz)):
            matriz[i][j] = indice*multiplicador
            multiplicador+=1
            
def impirmir_matriz(tabla):
    for i in tabla:
        indice = i[0]
        print(f"Tabla de {indice}: ", end= " ")
        for j in i:
            print(j, end=' ')
        print()

ingreso = int(input("Limite de tabla: "))
tabla = [[ 1 for _ in range(ingreso)]for _ in range (ingreso)]

rellenar_Tabla(tabla)
impirmir_matriz(tabla)