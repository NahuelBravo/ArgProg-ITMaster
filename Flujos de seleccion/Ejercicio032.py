"""
Una remiser�a requiere un sistema que calcule el precio de un viaje a partir de la cantidad de km que desea 
recorrer el usuario.

Tiene la siguiente tarifa:
Viaje m�nimo $50
Si recorre entre 0 y 10km: $20/km
Si recorre 10km o m�s: $15/km
Escribir un programa que permita ingresar la cantidad de km que desea recorrer el usuario y 
muestre el precio del viaje.

"""

cantidad_kilometros = int(input("Ingrese la cantidad de kilometros que quiere recorrer => "))

VIAJE_MINIMO = 50
viaje_total = VIAJE_MINIMO



if cantidad_kilometros >= 0 and cantidad_kilometros <= 10:
    viaje_total += (cantidad_kilometros * 20)
    print(f"Precio total del viaje es ${viaje_total}")
else:
    viaje_total += (cantidad_kilometros * 25)
    print(f"Precio total del viaje es ${viaje_total}")