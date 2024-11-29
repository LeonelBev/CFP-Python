#d = b**2-4*a*c
num1 = int(input("Ingrese el primer numero:"))
num2 = int(input("Ingrese el segudno numero:"))
num3 = int(input("Ingrese el tercer numero:"))
num4 = num2**2-4*num1*num3
#((-b)+d**0.5)/2*a
#((-b)-d**0.5)/2*a
if (num4 > 0):
    raiz1 = ((-num2)+num4**0.5)/2*num1
    raiz2 = ((-num2)-num4**0.5)/2*num1
    print(f"Raices reales: {raiz1} {raiz2}")