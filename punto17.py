#  desarrollar el algoritmo que lea tres números y diga si uno es divisible del otro.
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 % num2 == 0 or num1 % num3 == 0:
    print(f"{num1} es divisible por {num2} o {num3}")
else:
    print(f"{num1} no es divisible por {num2} ni {num3}")