#desarrollar el algoritmo dado como dato el sueldo de un trabajador, le aplica un aumento del 15% si su sueldo es inferior a $300.000
Sueldo = float(input("Ingresa el sueldo del trabajador: "))

if Sueldo > 300.000:
    aumento = Sueldo * 0.15
    nuevo_sueldo = Sueldo + aumento
    print("El sueldo del trabajador con el aumento aplicado es: ", nuevo_sueldo)
else:
    print("El sueldo del trabajador no tiene auemnto")

