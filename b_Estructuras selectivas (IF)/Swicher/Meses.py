def obtener_nombre_mes(numero_mes):
    meses = {
    1:"Enero",
    2:"Febrero",
    3:"Marzo",
    4:"Abril",
    5:"Mayo",
    6:"Junio",
    7:"Julio",
    8:"Agosto",
    9:"Septiembre",
    10:"Octubre",
    11:"Noviembre",
    12:"Diciembre"
    }
    return meses.get(numero_mes, "Mes no válido")

def main():
    try: 
        numero_mes = int(input("Ingrese un numero del mes (1-12): "))
        nombre_mes = obtener_nombre_mes(numero_mes)
        if nombre_mes != "Mes no válido":
            print(f"El número {numero_mes} corresponde al mes de {nombre_mes}.")
        else:
            print(nombre_mes)
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")

main()
