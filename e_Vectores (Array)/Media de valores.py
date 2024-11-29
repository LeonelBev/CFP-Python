array = 10*[0]
suma = 0

for i in range(0,len(array)):
    array[i] = int(input(f"Ingrese el numero de la posicion {i}: "))
    suma += array[i]

media = suma/len(array)

print(array)
print(f"La media de todos los valores es: {media}")