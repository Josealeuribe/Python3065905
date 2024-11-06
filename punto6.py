# Escriba el algoritmo que al capturar un numero entero convierta grados centígrados a kelvin, si captura un numero flotante diga si es mayor a 10.5, y si captura un carácter escriba su nombre.

valor = input("Ingrese un número o un caracter:")

try:
    celsius = int(valor)
    kelvin = round (celsius + 273.15,1)
    print("La temperatura en kelvin es : ", kelvin,"°K")
except ValueError:

 try:
    numeroF = float(valor)
    if numeroF >= 10.5:
        print("El número es mayor a 10.5")
    else:
        print("El número es menor a 10.5")
 except ValueError:
    print(f"El valor ingresado es un caracter: {valor}")
    


