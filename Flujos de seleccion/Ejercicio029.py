"""
Escribir un programa que permita Ingresar las notas de los dos parciales de un alumno e indicar si promocion�,
aprob� o debe recuperar. Si el valor de la nota no esta entre 0 y 10, debe informar un error.

Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
Se debe recuperar cuando al menos una de las dos notas es menor a 4.
"""

primer_parcial = float(input("Ingrese nota del primer parcial => "))
segundo_parcial = float(input("Ingrese nota del segundo parcial => "))

verdadero = False

while verdadero != True:
    if  primer_parcial < 0.0 or primer_parcial > 10.0: 
        print(f"Nota del primer parcial invalida") 
        primer_parcial = float(input("Ingrese nota del primer parcial => "))
        verdadero = True 
    elif segundo_parcial < 0.0 or segundo_parcial > 10.0:
        print(f"Nota del segundo parcial invalida") 
        segundo_parcial = float(input("Ingrese nota del segundo parcial => ")) 
        verdadero = True
    #si pongo la primera y segunda nota incorrectamente el programa me pide la
    # primera nota solamente y sigue funcionando normal (hay que arreglarlo)
        
if primer_parcial >= 7.0 and segundo_parcial >= 7.0:
    print("a promocionado")
elif primer_parcial >= 4.0 and segundo_parcial >= 4.0:
    print("a aprobado")
else:
    print("debe recuperar")