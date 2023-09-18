"""
Escribir un programa que permita controlar con validación el ingreso a un sitio web. 
Teniendo dos constantes con un nombre de usuario ("admin") y una contraseña ("123456"), 
el programa debe permitir al usuario ingresar sus credenciales. 
Si las mismas son erróneas, se volverán a pedir hasta un máximo de 3 intentos. 
Finalmente, la computadora debe mostrar alguno de los siguientes mensajes según sea el caso: "Acceso concedido" 
o "Se ha bloqueado la cuenta"
"""

def validar_acceso():
    CONTRASENIA = "123456"
    USUARIO = "admin"
    intentos = 3
    usuario = input("ingrese su usuario => ")
    contraseña = input("ingrese su contraseña => ")
    validador = True
    
    while validador:
        if intentos == 0:
            print("Se ha bloqueado la cuenta: supero el numero de intentos")
            validador = False
        elif usuario != USUARIO:
            intentos -= 1
            print(f"Usuario invalido, le quedan {intentos + 1} intentos")
            usuario = input("ingrese su usuario => ")
        elif contraseña != CONTRASENIA:   
            intentos -= 1
            print(f"Contraseña invalido, le quedan {intentos +1} intentos")
            contraseña = input("ingrese su contraseña => ")
        else:
            print("Acceso concedido")
            validador = False
            
validar_acceso()