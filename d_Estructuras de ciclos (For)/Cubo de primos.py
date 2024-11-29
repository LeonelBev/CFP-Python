for i in range (2, 72):
    primo = True
    j = 2
    while(i>j):
        if (i % j == 0):
            primo = False
            break
        else:
            j+=1
    if(primo == True):
        cubo = i**3
        print(f"El cubo de {i} es {cubo}")
