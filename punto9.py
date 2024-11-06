# Dados tres números enteros únicos, a, b y c. Elabore un algoritmo que los ordene de mayor a menor e imprímalos.
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

# Ordenamiento de mayor a menor
if a > b and a > c:
    if b > c:
        print(c, b, a)
    else:
        print(b, c, a)
elif b > a and b > c:
    if a > c:
        print(c, a, b)
    else:
        print(a, c, b)
        
