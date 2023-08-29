"""
Escribir un programa que solicite al usuario ingresar tres notas de un alumno. 
programa debe mostrar por pantalla las notas separadas por comas en un rengl�n 
y el promedio de las notas en el siguiente renglon.

Ejemplo de ejecuci�n:
    Ingrese la nota 1: 7
    Ingrese la nota 2: 8
    Ingrese la nota 3: 9
    Notas: 7, 8, 9
    Promedio: 8.0
"""

nota1 = float(input('ingrese nota 1 =>'))
nota2 = float(input('ingrese nota 2 =>'))
nota3 = float(input('ingrese nota 3 =>'))
promedio = (nota1 + nota2+ nota3) / 3

print(f"Notas: {nota1}, {nota2}, {nota3} \nPromedio: {promedio}")