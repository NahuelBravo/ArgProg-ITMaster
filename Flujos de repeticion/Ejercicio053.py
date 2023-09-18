"""
Escribir un programa que permita ingresar nombre y edad de un grupo de personas (para cada una, nombre y edad). 
La carga termina cuando en el nombre de la persona se ingresa un asterisco ('*'). 
Mostrar al final cómo se llama la persona más joven.
"""

def ingresar_datos():
    nombre = input("Ingrese el nombre de la persona => ")
    edad = int(input("Ingrese la edad de la persona => "))
    validador = True
    personas = []
    while validador:
        if nombre == "*":
            validador = False
        else:
            persona = (nombre, edad)
            personas.append(persona)
            nombre = input("Ingrese el nombre de la persona => ")
            edad = int(input("Ingrese la edad de la persona => "))
    
    persona_mas_joven(personas)
    
def persona_mas_joven(personas):
    edades = []
    for i in range (len(personas)):  
        edades.append(personas[i][1])
    minimo = min(edades)
    
    for i in range(len(edades)):
        if edades[i] == minimo:
            print(f"la persona mas joven es {personas[i][0]} con {minimo} años")

ingresar_datos()