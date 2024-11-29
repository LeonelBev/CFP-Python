import math
print("Ingrese el primer lado del triangulo: ")
lado1 = float (input())
print("Ingrese el segundo lado del triangulo: ")
lado2 = float (input())
print("Ingrese el grado alfa: ")
gradoAlfa = float (input())
lado3 = (lado1**2+lado2**2-2*lado1*lado2*math.cos(gradoAlfa*math.pi/180))**0.50
print("El tercer lado del triangulo es: ",lado3)
