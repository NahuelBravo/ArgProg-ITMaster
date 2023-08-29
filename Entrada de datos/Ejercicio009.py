"""
Escribir un programa que permita ingresar valores del mismo tipo para las variables num1 y num2. 
Una vez cargadas, mostrar ambas variables por pantalla, intercambi� sus 
valores (que lo cargado en num1 quede en num2, y viceversa) y volv� a mostrarlas actualizadas.
"""

num1 = input('Ingrese un valor => ')
num2 = input('Ingrese un valor => ')
print(f"El valor actual de los datos es: {num1}, {num2}")

if type(num1) == type(num2):
    num3 = num1
    num1 = num2
    num2 = num3
    print(f"Ahora el valor de los datos es: {num1}, {num2}") 
else:
    print("Error")

        