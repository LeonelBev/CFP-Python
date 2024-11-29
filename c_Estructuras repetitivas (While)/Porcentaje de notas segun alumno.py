nombre = str(input("Ingrese el nombre del alumno: "))

while(nombre != ""):
    nota1 = 0
    nota2 = 0
    nota3 = 0
    suma = 0
    nota1 = int(input("Ingrese la primer nota del alumno: "))
    if (nota1 >= 0) and (nota1 <= 10):
        nota2 = int(input("Ingrese la segunda nota del alumno: "))
        if (nota2 >= 0) and (nota2 <= 10):
            nota3 = int(input("Ingrese la tercera nota del alumno: "))
            if (nota3 >= 0) and (nota3 <= 10):
                suma = nota1 + nota2 + nota3
                practica = suma*0.1
                problema = suma*0.5
                teoria = suma*0.4
                notaFinal = practica + problema + teoria
                print(f"Nombre del alumno: {nombre}")
                print(f"Nota practica: {practica}")
                print(f"Nota de problemas: {problema}")
                print(f"Nota teorica: {teoria}")
                print(f"Nota final: {notaFinal}")
            else:
                print("Error en la primer nota ingresada.")
        else:
            print("Error en la segunda nota ingresada.")
    else:
        print("Error en la tercera nota ingresada.")
    nombre = str(input("Ingrese el nombre del siguiente alumno: "))
print("Fin del programa.")
