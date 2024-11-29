from os import system

mapaJ1 = [[0]*5,[0]*5,[0]*5,[0]*5,[0]*5]
mapaJ2 = [[0]*5,[0]*5,[0]*5,[0]*5,[0]*5]
unidades = 20
turnos = 3
ataque = False
ganadorJ1 = False
ganadorJ2 = False

#Imprimir mapa
def imprimir_Mapa(mapa):
    for fila in mapa:
        for valor in fila:
            print(valor, end=" ")
        print()

#Recorrer mapa
def recorrer_Mapa(mapa):
    global ganadorJ1
    global ganadorJ2
    enemigos = 0
    for i in range(len(mapa)):
        for j in range(len(mapa)):
            if(mapa[i][j] > 0):
                enemigos += 1
    if(enemigos > 0):
        ganadorJ1 = False
        return(ganadorJ1)
    else:
        ganadorJ1 = True
        return(ganadorJ1)            

#Tomar posiciones      
def pedir_Posiciones(mapa):
    global turnos
    global unidades
    global ganadorJ1
    global ataque
    
    while(turnos > 0) and (unidades > 0) and (ganadorJ1 == False):
        posicionX = -1
        posicionY = -1
        
        if(ataque == False):
            print("MAPA ACTUAL: ")
            print("")
            imprimir_Mapa(mapa)
        
        print("")    
        print(f"TURNOS RESTANTES: {turnos}")    
        posicionX = int(input("ELIJA LA POSICION X: ")) 
        while(posicionX < 0) or (posicionX >= len(mapa)):
            print("UBICACIÓN FUERA DEL MAPA. INTENTE OTRA VEZ.")
            posicionX = int(input("ELIJA LA POSICION X: "))
        posicionY = int(input("ELIJA LA POSICION Y: "))
        print("")    
        while(posicionY < 0) or (posicionY >= len(mapa)):
            print("UBICACIÓN FUERA DEL MAPA. INTENTE OTRA VEZ.")
            print("")
            posicionY = int(input("ELIJA LA POSICION Y: "))
            print("")
                    
        dropUnidades = repartir_Unidades()       
        turnos -= 1  
        mapa = insertar_Unidades(posicionX,posicionY,dropUnidades,mapa)
    
#Repartir unidades
def repartir_Unidades():
    global unidades
    global ataque
    
    if(ataque == False):
        print("REPARTIR UNIDADES")
    else:
        print("USAR ATAQUES")
    dropUnidades = int(input(f"RESTANTES {unidades}: "))
            
    while(dropUnidades > unidades):
        print("CANTIDAD INGRESADA NO DISPONIBLES.")
        if(ataque == False):
            print("REPARTIR UNIDADES:")
        else:
            print("USAR ATAQUES:")
        dropUnidades = int(input(f"UNIDADES RESTANTES {unidades}:"))
        
    unidades -= dropUnidades
    return(dropUnidades)

#Insertar unidades
def insertar_Unidades(x,y,dropUnidades,mapa):
    global turnos
    global unidades
    global ataque
    
    for i in range(0, len(mapa)):
            for j in range(0,len(mapa)):
                if (i == y) and (j == x):
                    if (mapa[i][j] != 0):
                        if(ataque == False):
                            print("ERROR. LUGAR YA OCUPADO. INTENTE OTRA VEZ.")
                            print("")
                            turnos += 1
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
                        mapa[i][j] = dropUnidades
                        return(mapa)
                    else:
                        print("FALLASTE.")
                        print("")
                        return(mapa)
                    
#Ataque
def Atacar(mapa):
    global turnos
    global unidades
    global ataque
    
    ataque = True
    turnos = 3
    unidades = 30
    pedir_Posiciones(mapa)
    
    if(ganadorJ1 == True) and (ganadorJ2 == False):
        print("JUGADOR 1 GANA.")
    elif(ganadorJ2 == True) and (ganadorJ1 == False):
        print("JUGADOR 2 GANA.")
    elif(ganadorJ1 == False) and (ganadorJ2 == False):
        print("EMPATE.")

print("TURNO DEL JUGADOR 1:")
unidades = 20
turnos = 3
pedir_Posiciones(mapaJ1)
system("cls")


print("TURNO DEL JUGADOR 2:")
unidades = 20
turnos = 3
pedir_Posiciones(mapaJ2)
system("cls")

print("ATAQUE DEL JUGADOR 1:")
Atacar(mapaJ1)

print("ATAQUE DEL JUGADOR 2:")
Atacar(mapaJ2)

print("Fin.")