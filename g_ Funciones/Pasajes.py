filas = 20
columnas = 3

colectivo = [[0 for _ in range (columnas)]for _ in range(filas)]

def main():
    comprar_Pasaje()
    impirmir_matriz(colectivo)
    print("TODOS LOS ASIENTOS VENDIDOS.")

def impirmir_matriz(matriz):
    for i in matriz:
        for j in i:
            print(j,end=' ')
        print()
        
def recorrer_colectivo():
    for i in range(filas):
        for j in range(columnas):
            if(colectivo[i][j] == 0):
                comprar_Pasaje()
                        
def comprar_Pasaje():
    posicion_X = -1
    posicion_Y = -1
    impirmir_matriz(colectivo)
    while(posicion_Y < 0 or posicion_Y > 19) or (posicion_X < 0 or posicion_X > 2):
        posicion_Y = int(input("INGRESE EJE Y (0 - 19): "))
        posicion_X = int(input("INGRESE EJE X (0 - 2): "))
    asignar_Asiento(posicion_Y,posicion_X)
    
def asignar_Asiento(posicion_Y,posicion_X):
    for i in range (filas):
        for j in range (columnas):
            if(i == posicion_Y) and (j == posicion_X):
                if(colectivo[i][j] == 0):
                    colectivo[i][j] = 1
                    recorrer_colectivo()
                else:
                    print("ASIENTO OCUPADO.")
                    comprar_Pasaje()
                    
main()