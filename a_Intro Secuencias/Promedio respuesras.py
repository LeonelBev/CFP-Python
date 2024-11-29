print("Ingrese las respuestas correctas: ")
respuestasCorrectas = int(input())
print("Ingrese las respuestas incorrectas: ")
respuestasIncorrectas = int(input())
print("Ingrese las respuesas en blanco: ")
respuestasBlanco = int(input())
promedioCorrectas = respuestasCorrectas * 3
promedioIncorrectas = respuestasIncorrectas * (-1)
promedioBlancas = respuestasBlanco * 0
promedioFinal = promedioCorrectas + promedioIncorrectas + promedioBlancas
print("Promedio final: ", promedioFinal)