CLAVE = "eureka"
ingreso = str(input("Ingrese la clave: "))
contador = 3
while (ingreso.casefold() != CLAVE) and contador!=1:
        print("Error. Clave incorrecta. ")
        contador-=1
        print(f"Intentos restantes: {contador}")
        ingreso = str(input("Ingrese la clave: "))
if (ingreso.casefold() == CLAVE):
    print("Ingresado correctamente.")
else:
    print("Intentos agostados.")
