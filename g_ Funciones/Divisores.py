def cantidad_Divisores(ingreso):
    contador = 0
    for i in range (1,ingreso+1):
        if(ingreso % i == 0):
            contador += 1
    return(contador)

ingreso = int(input("Ingrese un numero: "))
contador = cantidad_Divisores(ingreso)

print(f"Cantidad de divisores de {ingreso}: {contador}")
        