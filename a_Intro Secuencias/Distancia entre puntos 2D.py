print("Ingresar cordenadas A")
EjeX = float(input())
EjeY = float(input())
print("Ingresar cordenadas B")
Eje2X = float(input())
Eje2Y = float(input())
distancia = ((EjeX-Eje2X)**2 + (EjeY - Eje2Y)**2)** 0.5
print("Distancia entre puntos: ", distancia)