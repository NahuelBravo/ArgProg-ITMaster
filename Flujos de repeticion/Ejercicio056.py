"""
Escribir un programa que permita Leer números que representan edades de un grupo de personas, 
finalizando la lectura cuando se ingrese el número 999. Imprimir cuántos son menores de 18 años, 
cuántos tienen 18 años o más y el promedio de edad de ambos grupos. 
Descartar valores que no representan una edad válida. (Se considera válido una edad entre 0 y 100)
"""

def ingresar_edades():
    edad = int(input("Ingresar una edad (para finalizar ingrese 999) => "))
    edades = []
    validador = True
    
    while validador:
        if edad == 999:
            validador = False
        elif edad < 0 or edad > 100:
            edad = int(input("Ingresar una edad (para finalizar ingrese 999) => "))
        else:
            edades.append(edad)
            edad = int(input("Ingresar una edad (para finalizar ingrese 999) => "))
    
    agrupar_edades(edades)
    
def agrupar_edades(edades):
    mayores = []
    menores = []
    i = 0
    while i < len(edades):
        if edades[i] >= 18:
            mayores.append(edades[i])
            i += 1
        else:
            menores.append(edades[i])
            i += 1
    
    print(f" las edades son {edades}\n hay {len(mayores)} personas mayores y {len(menores)} personas menores")
    

ingresar_edades()