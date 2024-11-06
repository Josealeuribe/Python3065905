# Un algoritmo que lea un número, en caso de ser negativo lo multiplique por -1
numero = int(input("Ingrese un numero: "))

if numero < 0:
    numero *= -1
    print("El numero ingresado es negativo, pasandolo a positivo equivale a: ", numero)
else:
    print("El numero ingresado es positivo: ", numero)
