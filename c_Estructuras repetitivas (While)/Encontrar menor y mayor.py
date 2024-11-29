ingreso = int(input("Ingrese un numero: "))
Menor = ingreso
Mayor = ingreso

while(ingreso != -1):
    if(ingreso > Mayor):
        Mayor = ingreso
    if(ingreso < Menor):
        Menor = ingreso
    ingreso = int(input("Ingrese un numero: "))
    
print(f"El menor numero ingresado es {Menor} y el mayor es {Mayor}")
