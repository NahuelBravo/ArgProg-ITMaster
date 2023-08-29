"""
Escribir un programa que permita ingresar el valor monetario de una hora de trabajo 
y la cantidad de horas trabajadas por d�a, para calcular el salario semanal de un 
trabajador que trabaja todos los d�as h�biles y la mitad de las horas del 
d�a h�bil los s�bados, suponiendo que todas las horas tienen el mismo valor."
"""

valor_hora = float(input('Ingrese el valor de la hora => '))
horas_dias_habiles = int(input('Horas trabajadas los dias habiles => '))
dias_habiles_trabajados = int(input('Ingrese la cantidad de dias habiles trabajados =>'))
dias_habiles = dias_habiles_trabajados * horas_dias_habiles
dia_sabado = horas_dias_habiles / 2
salario_semanal = (dias_habiles + dia_sabado) * valor_hora

print(f'El salario semanal del trabajador es de: {salario_semanal:.2f}')