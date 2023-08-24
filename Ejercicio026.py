"""
Escribir un programa que permita ingresar la cantidad de invitados a una fiesta 
y la cantidad de asientos disponibles en el salon. 
Debes indicar si alcanzan los asientos, Si los asientos no alcanzaran indicar cu�ntos 
faltan para que todos los invitados puedan sentarse.
"""

invitados = int(input("Ingrese la cantidad de invitados => "))
asientos = int(input("Ingrese la cantidad de asientos disponibles => "))

if asientos > invitados:
    print(f"sobran {asientos - invitados} asientos en total")
elif asientos < invitados:
    print(f"faltan {invitados - asientos} para que todos los invitados se sienten")
else:
    print(f"Todos los invitados tienen sus asientos")