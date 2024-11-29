import math
# 1 galon = 3.78541 litros
LITROSAGALON = 3.78541
PRECIOLITRO = 2
print("Cantidad de galones cargados: ")
consumo = int (input())
total = (consumo * LITROSAGALON) * PRECIOLITRO
print("Total a pagar (redondeado): $", math.ceil(total))