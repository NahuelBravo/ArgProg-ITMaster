"""
Escribir un programa en Python que solicite al usuario ingresar dos valores 
que representen las medidas en grados de dos ángulos interiores de un triángulo. 
Luego, calcular y mostrar por pantalla el valor en grados del ángulo restante.

Es importante recordar que la suma de los ángulos interiores de todo triángulo es de 180 grados. 
Es decir, la suma de los ángulos internos de un triángulo siempre es igual a 180 grados. 
Por lo tanto, para calcular el ángulo restante es necesario restar la suma de los dos ángulos 
interiores ingresados al valor 180."

Para pensar:
¿Qué pasaría si se ingresan valores negativos como medidas de ángulos?
¿Qué sucedería si la suma de los dos ángulos ingresados es mayor o igual a 180 grados?
"""

angulo1 = int(input("ingrese en primer angulo => "))
angulo2 = int(input("ingrese el segundo angulo => "))

if angulo1 < 0 or angulo2 < 0:
    print("no se admiten valores negativos")
elif angulo1 + angulo2 >=180:
    print("no se admiten valores que sumados superen 180°(grados)")
else:
    angulo3 = 180 -(angulo1 + angulo2)
    print(f"El tecer angulo tienen un valor de {angulo3}° (grados)")