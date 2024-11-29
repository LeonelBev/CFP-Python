switcher = {
    1: "[MEDALLA DE ORO]",
    2: "[MEDALLA DE PLATA]",
    3: "[MEDALLA DE BRONCE]"
}
print("Ingrese la posición: ")
ingreso = int (input())
# diccionario.get(argumento, mensaje por defecto)
posicion = switcher.get(ingreso, "[Certificado de participación]")
print(posicion)