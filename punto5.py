#desarrollar un programa que capture tres números e imprima por pantalla cual es el número mayor, el menor, cuales son iguales, si los tres diferentes.

num1 = int(input("Ingrea el primer numero: "))
num2 = int(input("Ingrea el segundo numero: "))
num3 = int(input("Ingrea el tercer numero: "))

if num1 > num2 and num1 > num3:
    print(num1, "Es mayor que", num2, "y", num3)
elif num1 < num2 and num2 > num3:
    print(num2, "Es mayor que", num1, "y", num3)
else:
    print(num3, "Es mayor que", num1, "y", num2)

if num1 < num2 and num1 < num3:
    print(num1, "Es menor que", num2, "y", num3)
elif num1 > num2 and num2 < num3:
    print(num2, "Es menor que", num1, "y", num3)
else:
    print(num3, "Es menor que", num1, "y", num2)

if num1 == num2 and num2 == num3:
    print("Todos los numeros son iguales")
elif num1 == num2 or num1 == num3 or num2 == num3: 
    print("Hay dos numeros iguales")
else: 
    print("Todos los numeros son diferentes")







