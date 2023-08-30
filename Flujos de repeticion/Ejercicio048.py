"""
Escribir un programa que permita realizar varias operaciones matem�ticas ingresando un caracter 
por cada una la operaci�n a realizar (�+�, �-�, �*�, �/�, �F�) y 
dos n�meros enteros en el caso que no haya elegido �F�.
La computadora debe mostrar el resultado para la operaci�n ingresada. 
Considerar que no se puede dividir por cero. Cuando la operaci�n ingresada sea �F� nos indicar� que 
no se desean calcular m�s operaciones.
"""
num1 = int(input("Ingese un numero entero: "))
num2 = int(input("Ingese otro numero entero: "))
signo = input("Ingrese un operacion a realizar (+, -, *, /, F)")

operacion = 0

verdadero = True
while verdadero:
    if signo == "F":
        verdadero = False
    elif signo == "+":
        operacion = num1 + num2
        print(f"{num1} {signo}")