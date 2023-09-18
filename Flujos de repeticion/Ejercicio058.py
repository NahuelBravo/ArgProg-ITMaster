"""
Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:

Aplica el precio base a la primera docena de unidades.
Aplica un 10% de descuento a todas las unidades entre 13 y 100.
Aplica un 25% de descuento a todas las unidades por encima de las 100.

Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. 
El cálculo resultante sería:

100 * 12 + 90 * 88 + 75 * 130 = 18870, y el precio promedio será 18870 / 230 = 82,04

Escribir un programa que lea la cantidad solicitada de un producto y su precio base, 
y muestre el valor total de la venta y el precio promedio por unidad.

El fin de carga se determina ingresando -1 como cantidad solicitada.

Al finalizar informar:

a- Cantidad de ventas realizadas total.
b- Cantidad de ventas que se aplicaron un 10% de descuento.
c- Cantidad de ventas que SOLO se aplicó el precio base, no se le realizaron descuentos

"""

def ingresar_cant_valor():
    cant_producto = int(input("Ingrese la cantidad del producto que desea comprar => "))
    valor_base = float(input("Ingrese ingrese el valor base del producto => "))
    validador = True
    
    while validador:
        if cant_producto <= 0:
            print(f"Cantidad ingresada invalida, intente nuevamente")
            cant_producto = int(input("Ingrese la cantidad del producto que desea comprar => "))
        elif valor_base <= 0:
            print("Valor base ingresado invalido, intente nuevamente")
            valor_base = float(input("Ingrese ingrese el valor base del producto => "))
        else:
            compra = [cant_producto, valor_base]
            valor_compra(cant_producto, valor_base)
            validador = False
    
    compra = None

def valor_compra(cant_producto, valor_base):
    primera_docena = 0 
    unidades_trece_cien = 0
    mas_cien = 0
    valor_base = valor_base
    
    for i in range (cant_producto):
        i += 1
        if i <= 12:
            primera_docena += 1
        elif i > 12 and i <= 100:
            unidades_trece_cien += 1
        elif i > 100:
            mas_cien += 1
    
    valor_total = (primera_docena * valor_base) + (unidades_trece_cien * (valor_base * 0.90)) + (mas_cien * (valor_base * 0.75))
    valor_promedio = valor_total / (primera_docena + unidades_trece_cien + mas_cien)
    
    print(f"el valor total de la compra es {valor_total}, el valor promedio por unidad es {valor_promedio}")
ingresar_cant_valor()