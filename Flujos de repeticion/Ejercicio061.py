"""
Escribir un programa que permita ingresar un número entero positivo y mostrar su factorial. 
El factorial de un número es el producto de todos los números enteros desde 1 hasta el número ingresado. 
Por ejemplo, el factorial de 5 es 1 * 2 * 3 * 4 * 5 = 120.
"""

def validar_entero():
    num = int(input("Ingrese un numero entero positivo => "))
    
    while True:
        if num < 0:
            print("numero ingresado invalido, intente nuevamente")
            num = int(input("Ingrese un numero entero positivo => "))
        else:
            return num
            False

def calcular_factorial():
    num = validar_entero()
    factorial = 0
    for i in range(num):
        if i == 0:
            factorial = 1
        else:
            factorial += (factorial * i)
    print(factorial)

calcular_factorial()          