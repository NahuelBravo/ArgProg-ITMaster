"""
Escribir un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo b�sico y
su antig�edad en a�os. Si es soltero se le incrementa el sueldo en 5% del salario bruto por cada a�o de 
antig�edad, mientras que si es casado se le incrementa el sueldo en 7% del salario bruto por cada a�o de 
antig�edad. Tambi�n se le realizan los siguientes descuentos:

Jubilaci�n: 11%
Obra Social: 3%
Sindicato: 3%

Como datos de entrada se ingresa por teclado el sueldo b�sico, antig�edad y estado civil 
(S: Soltero / C: Casado). Se debe informar: (reemplazando los 9 por los valores que correspondan)
Estado Civil: Soltero/Casado Sueldo b�sico: $ 999.99 Antig�edad: 99 a�os

Descuentos:
Jubilaci�n - 999,99
Obra Social - 999,99
Sindicato - 999,99
Sueldo Neto 999,99
"""

sueldo_basico = float(input("Ingrese el sueldo basico => "))
antiguedad = int(input("Ingrese años de antigüedad => "))
estado_civil = input("Ingrese el estado civil Soltero (S)/Casado (C) => ")
jubliacion = (sueldo_basico* 0.11)
obra_social = (sueldo_basico * 0.003)
sindicato = (sueldo_basico * 0.003)
sueldo_neto = 0
verdadero = True

while verdadero != True:
    if estado_civil != 'c' and estado_civil!= 's':
        print(f"Estado civil '{estado_civil}' invalido")
        estado_civil = input("Ingrese el estado civil Soltero (S)/Casado (C) => ")
        verdadero = False
        

if estado_civil == 's':
    sueldo_neto += sueldo_basico + ((sueldo_basico * 0.005) * antiguedad) - antiguedad - obra_social -sindicato
    print(f"{sueldo_neto}")
else:
    sueldo_neto +=  sueldo_basico +  ((sueldo_basico * 0.007) * antiguedad)  - antiguedad - obra_social -sindicato
    print(f"{sueldo_neto}")