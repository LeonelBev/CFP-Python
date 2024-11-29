dados = int(input("Dados a tirar: "))
porcentaje =(1/(6**dados))*100
probabilidad =6**dados

print(f"La probabilidad de sacar 6 en {dados} dados es de: {dados}/{probabilidad} | {porcentaje: .2f}%")