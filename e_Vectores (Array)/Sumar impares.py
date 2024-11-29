array = [3,1,4,1,5,9,2,6,5,3,5]
suma = 0

for i in range(0,len(array)):
    if (array[i] % 2 != 0):
        suma+=array[i]
        
print(array)
print(suma)
