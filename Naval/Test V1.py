mapaJ1 = [0]*10
mapaJ2 = [0]*10

totalVidasJ1 = 20
turnosJ1 = 3

while(totalVidasJ1 > 0):
    if(turnosJ1 > 0):
        posicionJ1 = -1
        vidaBarcoJ1 = -1
        
        #Posicion J1
        while(posicionJ1 < 0) or (posicionJ1 > len(mapaJ1)):
            print(f"Mapa actual: {mapaJ1}")   
            posicionJ1 = int(input("Posicion del barquito del jugador 1: "))

        #Vida del barco        
        while(vidaBarcoJ1 <= 0) or (vidaBarcoJ1 > 20):
            print(f"Total de vidas para repartir: {totalVidasJ1}") 
            vidaBarcoJ1 = int(input("Vida del barquito: "))
            while(vidaBarcoJ1 > totalVidasJ1):
                print("No hay sificientes vidas.")
                print(f"Total de vidas para repartir: {totalVidasJ1}") 
                vidaBarcoJ1 = int(input("Vida del barquito: "))
            turnosJ1-=1
        for i in range(0, len(mapaJ1)):
            if(i == posicionJ1):
                if(mapaJ1[i] != 0):
                    print("Error. Lugar ya ocupado. Intente otra vez.")
                    turnosJ1+=1
                else:
                    mapaJ1[i] = vidaBarcoJ1
                    totalVidasJ1 -= vidaBarcoJ1
    else:
        break

totalVidasJ2 = 20
turnosJ2 = 3

while(totalVidasJ2 > 0):
    if(turnosJ2 > 0):
        posicionJ2 = -1
        vidaBarcoJ2 = -1
        
        #Posicion J1
        while(posicionJ2 < 0) or (posicionJ2 > len(mapaJ2)):
            print(f"Mapa actual: {mapaJ2}")   
            posicionJ2 = int(input("Posicion del barquito del jugador 2: "))

        #Vida del barco        
        while(vidaBarcoJ2 <= 0) or (vidaBarcoJ2 > 20):
            print(f"Total de vidas para repartir: {totalVidasJ2}") 
            vidaBarcoJ2 = int(input("Vida del barquito: "))
            while(vidaBarcoJ2 > totalVidasJ2):
                print("No hay sificientes vidas.")
                print(f"Total de vidas para repartir: {totalVidasJ2}") 
                vidaBarcoJ2 = int(input("Vida del barquito: "))
        turnosJ2-=1
        for i in range(0, len(mapaJ2)):
            if(i == posicionJ2):
                if(mapaJ2[i] != 0):
                    print("Error. Lugar ya ocupado. Intente otra vez.")
                    turnosJ2+=1
                else:
                    mapaJ2[i] = vidaBarcoJ2
                    totalVidasJ2 -= vidaBarcoJ2
    else:
        break

        
print(f"Mapa del jugador 1:{mapaJ1}")       
print(f"Mapa del jugador 2: {mapaJ2}")

winj1 = False
winj2 = False
restoAtt1 = 20
restoAtt2 = 20
ataquesJ1 = 99
ataquesJ2 = 99
turnoJ1 = True

while(winj1 == False) and (winj2 == False) and (restoAtt1 > 0) and (restoAtt2 > 0):
    attposicionJ1 = -1
    attposicionJ2 = -1
    
    if(turnoJ1 == True):
        #Ataque J1
        print("TURNO DEL JUGADOR 1")
        while(attposicionJ1 < 0) or (attposicionJ1 > 20):
            attposicionJ1 = int(input("Posicion de ataque del jugador 1: "))
            print(f"Ataques restantes: {restoAtt1}")
            attaquesJ1 = int(input(f"Cantidad de ataques a usar: "))
            if(attaquesJ1 > restoAtt1):
                while(attaquesJ1 > restoAtt1):
                    print(f"Ataques restantes: {restoAtt1}")
                    attaquesJ1 = int(input(f"Cantidad de ataques no disponibles. Intente otra vez: "))
                        
        turnosJ1 = False
        restoAtt1 -= attaquesJ1
        if(mapaJ2[attposicionJ1] != 0):
            mapaJ2[attposicionJ1] -= attaquesJ1
            print("Acierto!")
            if(mapaJ2[attposicionJ1] <= 0):
                print("Barquito hundido!")
                winj1 = True
            else:
                print("Sigue vivo!")
        else:
            print("Fallaste!")
    elif(turnosJ1 == False):
        #Ataque J2
        print("TURNO DEL JUGADOR 2")
        while(attposicionJ2 < 0) or (attposicionJ2 > 20):
            attposicionJ2 = int(input("Posicion de ataque del jugador 2: "))
            print(f"Ataques restantes: {restoAtt2}")
            ataquesJ2 = int(input("Cantidad de ataques a usar: "))
            if(ataquesJ2 > restoAtt2):
                while(restoAtt2 < ataquesJ2):
                    print(f"Ataques restantes: {restoAtt2}")
                    ataquesJ2 = int(input("Cantidad de ataques no disponibles. Intente otra vez: "))
    
        turnosJ1 = True
        restoAtt2 -= ataquesJ2
        if(mapaJ1[attposicionJ2] != 0):
            mapaJ1[attposicionJ2] -= ataquesJ2
            print("Acierto!")
            if(mapaJ1[attposicionJ2] <= 0):
                print("Barquito hundido!")
                winj2 = True
            else:
                print("Sigue vivo!")
        else:
            print("Fallaste!")
            
if(winj1 == True) or (restoAtt2 == 0):
    print("Jugador 1 gana")
elif(winj2 == True) or (restoAtt1 == 0):
    print("Jugador 2 gana")