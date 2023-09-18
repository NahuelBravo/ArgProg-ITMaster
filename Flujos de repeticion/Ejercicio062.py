"""
Un entrenador le ha propuesto a un atleta recorrer una ruta de cinco kilómetros durante 10 días para determinar 
si es apto para la prueba de 5 kilómetros que se desarrollará en el Parque. 
No se sabe si está apto y para eso nos piden que hagamos el siguiente programa.

Nos ingresan por cada día de entrenamiento tiempo de la prueba en minutos (entero mayor que 0 y menor a 100)

Para considerarlo apto debe cumplir las siguientes condiciones:

Que en ninguna de las pruebas haga un tiempo mayor a 20 minutos.
Que al menos en una de las pruebas realice un tiempo menor de 15 minutos.
Que su promedio sea menor o igual a 18 minutos.
Se pide:

Diseñar un algoritmo para registrar los datos y decidir si es apto para la competencia.
*Sólo en caso de estar apto, informar el promedio y el número de día en el que realizó el menor tiempo
"""

def ingresar_tiempo():
    tiempo_del_dia = int(input(f"Ingrese el tiempo del entrenamiento del dia => "))
    
    while True:
        if tiempo_del_dia < 0 or tiempo_del_dia > 100 :
            print("tiempo ingresado invalido, intente nuevamente")
            tiempo_del_dia = int(input(f"Ingrese el tiempo del entrenamiento del dia => "))
        else:
            return tiempo_del_dia
            False
    
    

def tiempos_entrenamientos():
    tiempos_dias = []
    for i in range(10):
        tiempos_dias.append(ingresar_tiempo())
    
    return tiempos_dias

def aptitud_atleta():
    tiempos_dias = tiempos_entrenamientos()
    es_apto = True
    tiempos_totales = 0

    for i in tiempos_dias:
        tiempos_totales += i
    
    promedio = tiempos_totales / (len(tiempos_dias))
    tiempo_mas_bajo = min(tiempos_dias)   
    
    for i in tiempos_dias:
        if i > 20:
            es_apto = False
        elif i != 15:
            es_apto = False
        elif promedio > 18:
            es_apto = False
        else:
            es_apto = True

    if es_apto == True:
        print(f"El atleta es apto, tiene un tiempo promedio de {promedio}, su tiempo mas bajo es {tiempo_mas_bajo}")
    else:
        print("el atleta no es apto")
aptitud_atleta()