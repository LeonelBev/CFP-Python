array = [3,1,4,1,5,9,2,6,5,3,5]
mayor = array[0]
segundoMayor = array[0]

for i in range(1,len(array)):
    if(array[i] > mayor):
        mayor = array[i]
    if(array[i] < mayor) and (array[i] > segundoMayor):
        segundoMayor = array[i]

print(f"El numero mayor es: {mayor} y el segundo mayor es: {segundoMayor}")