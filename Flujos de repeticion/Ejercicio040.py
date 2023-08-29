"""
Escribir un programa que permita ingresar dos numeros enteros a y b. El programa debe mostrar:

La suma de los numeros pares entre a y b.
El producto de los numeros impares entre a y b.
"""

num1 = int(input("ingrese un numero => "))
num2 = int(input("ingrese otro numero => "))

imparesList = []
paresList = []
pares = 0

for i in range(num1, num2 + 1):
    if i%2 != 0:
        imparesList.append(i)
    else:
        paresList.append(i)

for i in paresList:
    pares += i
print(pares)
    
for i in imparesList:
    k = i + 1
    for k in imparesList:
        print(f"{k} * {i} = {k%i}")

    