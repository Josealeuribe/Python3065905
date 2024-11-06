# Prepare un algoritmo que identifique e imprima el número medio de un conjunto de tres números únicos. El número medio es aquel que no es el menor ni el mayor.
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Identificar el número medio
if num1 > num2 and num1 < num3:
    medio = num1
    print("El número medio es: ", medio)
elif num2 > num1 and num2 < num3:
    medio = num2
    print("El número medio es: ", medio)
elif num3 > num1 and num3 < num2:
    medio = num3
    print("El número medio es: ", medio)
else:
    print("Los números ingresados no son unicos")
    



