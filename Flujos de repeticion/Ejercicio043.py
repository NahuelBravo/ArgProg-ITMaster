"""
Escribir un programa que lea n�meros enteros hasta que se la suma de �stos sea mayor que 100, 
y muestre la cantidad de n�meros ingresados.

"""
num = int(input("ingrese un numero => "))
suma = 0
numList = []

while suma < 100:
    suma += num
    numList.append(num)
    num = int(input("ingrese un numero => "))
    
print(f"cantidad de numeros ingresados es: {len(numList)}\n estos numeros sumados dan un total de: {suma}")   