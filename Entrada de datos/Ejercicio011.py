"""
Escribir un programa que permita resolver el siguiente problema:

Tres personas aportan diferente capital a una sociedad y desean saber el valor total aportado y 
qué porcentaje aportó cada una (indicando nombre y porcentaje).

Solicitar la carga por teclado del nombre de cada socio y su capital aportado, 
a partir de esto calcular e informar lo requerido previamente.
"""

persona1 = {'nombre': input('ingrese nombre del socio => '), 'aporte': float(input('ingrese cantidad aportada =>'))}
persona2 = {'nombre': input('ingrese nombre del socio => '), 'aporte': float(input('ingrese cantidad aportada =>'))}
persona3 = {'nombre': input('ingrese nombre del socio => '), 'aporte': float(input('ingrese cantidad aportada =>'))}
aportes_totales = persona1['aporte'] + persona2['aporte'] + persona3['aporte']
print(f"nombre: {persona1['nombre']} aporto a la sociedad ${persona1['aporte']}, un {(persona1['aporte'] / aportes_totales)*100} del total de la sociedad \nnombre: {persona2['nombre']} aporto a la sociedad ${persona2['aporte']}, un {(persona2['aporte'] / aportes_totales)*100} del total de la sociedad \nnombre: {persona3['nombre']} aporto a la sociedad ${persona3['aporte']}, un {(persona3['aporte'] / aportes_totales)*100} del total de la sociedad ")

