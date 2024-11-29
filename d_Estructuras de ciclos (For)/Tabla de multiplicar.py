num = int(input("Ingrese el numero: "))
limite = int(input("Ingrese hasta que numero de la tabla: "))
limite+=1
multi = 0

for i in range (0, limite):
    resultado = num*multi
    print(f"{num} X {multi} = {resultado}")
    multi+=1
    