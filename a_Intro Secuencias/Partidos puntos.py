print("Ingesar partidos | ganados | perdidos | empatados |")
ganados = int(input())
perdidos = int(input())
empatados = int(input())

promedioGanados = ganados * 3
promedioPerdidos = perdidos * 0
promedioEmpates = empatados * 1
total = promedioGanados + promedioPerdidos + promedioEmpates
print("Puntos totales : ", total)