array = [3,1,4,1,5,9,2,6,5,3,5]
suma = 0

for i in range(0,len(array)):
    suma+=array[i]
    
promedio = suma/len(array)

print(f"La suma total de los elementos de: {array} es: {suma} y el promedio es: {promedio}")