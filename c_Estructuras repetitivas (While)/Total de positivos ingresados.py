ingreso = int
contadorpositivo= 0 
contadornegativo= 0 
porcentaje= 0 
total = 0

while(ingreso != 0):
    ingreso = int(input("Ingrese numeros: "))
    if(ingreso > 0):
        contadorpositivo+=1
    elif(ingreso < 0):
        contadornegativo+=1

total = contadornegativo + contadorpositivo
porcentaje = (contadorpositivo/total)*100

print(f"Total de numeros positivos ingresados: {contadorpositivo}")
print(f"Porcentaje de numeros positivos: {porcentaje}%")