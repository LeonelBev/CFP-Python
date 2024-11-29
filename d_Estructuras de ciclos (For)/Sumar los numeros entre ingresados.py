num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if(num1 > num2):
    mayor = num1
    menor = num2
    suma = mayor
else:
    mayor = num2
    menor = num1
    suma = mayor

for i in range (menor, mayor):
    suma +=i

print(suma)