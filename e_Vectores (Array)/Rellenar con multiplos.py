tamanio = int(input("Ingrese el tamaño del arreglo: "))
multiplicador = 1
multiplo = int(input("Ingrese el numero a multiplicar: "))
array = tamanio*[multiplo]

for i in range(0,len(array)):
    array[i] = multiplicador*multiplo
    multiplicador+=1

print(array)