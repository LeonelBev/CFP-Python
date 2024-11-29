dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))

def sacarMultiplo (dividendo, divisor):
    if(dividendo % divisor == 0):
        resultado = True
    else:
        resultado = False
    return(resultado)

resultado = sacarMultiplo(dividendo, divisor)

if(resultado == True):
    print("El divisor es multiplo.")
else:
    print("El divisor no es multiplo.")


