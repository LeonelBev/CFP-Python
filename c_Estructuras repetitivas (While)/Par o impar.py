ingreso = int(input("Ingrese un numero mayor a 0:"))
while(ingreso <= 0):
    print(f"Error. El numero {ingreso} es menor a 0.")
    ingreso = int(input("Por favor ingrese un numero mayor a 0 nuevamente:"))
if(ingreso % 2 == 0):
    print(f"El numero {ingreso} es par")
else:
    print(f"El numero {ingreso} es impar")
