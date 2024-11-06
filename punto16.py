# desarrollar un algoritmo que capture un número y diga si es par o impar.
numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")