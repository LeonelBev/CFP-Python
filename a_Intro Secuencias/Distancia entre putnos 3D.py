import math

x1 = int (input("X1: "))
y1 = int (input("Y1: "))
z1 = int (input("Z1: "))
x2 = int (input("X2: "))
y2 = int (input("Y2: "))
z2 = int (input("Z2: "))

distancia = math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
print("Distancia calculada: ",distancia)