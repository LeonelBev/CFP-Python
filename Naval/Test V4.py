from os import system

#Imprimir mapa
def imprimir_Mapa(mapa):
    for fila in mapa:
        for valor in fila:
            print(valor, end=" ")
        print()

#Recorrer mapa
def recorrer_Mapa(mapa):
    global ganador
    enemigos = 0
    for i in range(len(mapa)):
        for j in range(len(mapa)):
            if(mapa[i][j] > 0):
                enemigos += 1
                
    if(enemigos > 0):
        ganador = False
        return
    else:
        ganador = True
        return           

#Tomar posiciones      
def pedir_Posiciones(mapa):
    global unidades
    global ataque
    
    while(unidades > 0):
        posicionX = -1
        posicionY = -1
        
        if(ataque == False):
            print("MAPA ACTUAL: ")
            imprimir_Mapa(mapa)
        
        print("")        
        posicionX = int(input("ELIJA LA POSICION X: ")) 
        while(posicionX < 0) or (posicionX >= len(mapa)):
            print("UBICACIÓN FUERA DEL MAPA. INTENTE OTRA VEZ.")
            print("")
            posicionX = int(input("ELIJA LA POSICION X: "))
        print("")
        posicionY = int(input("ELIJA LA POSICION Y: "))  
        while(posicionY < 0) or (posicionY >= len(mapa)):
            print("UBICACIÓN FUERA DEL MAPA. INTENTE OTRA VEZ.")
            print("")
            posicionY = int(input("ELIJA LA POSICION Y: "))
                    
        dropUnidades = repartir_Unidades()
        system("cls")        
        mapa = insertar_Unidades(posicionX,posicionY,dropUnidades,mapa)
        break
    
#Repartir unidades
def repartir_Unidades():
    global unidades
    global ataque
    
    print("")
    if(ataque == False):
        print("REPARTIR UNIDADES DE 1, 2 o 3 DE ESPACIO.")
    else:
        print("USAR ATAQUES")
        
    dropUnidades = int(input(f"UNIDADES RESTANTES |{unidades}|: ")) 
    while(dropUnidades <= 0) or (dropUnidades > 3):
        print("CANTIDAD INGRESADA NO DISPONIBLES.")
        print("")
        if(ataque == False):
            print("")
            print("REPARTIR UNIDADES DE 1, 2 o 3 DE ESPACIO.")
        else:
            print("USAR ATAQUES:")
        dropUnidades = int(input(f"UNIDADES RESTANTES |{unidades}|:"))
    unidades -= dropUnidades
    print("")
    return(dropUnidades)

#Insertar unidades
def insertar_Unidades(x,y,dropUnidades,mapa):
    global ganador
    global unidades
    global ataque
    
    for i in range(0, len(mapa)):
            for j in range(0,len(mapa)):
                if (i == y) and (j == x):
                    if (mapa[i][j] != 0):
                        if(ataque == False):
                            print("ERROR. LUGAR YA OCUPADO. INTENTE OTRA VEZ.")
                            print("")
                            unidades += dropUnidades
                            return(mapa)
                        else:
                            print("GOLPEADO.")
                            mapa[i][j] -= dropUnidades
                            if(mapa[i][j] > 0):
                                print("SIGUE EN PIE.")
                                print("") 
                                return(mapa)
                            else:
                                print("ELIMINADO.")
                                print("")
                                recorrer_Mapa(mapa)
                                return(mapa)
                    elif(ataque == False):
                        #Barco 3
                        if(dropUnidades == 3):
                            for i in range(0,len(mapa)):
                                for j in range(0,len(mapa)):
                                    if(i == y) and (j == x):
                                        mapa[i][j] = 1
                                        if(j+1 >= len(mapa)):
                                            mapa[i][j-2] = 1
                                        else:
                                            mapa[i][j+1] = 1
                                        if(j-1 < 0):
                                            mapa[i][j+2]= 1
                                        else:
                                            mapa[i][j-1] = 1
                            return(mapa)

                        #Barco 2
                        elif(dropUnidades == 2):      
                            for i in range(0,len(mapa)):
                                for j in range(0,len(mapa)):
                                    if(i == y) and (j == x):
                                        mapa[i][j] = 1
                                        if(j+1 >= len(mapa)):
                                            mapa[i][j-1] = 1
                                        else:
                                            mapa[i][j+1] = 1
                            return(mapa)
                        else:
                        #Barco 1            
                            for i in range(0,len(mapa)):
                                for j in range (0,len(mapa)):
                                    if (i == y) and (j == x):
                                        mapa[i][j] = 1
                            return(mapa)
                    else:
                        print("FALLASTE.")
                        print("")
                        return(mapa)
                    
#Ataque
def Atacar(mapa):
    global unidades
    global ataque
    
    ataque = True
    unidades = 99
    pedir_Posiciones(mapa)
    
mapaJ1 = [[0]*5,[0]*5,[0]*5,[0]*5,[0]*5]
mapaJ2 = [[0]*5,[0]*5,[0]*5,[0]*5,[0]*5]
ataque = False
ganador = False
turnoJ1 = True
turnoJ2 = False
unidades = 6

while (unidades > 0):
    system("cls")
    print("TURNO DEL JUGADOR 1:")
    pedir_Posiciones(mapaJ1)
    system("cls")

unidades = 6
while (unidades > 0):
    print("TURNO DEL JUGADOR 2:")
    pedir_Posiciones(mapaJ2)
    system("cls")

while(ganador == False):
    if(turnoJ1 == True):
        print("ATAQUE DEL JUGADOR 1:")
        turnoJ1 = False
        turnoJ2 = True
        Atacar(mapaJ2)
    elif(turnoJ2 == True):
        print("ATAQUE DEL JUGADOR 2:")
        Atacar(mapaJ1)
        turnoJ2 = False
        turnoJ1 = True
        
if(turnoJ1 == True) and (ganador == True):
    print("JUGADOR 2 GANA.")
elif(turnoJ2 == True) and (ganador == True):
    print("JUGADOR 1 GANA.")

print("")
print("Mapa J1: ")
imprimir_Mapa(mapaJ1)
print("")
print("Mapa J2")
imprimir_Mapa(mapaJ2)

print("Fin.")