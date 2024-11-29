sueldo = float(input())
if sueldo >= 0 and sueldo <= 15000:
    aumento = sueldo*1.20
    print("Tu sueldo con aumento otorgado es de 20:",aumento)
else:
    if sueldo <= 20000:
        aumento = sueldo*1.10
        print("Tu sueldo con aumento otorgado es de 10:",aumento)
    else:
        if sueldo <= 25000:
            aumento = sueldo*1.05
            print("Tu sueldo con aumento otorgado es de 5:",aumento)
        else:
            print("No hay descuento. ",sueldo)

        