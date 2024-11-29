ingreso = int(input("Ingrese el valor limite: "))

contadorSuma = 0
contadorResta = 0
division = 0

for i in range (1,ingreso+1):
    if(contadorSuma == contadorResta):
        division += 1/i
        contadorSuma+=1
    else:
        division -=1/i
        contadorResta+=1

print(f"Resultado: {division}")
   