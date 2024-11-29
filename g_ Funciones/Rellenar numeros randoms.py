from random import  *

def generador_Numero(matriz):
    for i in range (0,len(matriz)):
        for j in range (0,len(matriz)):
            matriz[i][j] = randint(0,8)
    return(matriz)
    
matriz = [[0 for _ in range (3)]for _ in range (3)]
matriz = generador_Numero(matriz)

for i in matriz:
    for j in i:
        print(j, end=' ')
    print()