"""
Escribir un programa que permita al usuario ingresar números hasta que se introduzca un 0.

La computadora debe mostrar el número máximo y el número mínimo.
"""

def ingrese_numeros():
    numero = int(input("ingrese un numero (ingrese 0 para detener) => "))
    numeros = []
    validador = True
    while validador:
        if numero == 0:
            validador = False
        else:
            numeros.append(numero)
            numero = int(input("ingrese un numero (ingrese 0 para detener) => "))
    print(numeros) 
    numero_minimo(numeros)
    numero_maximo(numeros)

def numero_minimo(numeros):
    minimo = min(numeros)
    print(f"el numero minimo es {minimo}")
   
   
def numero_maximo(numeros):
    maximo = max(numeros)
    print(f"el numero maximo es {maximo}")


ingrese_numeros()