color_Aulas = ["Azul","Verde","Amarilla"]
espacio_Aulas = [40,35,30]

ingreso = int(input("Ingrese la cantidad de alumnos: "))
while(ingreso <= 0) or (ingreso > 40):
    ingreso = int(input("Error. Intente otra vez: "))
    
for i in range(len(espacio_Aulas)):
    if(espacio_Aulas[i] >= ingreso):
        if(i+1 >= len(espacio_Aulas)):
            espacio_Asignado = i
        elif(ingreso > espacio_Aulas[i+1]):
            espacio_Asignado = i
        

print(f"Aula asignada: {color_Aulas[espacio_Asignado]}. Espacio del aula restante: {espacio_Aulas[espacio_Asignado]-ingreso}")
print("Fin.")