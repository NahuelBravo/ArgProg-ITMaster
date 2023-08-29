"""
La farmacia Sindical efect�a descuentos a sus afiliados seg�n el importe de la compra con la siguiente 
escala:

Menor de $5500.0 el descuento es del 4.5%
Entre $5500.0 y $10000.0 el descuento es del 8%
M�s de $10000.0 el descuento es del 10.5%
Escribir un programa que reciba un importe e informe: el descuento y el precio neto a cobrar, 
con mensajes aclaratorios.

"""

importe = float(input("Ingrese su importe => "))

precio_neto = 0

if importe < 5500.0:
    precio_neto += (importe - (importe * 0.045))
    print(f"Su importe es ${importe}, recibe un descuento del 4.5%, el precio neto es ${precio_neto}")
elif importe >= 5500.0 and importe <= 10000.0:
    precio_neto += (importe - (importe * 0.08))
    print(f"Su importe es ${importe}, recibe un descuento del 8%, el precio neto es ${precio_neto}")
else:
    precio_neto += (importe - (importe * 0.105))
    print(f"Su importe es ${importe}, recibe un descuento del 10.5%, el precio neto es ${precio_neto}")
    