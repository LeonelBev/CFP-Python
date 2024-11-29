primo = True
j = 2

ingreso = int(input("Ingrese el numero: "))

while(ingreso > j):
    if (ingreso % j == 0):
        primo = False
        break
    else:
        j+=1
if(primo == True):
    print(f"{ingreso} es primo. ")
else:
    print(f"{ingreso} no es primo. ")
