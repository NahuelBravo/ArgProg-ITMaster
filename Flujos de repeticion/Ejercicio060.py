"""
Escribir un programa para calcular el sueldo final a pagar a cada empleado de una empresa. 
De cada uno se tiene, sueldo básico, antigüedad, cantidad de hijos y estudios superiores (‘S’ o ‘N’). 
Además, se conocen los porcentajes de aumento del sueldo que dependen de los siguientes factores:

Si el empleado tiene más de 10 años de antigüedad: aumento del 10%
Si el empleado tiene más de 2 hijos: aumento del 10%, si solo tiene uno 5%
Si el empleado posee estudios superiores: aumento del 5%
Luego de ingresar los datos de un empleado se debe preguntar si se desea ingresar otro empleado o no. 
Se termina la carga cuando no se deseen ingresar más empleados.

Determinar: 
a. Por cada empleado: número de empleado, el sueldo básico y el nuevo sueldo. 
b. Sueldo nuevo promedio de la empresa.
"""

def datos_empleado():
    #sueldo básico, antigüedad, cantidad de hijos y estudios superiores
    sueldo_basico = int(input("Ingrese sueldo base => "))
    antiguedad = int(input("Ingrese años de antiguedad => "))
    cant_hijos = int(input("Ingrese cantidad de hijos => "))
    estudios_superiores = input("Tiene estudios superiores? [S/N] => ")
    empleado = None
    validador = True
    while validador:
        if sueldo_basico == 0:
            print("sueldo invalido ingrese una cantidad superior a cero")
            sueldo_basico = int(input("Ingrese sueldo base => "))
        elif estudios_superiores == "S" or estudios_superiores == "N":
            empleado = [sueldo_basico, antiguedad, cant_hijos, estudios_superiores]
            validador = False
        else:
            print("dato ingresado invalido, intente nuevamente")
            estudios_superiores = input("Tiene estudios superiores? [S/N] => ")
    return empleado

def empleados_empresa():
    agregar_empleado = input("agregar un empleado? [S/N] => ")
    empleados = []
    validador = True
    
    while validador:
        if agregar_empleado == "S":
           empleados.append(datos_empleado())
           agregar_empleado = input(" desea agregar otro empleado? [S/N] => ")
        elif agregar_empleado == "N":
            print("paso paso paso")
            break
        else:
            print("opcion ingresada invalida, intente nuevamente")
            agregar_empleado = input("agregar un empleado? [S/N] => ")
    calcular_sueldos(empleados)

def calcular_sueldos(empleados):
    #Si el empleado tiene más de 10 años de antigüedad: aumento del 10%
    #Si el empleado tiene más de 2 hijos: aumento del 10%, si solo tiene uno 5%
    #Si el empleado posee estudios superiores: aumento del 5%
    #sueldo_basico, antiguedad, cant_hijos, estudios_superiores
    for i in range(len(empleados)):
        sueldo_nuevo = empleados[i][1]
        
        if empleados[i][1] > 10:
            sueldo_nuevo += empleados[i][0] + (empleados[i][0] * 0.10)
            
        if empleados[i][2] > 1:
            sueldo_nuevo += empleados[i][0] + (empleados[i][0] * 0.10)
        else:
            sueldo_nuevo += empleados[i][0] + (empleados[i][0] * 0.05)
            
        if empleados[i][3] == "S":
            sueldo_nuevo += empleados[i][0] + (empleados[i][0] * 0.05)
        else:
            sueldo_nuevo += empleados[i][0] + (empleados[i][0] * 0.05)
        
        empleados[i].append(sueldo_nuevo)
        print(f"empleado{i+1}\n"
          f"{ '_' * 50}\n" 
          f"sueldo_basico: {empleados[i][0]}\n"
           f"{ '_' * 50}\n" 
          f"antiguedad: {empleados[i][1]}\n"
           f"{ '_' * 50}\n" 
          f"cant_hijos: {empleados[i][2]}\n"
           f"{ '_' * 50}\n" 
          f"estudios_superiores: {empleados[i][3]}\n"
           f"{ '_' * 50}\n" 
          f"nuevo sueldo: {empleados[i][4]}\n"
           f"{ '_' * 50}\n" 
            )
empleados_empresa()


