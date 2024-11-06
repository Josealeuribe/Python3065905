# . Escriba un algoritmo que acepte o rechace una pieza en forma de varilla, para una empresa de acuerdo a los siguientes criterios:
#a. Su longitud debe ser mayor de 7.5 cm pero no exceder los 9 cm
#b. Su diámetro no debe ser menor que 0.5 cm ni mayor de 1.3 cm.
#c. Por ningún motivo su masa debe exceder los 5.8 cm
#i. Nota: masa = diámetro * longitud / densidad; densidad = 3.5 Gr/cm

longitud = float(input("Ingrese la longitud de la varilla: "))
diametro = float(input("Ingrese el diámetro de la varilla: "))

masa = (diametro * longitud)/3.5
if longitud > 7.5 and longitud <= 9 and diametro >= 0.5 and diametro <= 1.3 and masa <= 5.8:
    print("La pieza es aceptada")
elif longitud > 7.5 and longitud <= 9 and diametro >= 0.5 and diametro <= 1.3 and masa > 5.8:
    print("La varilla es rechazada por superar la masa permitida")
elif longitud <= 7.5 or longitud > 9:
    print("La varilla es rechazada por tener una longitud incorrecta")
else:
    print("La varilla es rechazada por tener un diámetro incorrecto")
    

