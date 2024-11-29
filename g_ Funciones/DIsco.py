from random import *

disco = [0 for _ in range(270)]
mayores21 = 0
menores21 = 0

def generar_Num_Random():
    for i in range(len(disco)):
        disco[i] = randint(18,40)
        comprobar_Edad(disco[i])
    return(disco)

def comprobar_Edad(ingresante):
    global mayores21
    global menores21
    
    if(ingresante >= 21):
        mayores21 += 1
        return(mayores21)
    else:
        menores21 += 1
        return(menores21)
    
def main():
    generar_Num_Random()
    print(disco)
    print(f"Mayores a 21 ingresados: {mayores21}")
    print(f"Menores a 21 ingresados: {menores21}")

main()