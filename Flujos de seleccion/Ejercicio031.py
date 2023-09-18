"""
Una editorial determina el precio de un libro seg�n la cantidad de p�ginas que contiene. 
El costo b�sico del libro es de $1000, m�s $35,10 por p�gina con encuadernaci�n r�stica. 
Si el n�mero de p�ginas supera las 300 la encuadernaci�n debe ser especial, 
lo que incrementa el costo en $1200. 
Adem�s, si el n�mero de p�ginas sobrepasa las 600 se hace necesario otro procedimiento de encuadernaci�n 
que incrementa el costo en $880. Desarrollar un programa que calcule el costo de un libro dado el n�mero de 
p�ginas.

En Python no existen constantes como tal, pero se utiliza una convenci�n de nomenclatura en may�sculas
para indicar que una variable no debe ser modificada. 
Esto se conoce como "constante simb�lica" o "constante convencional". 
Para definir una constante convencional, simplemente se define una variable con un nombre en may�sculas.

Por ejemplo, para el problema anterior, se pueden definir las constantes:

COSTO_BASICO con valor 1000

COSTO_POR_PAGINA con valor 35.10

COSTO_ENC_RUSTICA con valor 1200

COSTO_ENC_ESPECIAL con valor 880.

Es una buena pr�ctica utilizar constantes para almacenar valores fijos en un programa, 
ya que facilita la lectura del c�digo y su mantenimiento, evita errores por la modificaci�n 
accidental de valores y permite un f�cil ajuste de los valores fijos en caso de ser necesario.

# constantes simb�licas
COSTO_BASICO = 1000
COSTO_POR_PAGINA = 35.10
COSTO_ENC_RUSTICA = 1200
COSTO_ENC_ESPECIAL = 880

num_paginas = int(input("Ingrese el n�mero de p�ginas del libro: "))
costo = COSTO_BASICO + (COSTO_POR_PAGINA * num_paginas)

# Escriba lo que falta de la soluci�n aqu�

print("El costo del libro es: $", costo)
"""

COSTO_BASICO = 1000
COSTO_POR_PAGINA = 35.10