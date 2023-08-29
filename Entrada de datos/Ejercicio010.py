"""
Escribir un programa para resolver el siguiente problema:
Tres personas invierten dinero para fundar una empresa 
(no necesariamente en partes iguales). 
Calcular qu� porcentaje invirti� cada una.
"""

inversion1 = float(input('ingrese inversion 1 => '))
inversion2 = float(input('ingrese inversion 2=> '))
inversion3 = float(input('ingrese inversion 3 => '))

inversion_total = inversion1 + inversion2 + inversion3

porcentaje1 = f"{(inversion1 / inversion_total * 100):.2f}%"
porcentaje2 = f"{(inversion2 / inversion_total * 100):.2f}%"
porcentaje3 = f"{(inversion3 / inversion_total * 100):.2f}%"

print(f"La persona 1 invirtio en la empresa el {porcentaje1} \nLa persona 2 invirtio en la empresa el {porcentaje2} \nLa persona 3 invirtio en la empresa el {porcentaje3}")