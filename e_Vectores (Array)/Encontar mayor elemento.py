array = [3,1,4,1,5,9,2,6,5,3,5]
mayor = array[0]

for i in range(0,len(array)):
    if(array[i] > mayor):
        mayor = array[i]

print(array)
print(f"El numero mayor es: {mayor}")