"""
Escribir un programa que permita ingresar dos números enteros e indicar si el primero es mayor, 
menor o igual al segundo.
"""

num1 = float(input("Ingrese un numero => "))
num2 = float(input("Ingrese otro numero => "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 < num2:
    print(f"{num1} es menor {num2}")
else:
    print(f"{num1} es igual a {num2}")