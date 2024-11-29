import math

print("Ingrese radio: ")
radio = float (input())
#volumen = 4/3*π*r³
volumen = 4/3*math.pi*radio**3
print("El radio ingresado de la esfera es: ", radio)
print("El volumen de la esfera es: ", volumen)