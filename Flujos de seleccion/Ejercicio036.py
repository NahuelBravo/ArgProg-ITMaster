"""
Escribir un programa que permita ingresar dos n�meros enteros y la operaci�n a 
realizar('+', '-', '*', '/'). 
Debe mostrarse el resultado para la operaci�n ingresada. 
Considerar que no se puede dividir por cero (en ese caso mostrar el texto 'ERROR').
"""

num1 = int(input("ingrese un numero => "))
num2 = int(input("ingrese otro numero => "))
operacion = input("ingrese operacion a realizar (+, -, *, /)")

if operacion == '+':
    print(f"{num1} {operacion} {num2} = {num1 + num2}")
elif operacion == '-':
    print(f"{num1} {operacion} {num2} = {num1 - num2}")
elif operacion == '*':
    print(f"{num1} {operacion} {num2} = {num1 * num2}")
#revisar la division
elif num1 or num2 == 0 and operacion == '/':
    print("no se puede dividir por 0")
else:
    print(f"{num1} {operacion} {num2} = {int(num1 // num2)}")
    
    
    