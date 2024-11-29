import math

print("Ingresar GB: ")
gigas = float(input())
megas = gigas * 1024
discos = megas / 1.44
print(discos)
print("Discos necesarios: ", round(discos))
print(math.ceil(discos))