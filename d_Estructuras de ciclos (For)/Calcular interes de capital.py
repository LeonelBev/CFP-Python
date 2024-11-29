capital = 0
anio = 0
interes = 0

while (capital < 0) or (interes <= 0) or (interes >= 100) or (anio <= 0):
    interes = int(input("Ingrese el interes: "))
    capital = int(input("Ingrese el capital: "))
    anio = int(input("Ingrese el año: "))

for i in range (1, anio):
    capital = capital*(1+interes/100)

print(f"Tienes ${capital: .2f} ARGs")
