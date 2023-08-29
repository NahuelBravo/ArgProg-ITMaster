"""
Escribir un programa que a partir de un n�mero entero cant ingresado por el usuario permita 
cargar por teclado cant n�meros enteros. 
La computadora debe mostrar cu�l fue el mayor n�mero y en qu� posici�n apareci�.

"""

num = int(input("ingrese un numero entero, para finalizar introduzca '0' =>" ))

numList = []

while num != 0:
    numList.append(num)
    num = int(input("ingrese un numero entero, para finalizar introduzca '0' =>" ))


maximo = max(numList)

for i in range (len(numList)):
    if numList[i] == maximo:
        print(f"El numero mas alto introducido fue: {maximo}, fue el {i+1}° numero introducido.")