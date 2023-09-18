"""
Escribir un programa que permita al usuario ingresar dos n�meros enteros. La computadora debe indicar 
si el mayor es divisible por el menor.
(Un n�mero entero a es divisible por un n�mero entero b cuando el resto de la divisi�n entre a y b es 0)
"""

num1 = int(input("Ingrese un numero entero => "))
num2 = int(input("Ingrese un otro numero entero => "))

mayor = max(num1,num2)
menor = min(num1,num2)


if mayor%menor == 0:
    print(f"El numero mayor '{mayor}' es divisible por el menor '{menor}'")
else:
    print(f"El numero mayor '{mayor}' no es divisible por el menor '{menor}'")
