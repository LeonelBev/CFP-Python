limite = int(input("Ingrese la cantidad de empleados: "))
SueldoMayor = 0
ordenEmpleado = int

for i in range (1,limite+1):
    orden = int(input("Ingrese el numero de orden: ")) 
    sueldo = int(input("Ingrese el sueldo del empleado: "))
    
    if(sueldo > SueldoMayor):
        SueldoMayor = sueldo
        ordenEmpleado = orden
        
print(f"El empleado #{ordenEmpleado} tiene el mayor sueldo: ${SueldoMayor}")
