"""
Escribir un programa que permita leer dos n�meros A y B (enteros positivos). 
Calcular el producto A * B por sumas sucesivas e imprimir el resultado.

Ejemplo:
4*3 = 4 + 4 + 4 (4 sumado 3 veces).
3*4 = 3 + 3 + 3 + 3 (3 sumado 4 veces).

"""

num1 = int(input("ingrese un entero positivo => "))
num2 = int(input("ingrese otro entero positivo => "))

verdadero = True

while verdadero:
    if num1 < 0:
        print("numero ingresado invalido")
        num1 = int(input("ingrese un entero positivo => "))
        verdadero = True
    elif num1 < 0:
        print("numero ingresado invalido")
        num2 = int(input("ingrese otro entero positivo => "))
        verdadero = True
    else:
        verdadero = False

producto_por_sumas = ""
for i in range(num2):
    a =f"{num1}"
    s = f" + {num1}"
    if i == 0:
        producto_por_sumas = producto_por_sumas + a
    else:
        producto_por_sumas = producto_por_sumas + s
print(f"{num1} x {num2} = {producto_por_sumas} = {num1 * num2}")
        
    