"""
Escribir un programa que permita ingresar un n�mero entero n. 
Debe mostrar los primeros 10 m�ltiplos de n.

Ejemplo:

n = 5  

n x 1 = 5  
n x 2 = 10  
n x 3 = 15  
n x 4 = 20  
n x 5 = 25  
n x 6 = 30  
n x 7 = 35  
n x 8 = 40  
n x 9 = 45  
n x 10 = 50
"""

num1 = int(input("ingrese un numero entero => "))

for i in range(1,11):
    print (f"{num1} x {i} = {num1 * i}")