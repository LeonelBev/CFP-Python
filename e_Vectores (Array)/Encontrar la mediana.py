array = [3,1,4,1,5,9,2,6,5,3,5]

for i in range(len(array)-2):
    for j in range(len(array)-1):
        if(array[j] > array[j+1]):
            aux = array[j]
            array[j] = array[j+1]
            array[j+1] = aux

if(len(array) % 2 == 0):
    mediana = (array[len(array)//2-1])+(array[len(array)//2])/2
else:
    mediana = array[len(array)//2]

print(array)
print(f"La mediana es: {mediana}")