import math
radial = float (input("Ingrese el angulo radial: "))
#Radial a Sexagesimal = 1rad * 180/pi
sexagesimales = radial*180/math.pi
#Sexagesimal a Centesimal = 1°*200/180
centesimales = sexagesimales*200/180
print("Angulo radial: ",radial)
print("Angulo sexagesimal: ",sexagesimales)
print("Angulo centesimales: ",centesimales)