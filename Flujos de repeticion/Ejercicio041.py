"""
Escribir un programa que lea n�meros enteros hasta que se ingrese un 0, y muestre el m�ximo.

"""

num = int(input("ingrese un numero entero => "))

numList = []
while num != 0:
    numList.append(num)
    num = int(input("ingrese un numero entero => "))

print(numList)