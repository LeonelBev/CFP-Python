
"""
enteros = []
indice = 0
longitud = 0
comparador = 0
cantElementos = int(input("Ingrese la cantidad de elementos: "))

for i in range(1,cantElementos+1):
    elemento = int(input(f"Ingrese el {i}° elemento: "))
    enteros.append(elemento)
    
print(enteros)
longitud = len(enteros)
  
while indice < longitud:
    if(comparador == enteros[indice]):
        enteros.pop(indice)
        indice-=1
        comparador = 0
        longitud-= 1
    else:
        comparador = enteros[indice]
        indice+=1

print(enteros)
"""