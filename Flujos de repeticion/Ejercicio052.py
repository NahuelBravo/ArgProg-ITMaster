"""
Escribir un programa que permita un programa que permita ingresar la estatura (en metros con decimales) 
de cada jugador de un equipo de básquet La carga finalizará al ingresar cero. 
Calcular y mostrar la estatura promedio del equipo.
"""

def ingresar_altura():
    altura = float(input("ingrese altura del jugador (introduzca 0 para finalizar => "))
    alturas_equipo = []
    validador = True
    while validador:
        if altura == 0:
            validador = False
        else:
            alturas_equipo.append(altura)
            altura = float(input("ingrese altura del jugador (introduzca 0 para finalizar => "))
    promedio_altura(alturas_equipo)
    
def promedio_altura(alturas_equipo):
    suma_alturas = 0
    for i in range(len(alturas_equipo)):
        suma_alturas += alturas_equipo[i]
        
    promedio_alturas = (suma_alturas / (len(alturas_equipo)))
    print(f"el promedio de alturas del equipo es {promedio_alturas}")
    
    
ingresar_altura()