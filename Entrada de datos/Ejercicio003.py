"""
Escribir un programa que solicite al usuario su nombre y su edad, 
despu�s pida una cantidad de a�os y muestre por pantalla un mensaje
que indique cu�ntos a�os tendr� la persona despu�s de sumarle a su edad 
la cantidad de a�os ingresada. El mensaje debe tener el siguiente formato: 
    'Hola, [nombre]. Dentro de [cantidad] a�os tendr�s [edad + cantidad] a�os'".
"""

nombre = str(input('ingrese su nombre =>'))
edad = int(input('ingrese su edad =>'))
anios = int(input('ingrese una cantidad de anos =>'))
edad_futura = anios + edad

print(f'Hola, {nombre}. Dentro de {anios} años tendr�s {edad_futura} años')




