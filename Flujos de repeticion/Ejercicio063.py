"""
Escribir un programa para registrar y obtener información sobre los viajes diarios de un conductor de Uber.

Cada vez que comienza un viaje se debe ingresar la distancia recorrida, indicando si el viaje fue corto (‘C’),
mediano (‘M’), largo (‘L’) o si es el fin de los datos (‘Z’).

El día finaliza cuando se llega a los 30 viajes o cuando se ingresa distancia ‘Z’ (fin de los datos).

Por cada viaje se debe ingresar la siguiente información:
    Cantidad de pasajeros (mayor a 0 y menor a 4).
    Importe a cobrar, incluyendo la el costo básico ($180).

Por cada pasajero de ese viaje se debe ingresar:
    Nombre.
    Edad (mayor a 18 y menor a 120 años).


Se desea saber, para cada viaje, cuál es la persona más grande y su nombre.

Al finalizar el día de trabajo, el programa debe informar:

    Cantidad de viajes por cada categoría (‘C’, ‘M’, ‘L’).
    Recaudación total.
    Valor promedio del viaje.
    Porcentaje de viajes cortos.

Todos los datos ingresados deben ser validados.
"""
def dia_de_trabajo():
    def datos_viaje():
        tipo_de_viaje = input("Tipo de viaje [C/M/L]: ")
        cant_pasajeros = int(input("Cantidad de pasajeros: "))
        IMPORTE_BASICO = 180
        importe = int(input("Importe a cobrar (se le suma el importe basico de $180): ")) + IMPORTE_BASICO
        
        while True:
            if cant_pasajeros < 1 or cant_pasajeros > 4:
                print("cantidad de pasajeros es invalida, no se puede realizar el viaje")
                cant_pasajeros = int(input("Cantidad de pasajeros: "))
            elif tipo_de_viaje not in ['C', 'M', 'L']:
                print("tipo de viaje invalido, ingrese una opcion valida")
                tipo_de_viaje = input("Tipo de viaje [C/M/L]: ")
            else:
                pasajeros = datos_pasajeros(cant_pasajeros)
                pasajero_mas_grande = pasajero_grande(pasajeros)
                viaje = (tipo_de_viaje, pasajeros, importe, pasajero_mas_grande)
                return viaje

    def datos_pasajeros(cant_pasajeros):
        datos_pasajeros = []
        for i in range(cant_pasajeros):
            datos_pasajeros.append(pasajero())
        return datos_pasajeros

    def pasajero():
        nombre = input("Ingrese el nombre del pasajero: ")
        edad = int(input("Ingrese la edad del pasajero: "))
        
        if edad < 18 or edad > 120:
            pasajero = None
            return pasajero
        else:
            pasajero = (nombre, edad)
            return pasajero

    def validar_viaje(nuevo_viaje):
        for pasajero in nuevo_viaje[1]:
            if pasajero is None:
                print(f"Edad de un pasajero es invalida, no se puede realizar el viaje")
                return False
        return True

    def pasajero_grande(pasajeros):
        edades = [pasajero[1] for pasajero in pasajeros]
        mayor = max(edades)
        pasajero_grande = None
        
        for pasajero in pasajeros:
            if pasajero[1] == mayor:
                pasajero_grande = pasajero
                
        return pasajero_grande

    def valor_promedio(viajes_del_dia):
        recaudacion_total = sum(viaje[2] for viaje in viajes_del_dia)
        cant_viajes = len(viajes_del_dia)
        valor_promedio = recaudacion_total / cant_viajes 
        return valor_promedio  

    def recaudacion_total(viajes_del_dia):
        return sum(viaje[2] for viaje in viajes_del_dia)

    def porcentaje_viajes_cortos(viajes_del_dia):
        cant_viajes_cortos = sum(1 for viaje in viajes_del_dia if viaje[0] == 'C')
        cant_de_viajes = len(viajes_del_dia)
        porcentaje_viajes_cortos = (cant_viajes_cortos / cant_de_viajes) * 100
        return porcentaje_viajes_cortos

    def cantidad_tipos_de_viajes(viajes_del_dia):
        viajes_cortos = 0
        viajes_medios = 0
        viajes_largos = 0
        for viajes in viajes_del_dia:
            if viajes[0] == "C" :
                viajes_cortos += 1
            elif viajes[0] == "M":
                viajes_medios += 1
            else:
                viajes_largos += 1
        
        cant_viajes_categoria = (viajes_cortos, viajes_medios, viajes_largos)
        return cant_viajes_categoria
    
    realizar_viaje = input("Quiere realizar un viaje? [S/N]: ")
    viajes_del_dia = []
    CANT_VIAJES_DISPONIBLES = 30
    
    while True and CANT_VIAJES_DISPONIBLES > 0:
        if realizar_viaje == "S" or realizar_viaje == "s":
            nuevo_viaje = datos_viaje()
            if validar_viaje(nuevo_viaje):
                viajes_del_dia.append(nuevo_viaje)
                CANT_VIAJES_DISPONIBLES -= 1
                print(CANT_VIAJES_DISPONIBLES)
                realizar_viaje = input("Quiere realizar otro viaje? [S/N]: ")
            else:
                print("Viaje invalido, no se puede realizar")
                realizar_viaje = input("Quiere realizar otro viaje? [S/N]: ")
        elif realizar_viaje == "N" or realizar_viaje == "n":
            print(f"Tenga buen dia\n")
            CANT_VIAJES_DISPONIBLES = 30
            break  
        else:
            print("Opcion ingresada invalida, intente nuevamente")
            realizar_viaje = input("Quiere realizar un viaje? [S/N]: ")
    
    valor_promedio_viajes = valor_promedio(viajes_del_dia)
    recaudacion_total_valor = recaudacion_total(viajes_del_dia)
    cant_tipos_de_viaje = cantidad_tipos_de_viajes(viajes_del_dia)
    porcentaje_viajes_cortos = porcentaje_viajes_cortos(viajes_del_dia)
    
    print(f"VIAJES DEL DIA\n"
          f"{'-' * 80}\n"
          f"Recaudacion Total: ${recaudacion_total_valor}\n"
          f"Valor Promedio Viajes: ${valor_promedio_viajes}\n"
          f"Viajes Cortos: {porcentaje_viajes_cortos:.2f}%\n"
          f"Cantidad Tipos de Viaje: C: {cant_tipos_de_viaje[0]} M: {cant_tipos_de_viaje[1]} L: {cant_tipos_de_viaje[2]}")
    print(f"Pasajeros mas Grandes\n"
          f"{'-' * 80}\n")
    for viaje in range(len(viajes_del_dia)):
        print(f"Pasajero mas grande en el viaje N° {viaje + 1} es:\n" 
                f"  nombre: {viajes_del_dia[viaje][3][0]}\n" 
                f"  edad: {viajes_del_dia[viaje][3][1]}")
dia_de_trabajo()


