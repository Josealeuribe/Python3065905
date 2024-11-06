# Desarrollar un algoritmo que evalué la siguiente expresión aritmética 1/n.
N = float(input("Ingrese un número entero positivo mayor a 0: "))
if N > 0:
    resultado = 1/N
    print("El resultado es: ",resultado)
else:
    print("El número ingresado no es válido")
    