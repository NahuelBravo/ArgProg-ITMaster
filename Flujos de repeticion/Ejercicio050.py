"""
Escribir un programa que permita validar la nota de un examen. 
Se espera que la nota que el usuario ingrese sea un n�mero comprendido entre 0 y 10.

La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.

Las notas 1 y 3 no usan nunca.
La nota 0 se reserva para los ausentes.
Las notas v�lidas pueden ser un 2 o un valor entre 4 y 10.

"""

def validar_nota():
    nota = int(input("Ingrese una nota entre 0 y 10 => "))
    validador = True
    while validador:
        if nota == 1 or nota == 3:
            print(f"nota: {nota}, nota invalida ")
            nota = int(input("Ingrese una nota entre 0 y 10 => "))
            validador = True
        elif nota == 2 or nota > 3 and nota <= 10:
            print(f"nota: {nota}, esta nota es valida")
            validador = False
        elif nota == 0:
            print(f"nota: {nota}, ausente")
            validador = False
        else:
            print(f"nota invalida, ingrese nuevamente")
            nota = int(input("Ingrese una nota entre 0 y 10 => "))
            validador = True
            
validar_nota()