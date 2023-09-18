"""
Escribir un programa que permita validar la nota de un examen. 
Se espera que la nota que el usuario ingrese sea un n�mero comprendido entre 0 y 10.

La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.

"""

nota = float(input("Ingrese una nota => "))

verdadero = True
while verdadero:
    if nota < 0 or nota > 10:
        print(f"Introducta una nota comprendida entre 0 y 10 por favor")
        nota = float(input("Ingrese una valida => "))
        verdadero = True
    else:
        verdadero = False
print(f"la nota ingresada es: {nota}")