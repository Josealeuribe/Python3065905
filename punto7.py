#Desarrolle un algoritmo que lea de un registro: el nombre, la edad, el sexo, el estado civil de cualquier persona e imprima el nombre de la persona, si corresponde a un hombre casado mayor de 40 años o a una mujer soltera menor de 50 años.

nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
sexo = input("Ingrese el sexo: ")
estado_civil = input("Ingrese el estado civil: ")

if sexo == "masculino" and estado_civil == "casado" and edad > 40: 
    print(nombre, "es un hombre casado mayor de 40 años")
elif sexo == "femenino" and estado_civil == "soltera" and edad < 50:
    print(nombre, "es una mujer soltera menor de 50 años")
else:
    print(nombre, "no cumple con las condiciones para ser considerado")



