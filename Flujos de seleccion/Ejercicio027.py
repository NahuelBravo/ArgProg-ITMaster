"""
Escribir un programa que permita ingresar una edad (entre 1 y 120 a�os), 
un g�nero ('F'para mujeres, 'M' para hombres) y un nombre. 
En caso de haber ingresado valores err�neos (edad fuera de rango o g�nero inv�lido), 
informar tal situaci�n indicando el nombre de la persona. 
Si los datos est�n bien ingresados el programa debe indicar, 
sabiendo que las mujeres se jubilan con 60 a�os o m�s y los hombres con 65 a�os o m�s, 
si la persona est� en edad de jubilarse.
"""

edad = int(input("Ingrese su edad => "))
genero = input("Ingrese su genero 'M' o 'F' => ") 
nombre = input("Ingrese su nombre => ")
verdadero = True

while verdadero:
    if edad < 1 or edad > 120:
        print(f"Edad de {nombre} invalida")
        edad = int(input("Ingrese su edad => "))
        verdadero = False
    elif genero != 'M' or genero != 'F':
        print(f"Genero de {nombre} invalido")
        genero = input("Ingrese su genero 'M' o 'F' => ")
        verdadero = False
    

if genero == 'F' and edad >= 60:
    print(f"{nombre} estas en edad jubilatoria")  
elif genero == 'M' and edad >= 65: 
    print(f"{nombre} estas en edad jubilatoria") 
else:
    print(f"{nombre} no estas en edad jubilatoria")    
                


        
        