"""
Escribir un programa que permita ingresar un n�mero entero. Debe mostrarse el n�mero ingresado:
a. Multiplicado por 10. (utilizar el operador *) 
a. Dividido por 10. (utilizar el operador /) 
a. Elevado al cuadrado. (utilizar el operador **)

Cada resultado debe mostrarse en una l�nea distinta.
Ejemplo de ejecuci�n:
Ingrese un n�mero entero: 5
5 * 10 = 50
5 / 10 = 0.5
5 ** 2 = 25
"""

num1 = int(input('ingrese un numero => '))
multiplicacion = num1 * 10
division = num1 / 10
al_cuadrado = num1 ** 2

print(f" {num1} * 10 = {multiplicacion} \n {num1} / 10 = {division} \n {num1} ** 2 = {al_cuadrado} ")
