"""
Existen dos reglas que identifican dos conjuntos de valores:

a) El n�mero es de un solo d�gito.
b) El n�mero es impar.
A partir de estas reglas, escribir un programa que permita ingresar un n�mero entero.

Debe asignar el valor que corresponda a las variables booleanas:

esDeUnSoloDigito
esImpar
estaEnAmbos
noEstaEnNinguno
el valor Verdadero o Falso, seg�n corresponda, para indicar si el valor n�mero ingresado pertenece 
o no a cada conjunto. 
Definir un lote de prueba de varios n�meros y probr el algoritmo, escribiendo los resultados.

"""

import random

numeros_aleatorios = []
for i in range(11):
    numeros_aleatorios.append(random.randrange (1,99))

esDeUnSoloDigito = None
esImpar = None
estaEnAmbos = None
noEstaEnNinguno = None

for i in numeros_aleatorios:
    if i < 10 and i % 2 == 0:
        esDeUnSoloDigito = True
        esImpar = False
        estaEnAmbos = False
        noEstaEnNinguno = False
        print(f"el numero {i}\n es de un solo dijito? {esDeUnSoloDigito}\n es impar? {esImpar} \n esta en ambos? {estaEnAmbos}\n no esta en ninguno? {noEstaEnNinguno}")
    elif i < 10 and i %2 != 0:
        esDeUnSoloDigito = True
        esImpar = True
        estaEnAmbos = True
        noEstaEnNinguno = False
        print(f"el numero {i}\n es de un solo dijito? {esDeUnSoloDigito}\n es impar? {esImpar} \n esta en ambos? {estaEnAmbos}\n no esta en ninguno? {noEstaEnNinguno}")
    elif i >= 10 and i %2 != 0:
        esDeUnSoloDigito = False
        esImpar = True
        estaEnAmbos = False
        noEstaEnNinguno = False
        print(f"el numero {i}\n es de un solo dijito? {esDeUnSoloDigito}\n es impar? {esImpar} \n esta en ambos? {estaEnAmbos}\n no esta en ninguno? {noEstaEnNinguno}")
    else:
        esDeUnSoloDigito = False
        esImpar = False
        estaEnAmbos = False
        noEstaEnNinguno = False
        print(f"el numero {i}\n es de un solo dijito? {esDeUnSoloDigito}\n es impar? {esImpar} \n esta en ambos? {estaEnAmbos}\n no esta en ninguno? {noEstaEnNinguno}")


