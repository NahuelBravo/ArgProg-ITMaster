"""
Escribir un programa que permita realizar varias operaciones matem�ticas ingresando un caracter 
por cada una la operaci�n a realizar (�+�, �-�, �*�, �/�, �F�) y 
dos n�meros enteros en el caso que no haya elegido �F�.
La computadora debe mostrar el resultado para la operaci�n ingresada. 
Considerar que no se puede dividir por cero. Cuando la operaci�n ingresada sea �F� nos indicar� que 
no se desean calcular m�s operaciones.
"""
def realiza_operacion():
    signo = input("Ingrese un operacion a realizar (+, -, *, /, F) =>")
    num1 = int(input("Ingese un numero entero: "))
    num2 = int(input("Ingese otro numero entero: "))
    operacion = 0
    validador = True
    while validador:
        if signo == "F":
            validador = False
        elif signo == "+":
            operacion = num1 + num2
            print(f"{num1} {signo} {num2} = {operacion}")
            signo = input("Ingrese un operacion a realizar (+, -, *, /, F) =>")
            num1 = int(input("Ingese un numero entero: "))
            num2 = int(input("Ingese otro numero entero: "))
            validador = True
        elif signo == "-":
            operacion = num1 - num2
            print(f"{num1} {signo} {num2} = {operacion}")
            signo = input("Ingrese un operacion a realizar (+, -, *, /, F) =>")
            num1 = int(input("Ingese un numero entero: "))
            num2 = int(input("Ingese otro numero entero: "))
            validador = True
        elif signo == "*":
            operacion = num1 * num2
            print(f"{num1} {signo} {num2} = {operacion}")
            signo = input("Ingrese un operacion a realizar (+, -, *, /, F) => ")
            num1 = int(input("Ingese un numero entero: "))
            num2 = int(input("Ingese otro numero entero: "))
            validador = True
        elif signo == "/" and num1 or num2 == 0:
            print(f"ERROR: no se puede dividir por cero, realice la operacion nuevamente")
            validador = False
            realiza_operacion()
        else:
            operacion = num1 / num2
            print(f"{num1} {signo} {num2} = {operacion}")
            signo = input("Ingrese un operacion a realizar (+, -, *, /, F) =>")
            num1 = int(input("Ingese un numero entero: "))
            num2 = int(input("Ingese otro numero entero: "))
            validador = True

            
realiza_operacion()