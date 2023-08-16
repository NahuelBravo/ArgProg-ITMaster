"""
Escribir un programa que permita ingresar tres números enteros e indicar cual es el mayor.
"""

num1 = float(input("Ingrese un numero => "))
num2 = float(input("Ingrese otro numero => "))
num3 = float(input("Ingrese un numero mas => "))



if num1 > num2 and num2:
    print(f"{num1} es mayor que {num2} y {num3}")
elif num2 > num1 and num3:
    print(f"{num2} es mayor que {num1} y {num3}")
else:
    print(f"{num3} es mayor que {num1} y {num2}")