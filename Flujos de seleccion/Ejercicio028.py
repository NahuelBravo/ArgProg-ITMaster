"""
Crear un programa que pida un n�mero de mes (ejemplo 4) y escriba el nombre del mes en letras ("abril"). 
Verificar que el mes sea v�lido e informar en caso que no lo sea.
"""

numero_de_mes = int(input("Ingrese numero del mes => ")) - 1
nombre_del_mes = input("Ingrese nombre del mes => ")
meses = ["enero", "febrero", "marzo", "abril", "mayo",
         "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

if meses[numero_de_mes] == nombre_del_mes:
    print(f"el nombre del mes {nombre_del_mes} y el numero de mes {numero_de_mes + 1} es valido")
else:
    print(f"el nombre del mes {nombre_del_mes} y el numero de mes {numero_de_mes} es invalido")

    
