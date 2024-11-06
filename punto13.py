# desarrollar un algoritmo que halle la nota total de una materia en el SENA, y determine si la gano o la reprobó
A = float(input("Ingrese la calificación del primer parcial: "))
B = float(input("Ingrese la calificación del segundo parcial: "))
C = float(input("Ingrese la calificación del tercer parcial: "))

if A >= 100 and B >= 100 and C >= 100:
    print("El alumno aprobo la materia")
elif A < 100 or B < 100 or C >= 100:
    print("El alumno reprobo la materia")
elif A < 100 or B >= 100 or C < 100:
    print("El alumno reprobo la materia")
else:
    print("El alumno reprobo la materia")
