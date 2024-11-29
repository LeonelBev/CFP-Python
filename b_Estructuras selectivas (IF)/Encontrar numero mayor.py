print("Ingrese primer numero: ")
num1 = float(input())
print("Ingrese segundo numero: ")
num2 = float(input())
print("Ingrese tercer numero: ")
num3 = float(input())
if num1 > num2 and num1 > num3:
    print("Numero mayor: ",num1)
else:
    if num2 > num3:
        print("Numero mayor: ",num2)
    else:
        print("Numero mayor", num3)