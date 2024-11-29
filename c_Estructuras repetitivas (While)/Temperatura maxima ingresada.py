temp = int
tempmax = 0
tempmin = 0
while(temp != 0):
    temp = int(input("Ingrese la temperatura: "))
    if(temp > tempmax):
        tempmax = temp
    elif(temp < tempmin):
        tempmin = temp
print(f"Temperatura máxima: °{tempmax}")
print(f"Temperatura minima: °{tempmin}")