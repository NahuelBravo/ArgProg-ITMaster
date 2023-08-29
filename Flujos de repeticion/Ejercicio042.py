"""
Escribir un programa que lea n�meros enteros hasta que se ingrese un 0, 
y muestre el promedio de los n�meros ingresados.

"""

num = int(input("ingrese un numero entero => "))
numList = []
suma = 0
while num != 0:
    numList.append(num)
    num = int(input("ingrese un numero entero => "))
    suma += num
promedio = suma / len(numList)
print(f"promedio es: {promedio}")