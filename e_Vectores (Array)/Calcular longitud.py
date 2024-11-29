longitud = int(input("Ingrese el tamaño de los arreglos: "))
nombres = longitud*[" "]
longNombres = longitud*[0]

for i in range (0,len(nombres)):
    nombres[i] = input(f"Ingrese el nombre {i}: ")
    longNombres[i] = len(nombres[i])
    
print(nombres)
print(longNombres)