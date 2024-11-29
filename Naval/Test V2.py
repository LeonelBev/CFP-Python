mapaJ1 = [[0]*5,[0]*5,[0]*5,[0]*5,[0]*5]
unidades = 20
turnos = 3
ataque = False
ganadorJ1 = False

#Imprimir mapa
def imprimir_Mapa(mapa):
    for fila in mapa:
        for valor in fila:
            print(valor, end=" ")
        print()

#Recorrer mapa
def recorrer_Mapa(mapa):
    global ganadorJ1
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
            imprimir_Mapa(mapa)
            
        print(f"TURNOS RESTANTES: {turnos}")    
        posicionX = int(input("ELIJA LA POSICION X: ")) 
        while(posicionX < 0) or (posicionX > len(mapa)):
            print("UBICACIÓN FUERA DEL MAPA. INTENTE OTRA VEZ.")
            posicionX = int(input("ELIJA LA POSICION X: "))
                
        posicionY = int(input("ELIJA LA POSICION Y: "))    
        while(posicionY < 0) or (posicionY > len(mapa)):
            print("UBICACIÓN FUERA DEL MAPA. INTENTE OTRA VEZ.")
            posicionY = int(input("ELIJA LA POSICION Y: "))
                    
        dropUnidades = repartir_Unidades()       
        turnos -= 1  
        mapa = insertar_Unidades(posicionX,posicionY,dropUnidades)
    
#Repartir unidades
def repartir_Unidades():
    global unidades
    global ataque
    
    if(ataque == False):
        print("UNIDADES A REPARTIR:")
    else:
        print("ATAQUES A USAR:")
    dropUnidades = int(input(f"RESTANTES {unidades}: "))
            
    while(dropUnidades > unidades):
        print("CANTIDAD INGRESADA NO DISPONIBLES.")
        if(ataque == False):
            print("UNIDADES A REPARTIR:")
        else:
            print("ATAQUES A USAR:")
        dropUnidades = int(input(f"UNIDADES RESTANTES {unidades}:"))
        
    unidades -= dropUnidades
    return(dropUnidades)

#Insertar unidades
def insertar_Unidades(x,y,dropUnidades):
    global turnos
    global unidades
    global ataque
    
    for i in range(0, len(mapaJ1)):
            for j in range(0,len(mapaJ1)):
                if (i == y) and (j == x):
                    if (mapaJ1[i][j] != 0):
                        if(ataque == False):
                            print("ERROR. LUGAR YA OCUPADO. INTENTE OTRA VEZ.")
                            turnos += 1
                            unidades += dropUnidades
                            return(mapaJ1)
                        else:
                            print("GOLPEADO.")
                            mapaJ1[i][j] -= dropUnidades
                            if(mapaJ1[i][j] > 0):
                                print("SIGUE EN PIE.")
                                return(mapaJ1)
                            else:
                                print("ELIMINADO.")
                                recorrer_Mapa(mapaJ1)
                                return(mapaJ1)
                    elif(ataque == False):
                        mapaJ1[i][j] = dropUnidades
                        return(mapaJ1)
                    else:
                        print("FALLASTE.")
                        return(mapaJ1)
                    
#Ataque
def Atacar(mapa):
    global turnos
    global unidades
    global ataque
    
    ataque = True
    turnos = 3
    unidades = 30
    print("ATAQUE")
    pedir_Posiciones(mapa)
    
    if(ganadorJ1 == True):
        print("GANASTE.")
    else:
        print("PERDISTE.")
    
pedir_Posiciones(mapaJ1)
imprimir_Mapa(mapaJ1)
#Limpiar la consola
from os import system
system("cls")

Atacar(mapaJ1)

print("Fin.")