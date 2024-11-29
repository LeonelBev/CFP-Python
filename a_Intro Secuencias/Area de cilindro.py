import math

print("Ingrese altura: ")
altura = float (input())
print("Ingrese radio: ")
radio = float (input())
#volumen = π*r²*h
volumen = math.pi*radio**2*altura
#area = 2π*r*h+(r+h)
area = 2*math.pi*radio*(radio+altura)
print("La altura ingresada del cilindro es: ", altura)
print("El radio ingresado del cilindro es: ", radio)
print("El área del cilindro es: ", area)
print("El volumen del cilindro es: ", volumen)
