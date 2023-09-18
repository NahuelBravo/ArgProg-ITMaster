"""
Escribir un programa que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final.
El fin de la carga se determina ingresando un -1 en el legajo.

Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4. 
Se debe validar que la nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar:

Cantidad de alumnos que aprobaron (nota >= 4). Cantidad de alumnos que desaprobaron el examen (nota < 4). 
Porcentaje de alumnos que están aplazados (nota == 1).


"""

def validar_datos_examen():
    legajo = int(input("ingrese el numero de legajo => "))
    nota = int(input("ingrese la nota => "))
    alumnos = []
    validador = True
    
    while validador:
        if legajo == -1:
            validador = False
        elif legajo < -1:
            print(f"numero de legajo invalido, ingrese nuevamente")
            legajo = int(input("ingrese el numero de legajo => "))
        elif nota < 1 or nota > 10:
            print(f"nota invalida, ingrese nuevamente")
            nota = int(input("ingrese la nota => "))
        else:
            alumno = (legajo, nota)
            alumnos.append(alumno)
            legajo = int(input("ingrese el numero de legajo => "))
            nota = int(input("ingrese la nota => "))
    
    informe(alumnos)

def informe(alumnos):
    cant_aprobados = 0
    cant_desaprobados = 0
    cant_aplazados = 0
    
    for i in range(len(alumnos)):
        if alumnos[i][1] >= 4:
            cant_aprobados += 1
            print(f"numero de legajo: {alumnos[i][0]}, nota de examen: {alumnos[i][1]} (aprobado)")
        elif alumnos[i][1] < 4 and alumnos[i][1] > 1 :
            cant_desaprobados += 1
            print(f"numero de legajo: {alumnos[i][0]}, nota de examen: {alumnos[i][1]} (desaprobado)")
        elif alumnos[i][1] == 1:
            print(f"numero de legajo: {alumnos[i][0]}, nota de examen: {alumnos[i][1]} (desaprobado)")
            cant_aplazados += 1
            cant_desaprobados += 1
    porcentaje_aplazados = (cant_aplazados /(cant_aprobados + cant_desaprobados + cant_aplazados)) * 100 
    print(f"numero de alumnos aprobados: {cant_aprobados}")
    print(f"numero de alumnos desaprobados: {cant_desaprobados}")
    print(f"porcentaje de aplazados: {porcentaje_aplazados}")
    
validar_datos_examen()