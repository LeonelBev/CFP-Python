from os import system

def imprimir_Mapa(mapa):
    for i in mapa:
        for j in i:
            print(j, end=" ")
        print()      

def buscar_Barcos(mapa,ganador):
    enemigos = 0
    for i in range(len(mapa)):
        for j in range(len(mapa)):
            if mapa[i][j] > 0:
                enemigos += 1
    if(enemigos > 0):
        ganador = False
    else:
        ganador = True
    return(ganador)

def solicitar_Posicion(mapa):
    posicion = int(input("INGRESE LA POSICIÓN: "))
    while(posicion < 0) or (posicion>= len(mapa)):
        print("||| ERROR. POSICION FUERA DEL MAPA. INTENTE OTRA VEZ. |||")
        print()
        posicion = int(input("ELIJA LA POSICIÓN NUEVAMENTE: "))
    return(posicion)

def repartir_Unidad(unidades):
    print()
    print("||| INGRESE LAS UNIDADES A REPARTIR (1,2,3) |||")
    drop_Unidad = int(input(f"UNIDADES DISPONIBLES: |{unidades}|: "))
    while(drop_Unidad <= 0) or (drop_Unidad > 3):
        print()
        print("||| CANTIDAD INGRESADA NO SOPORTABLE. (SOLO 1,2 O 3 POR UNIDAD). |||")
        drop_Unidad = int(input(f"UNIDADES DISPONIBLES |{unidades}|: "))
    unidades -= drop_Unidad
    return(drop_Unidad,unidades)
    
def insertar_Unidad(drop_Unidad,mapa,Y,X,unidades):
    for i in range(0, len(mapa)):
        for j in range(0, len(mapa)):
            if(i == Y) and (j == X):
                if(mapa[i][j] != 0): #Se superponen barcos...
                    print("||| ¡LUGAR YA OCUPADO! INTENTE OTRA VEZ!. |||")
                    unidades+= drop_Unidad
                    return(mapa,unidades)
                else:
                    if(drop_Unidad == 3):
                        barco_3(mapa,i,j)
                    elif(drop_Unidad == 2):
                        barco_2(mapa,i,j)
                    else:
                        barco_1(mapa,i,j)
    return(mapa,unidades)

def barco_3(mapa,i,j):
    mapa[i][j] = 1
    if(j+1 >= len(mapa)):
        mapa[i][j-2] = 1
    else:
        mapa[i][j+1] = 1
    if(j-1 < 0):
        mapa[i][j+2] = 1
    else:
        mapa[i][j-1] = 1
    return(mapa)
                        
def barco_2(mapa,i,j):
    mapa[i][j] = 1
    if(j+1 >= len(mapa)):
        mapa[i][j-1] = 1
    else:
        mapa[i][j+1] = 1
    return(mapa)

def barco_1(mapa,i,j):
    mapa[i][j] = 1
    return(mapa)

def realizar_Ataque(mapa,y,x):
    for i in range(0,len(mapa)):
        for j in range(0,len(mapa)):
            if(i == y) and (j == x):
                if(mapa[i][j] != 0):
                    mapa[i][j] -=1
                    print()
                    print("¡GOLPEADO!")
                    return(mapa)
                else:
                    print()
                    print("FALLASTE.")
                    return(mapa)             

def turno_Posicionar(mapa,unidades):
    while(unidades > 0):
        print("")
        print("POSICIÓN X")
        posicionX = solicitar_Posicion(mapa)
        print()
        print("POSICIÓN Y")
        posicionY = solicitar_Posicion(mapa)
        drop_Unidad,unidades = repartir_Unidad(unidades)
        mapa,unidades = insertar_Unidad(drop_Unidad,mapa,posicionY,posicionX,unidades)
        print()
        print("| MAPA ACTUAL |")
        imprimir_Mapa(mapa)
    system("cls")
    
def turno_Ataque(mapa):
    print()
    print("POSICIÓN X")
    posicionX = solicitar_Posicion(mapa)
    print()
    print("POSICIÓN Y")
    posicionY = solicitar_Posicion(mapa)
    realizar_Ataque(mapa,posicionY,posicionX)
        
def main():
    mapaJ1 = [[0]*5,[0]*5,[0]*5,[0]*5,[0]*5]
    mapaJ2 = [[0]*5,[0]*5,[0]*5,[0]*5,[0]*5]
    
    ganador = False
    turnoJ1 = True
    turnoJ2 = False
    
    unidades = 6
    print("| TURNO DEL JUGADOR 1 |")
    turno_Posicionar(mapaJ1,unidades)
    system("cls")
    
    unidades = 6
    print("| TURNO DEL JUGADOR 2 |")
    turno_Posicionar(mapaJ2,unidades)
    system("cls")
    
    while(ganador == False):
        if(turnoJ1 == True):
            print("| ATAQUE DEL JUGADOR 1 |")
            turnoJ1 = False
            turnoJ2 = True
            turno_Ataque(mapaJ2)
            ganador = buscar_Barcos(mapaJ2,ganador)
        elif(turnoJ2 == True):
            print()
            print("| ATAQUE DEL JUGADOR 2 |")
            turno_Ataque(mapaJ1)
            turnoJ2 = False
            turnoJ1 = True
            ganador = buscar_Barcos(mapaJ1,ganador)
            
    if(turnoJ1 == True) and (ganador == True):
        print("|||| JUGADOR 2 GANA. ||||")
    elif(turnoJ2 == True) and (ganador == True):
        print("|||| JUGADOR 1 GANA. ||||")

main()