anio = int(input("Ingrese el año: "))
mes = int(input("Ingrese el mes: "))
dia = int(input("Ingrese el dia: "))
if (anio < 2000) or (anio > 2024):
    print("Error. Año incorrecto.")
else:
    if(mes < 1) or (mes > 12):
        print("Error. Mes incorrecto.")
    else:
        if (dia < 1) or (dia > 31):
            print("Error. Día incorrecto.")
        else:
            if(dia == 31) and (mes == 12):
                mes = mes+1
                dia = 1
                anio = anio+1
                mes= 1
                print(f"Proximo día:{dia} {mes} {anio}")
            else:
                if(dia == 31):
                    mes = mes+1
                    dia = 1
                    print(f"Proximo día:{dia} {mes} {anio}")
                else:
                    dia = dia+1
                    print(f"Proximo día:{dia} {mes} {anio}")
