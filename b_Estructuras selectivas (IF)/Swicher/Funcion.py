variable = int (input("Ingrese su variable: "))
num = int (input("Ingrese la operación: | 1 | 2 | 3 |: "))
swicher={1 : 100*variable,
         2 : 100**variable,
         3 : 100/variable
}
resultado = swicher.get(num, "Error. Operación no existente.")
print(resultado)