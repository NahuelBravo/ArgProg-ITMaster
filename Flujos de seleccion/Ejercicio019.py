"""
Escribir un programa que permita ingresar dos números enteros e indicar si son iguales o distintos

"""
num1 = int(input("ingrese un numero entero => "))
num2 = int(input("ingrese otro numero entero => "))

if num1 != num2:
    print(f"{num1} es distinto de {num2}")
else:
    print(f"{num1} es igual a {num2}")