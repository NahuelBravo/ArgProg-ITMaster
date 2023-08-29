"""
Ejercicio 16:
Escribir un programa que permita al usuario ingresar un período de tiempo en segundos. 
Luego, el programa debe convertir ese período de tiempo a una forma más legible y comprensible para el usuario,
expresando el resultado en días, horas, minutos y segundos. 
El resultado se mostrará en pantalla en un mensaje que indique la cantidad de segundos ingresados 
y su equivalente en días, horas, minutos y segundos.

Ejemplo: 200000 segundos equivalen a 2 días, 7 horas, 33 minutos y 20 segundos. 
Usar en el programa las siguientes instrucciones:
dias = segundos // 86400 # 86400 segundos = 1 día

horas = (segundos % 86400) // 3600 # 3600 segundos = 1 hora

minutos = (segundos % 3600) // 60 # 60 segundos = 1 minuto

segundos_restantes = segundos % 60 # segundos restantes
"""

periodo_segundos = int(input("Ingrese el periodo en segundos => "))
dias = 0
horas = 0
minutos = 0
segundos = 0

if periodo_segundos != 0:
    dias = periodo_segundos // 86400
    horas = (periodo_segundos % 86400) // 3600
    minutos = (periodo_segundos % 3600) // 60
    segundos = (periodo_segundos % 60)
    print(f"dias: {dias}, horas: {horas}, minutos: {minutos}, segundos: {segundos}")
else:
    print("El periodo de tiempo es 0")


    

