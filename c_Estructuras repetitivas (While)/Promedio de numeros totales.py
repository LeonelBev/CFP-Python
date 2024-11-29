ingreso = int
numTOTAL = 0
numSUMA = 0
promedio = 0

ingreso = int(input("Ingrese numeros: "))
numMAX = ingreso
numMIN = ingreso

while(ingreso != 0):
    if(ingreso > numMAX):
        numMAX = ingreso
    elif(numMIN > ingreso):
        numMIN = ingreso
    numTOTAL+= 1
    numSUMA += ingreso
    ingreso = int(input("Ingrese numeros: "))

promedio = numSUMA / numTOTAL

print(f"Numero máximo: {numMAX}")
print(f"Numero minimo: {numMIN}")
print(f"Promedio: {promedio}")
