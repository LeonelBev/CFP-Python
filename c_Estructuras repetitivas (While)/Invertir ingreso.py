ingreso = int(input("Ingrese el numero a invertir: "))

auxiliar = 0
auxiliar2 = 0
i = 10

while (i <= ingreso):
    auxiliar= ingreso % 10
    ingreso = ingreso//10
    auxiliar2 = auxiliar2*10+auxiliar
    
auxiliar2=auxiliar2*10+ingreso
print(f"Numero invertido: {auxiliar2}")
