"""
Escribir un programa que permita leer dos n�meros naturales A y B. 
Calcular A elevado a la B mediante productos sucesivos y mostrar el resultado.

Ejemplo:

4^3 = 4 * 4 * 4 (4 multiplicado 3 veces).
3^4 = 3 * 3 * 3 * 3 (3 multiplicado 4 veces).
"""


num1 = int(input("ingrese un entero positivo => "))
num2 = int(input("ingrese otro entero positivo => "))


producto_por_sumas = ""
for i in range(num2):
    a =f"{num1}"
    s = f" x {num1}"
    if i == 0:
        producto_por_sumas = producto_por_sumas + a
    else:
        producto_por_sumas = producto_por_sumas + s
print(f"{num1} ^ {num2} = {producto_por_sumas} = {num1**num2}")