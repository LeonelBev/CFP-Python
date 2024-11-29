seguir = 0

def calcularArea (bas,altu):
    resultado = bas * altu / 2
    return(resultado)
    
while(seguir != -1):
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))
    
    resultado = calcularArea(base,altura)
    print(f"Area del triangulo: {resultado}")
    
    seguir = int(input("Seguir?: "))
    
print("Fin.")
    
    
    