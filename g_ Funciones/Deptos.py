from random import  *

filas = 10
columnas = 2

def programa ():
    dptos = [[0 for _ in range (columnas)]for _ in range (filas)]
    generador_Numero(dptos)
    impirmir_matriz(dptos)
    contador_habitantes(dptos)
     
def impirmir_matriz(matriz):
    for i in matriz:
        for j in i:
            print(j,end=' ')
        print()
            
def generador_Numero(matriz):
    for i in range (filas):
        for j in range (columnas):
            matriz[i][j] = randint(0,8)
    return(matriz)

def contador_habitantes(dpto):
    contador_Total = 0
    for i in range(filas):
        contador_Piso = 0
        for j in range(columnas):
            contador_Piso += dpto[i][j]
            contador_Total += dpto[i][j]
        print(f"Numero de habitantes en el piso {i+1}: {contador_Piso}") 
    print(f"Contador total de habitantes: {contador_Total}")
    
programa()