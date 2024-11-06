# A ciertos estudiantes se les dice que su calificación final será el promedio de las dos calificaciones más altas de entre las tres que se han obtenido en el curso. Haga un algoritmo que permita a un estudiante efectuar el cálculo correspondiente a su nota final.

nota1 = float(input("Ingrese la primera calificación: "))
nota2 = float(input("Ingrese la segunda calificación: "))
nota3 = float(input("Ingrese la tercera calificación: "))

if nota1 >= 3.0 and nota2 >= 3.0 and nota3 < 3.0:
    nota_alta = (nota1 + nota2)/2
    print("La calificación final es: ", nota_alta)
elif nota1 >= 3.0 and nota2 < 3.0 and nota3 >= 3.0:
    nota_alta = (nota1 + nota3)/2
    print("La calificación final es: ", nota_alta)
else:
    nota_alta = (nota2 + nota3)/2
    print("La calificación final es: ", nota_alta)



