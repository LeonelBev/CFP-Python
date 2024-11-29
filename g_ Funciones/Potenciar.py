def Potenciar(base, potencia):
    resultado = base**potencia
    return(resultado)

seguir = 0

while(seguir != -1):
    base = int(input("Ingrese la base: "))
    potencia = int(input("Ingrese la potencia: "))
    resultado = Potenciar(base,potencia)
    
    print(f"Resultado potenciado: {resultado}")
    seguir= int(input("Desea seguir: "))
    
print("Fin del programa.")
