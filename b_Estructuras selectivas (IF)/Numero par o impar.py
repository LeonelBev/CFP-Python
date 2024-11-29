num = float(input("Ingrese un numero: "))
if (num >= 0) and (num <= 10):
    if (num % 2 == 0):
        print("Numero par")
    else: 
        print("Numero impar")
else:
    print("El numero es menor a | 0 | o mayor a | 10 |")