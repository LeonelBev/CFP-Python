tamanio = int(input("Tamaño del arreglo: "))
array = [0]*tamanio
contador = 0

for i in range(len(array)):
    array[i] = int(input(f"Elemento a ingresar en la posicion {i+1}: "))

for i in range(len(array)):
    if(array[i] < 0):
        contador +=1

print(array)        
print(f"Cantidad total de numeros negativos: {contador}")