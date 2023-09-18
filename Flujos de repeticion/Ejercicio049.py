"""
Escribir un programa que permita validar una opci�n ingresada. 
Se le preguntar� al usuario si desea continuar con alguna operaci�n de la forma "�Dese�s continuar? [S/N]". 
Se espera que el usuario ingrese una 'S' o una 'N' (incluir las min�sculas). 
La opci�n debe ser ingresada tanto como sea necesario hasta que quede comprendida dentro de las posibilidades esperadas.
"""
def validar_opcion():
    validador = True
    opcion = input("¿Desea continuar? [S/N]")
    
    while validador:
        if opcion == "S" or opcion == "s":
            print("Continuar con la operación")
            print(opcion)
            validador = False
        elif opcion == "N" or opcion == "n":
            print("Hasta luego")
            print(opcion)
            validador = False
        else:
            print("Opción inválida")
            print(opcion)
            opcion = input("¿Desea continuar? [S/N]")    
validar_opcion()