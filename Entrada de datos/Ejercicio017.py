"""
¡Ayuda! Se me rompió el programa que convierte una cantidad de dinero en la cantidad mínima de billetes y 
monedas necesarios. Tengo todas las instrucciones necesarias, pero están todas mezcladas. 
¿Podrías ayudarme a ordenarlas de manera correcta para que funcione el programa como debería? 
A lo mejor se me perdieron algunas instrucciones, ¿podrías agregarlas?



resto = cantidad_total
billetes_cien = resto // 100
resto = resto % 100
billetes_cinco = resto // 5
billetes_mil = resto // 1000
billetes_cincuenta = resto // 50
billetes_doscientos = resto // 200
billetes_diez = resto // 10
billetes_docientos = resto // 200
resto = resto % 10
cantidad_total = int(input("Ingrese la cantidad de dinero a convertir: "))
billetes_uno = resto // 1
print("Para la cantidad de  ",𝑐𝑎𝑛𝑡𝑖𝑑𝑎𝑑𝑡𝑜𝑡𝑎𝑙,"𝑠𝑒𝑛𝑒𝑐𝑒𝑠𝑖𝑡𝑎𝑛:")
𝑝𝑟𝑖𝑛𝑡(𝑏𝑖𝑙𝑙𝑒𝑡𝑒𝑠𝑚𝑖𝑙,"𝑏𝑖𝑙𝑙𝑒𝑡𝑒𝑠𝑑𝑒 1000")
print(billetes_doscientos, "billetes de  200")
𝑝𝑟𝑖𝑛𝑡(𝑏𝑖𝑙𝑙𝑒𝑡𝑒𝑠𝑐𝑖𝑒𝑛,"𝑏𝑖𝑙𝑙𝑒𝑡𝑒𝑠𝑑𝑒 100")
print(billetes_cincuenta, "billetes de  50")
𝑝𝑟𝑖𝑛𝑡(𝑏𝑖𝑙𝑙𝑒𝑡𝑒𝑠𝑑𝑖𝑒𝑧,"𝑏𝑖𝑙𝑙𝑒𝑡𝑒𝑠𝑑𝑒 10")
print(billetes_cinco, "billetes de  5")
𝑝𝑟𝑖𝑛𝑡(𝑏𝑖𝑙𝑙𝑒𝑡𝑒𝑠𝑢𝑛𝑜,"𝑏𝑖𝑙𝑙𝑒𝑡𝑒𝑠𝑑𝑒 1")
"""
cantidad_total = int(input("Ingrese la cantidad de dinero a convertir: "))

billetes_mil = 0
billetes_docientos= 0
billetes_cien = 0
billetes_cincuenta = 0
billetes_diez = 0
billetes_cinco = 0
billetes_uno = 0
resto = cantidad_total

if resto != 0:
    billetes_mil = resto // 1000
    resto = resto % 1000
    billetes_doscientos = resto // 200
    resto = resto % 200
    billetes_cien = resto // 100
    resto = resto % 100
    billetes_cincuenta = resto // 50
    resto = resto % 50
    billetes_diez = resto // 10
    resto = resto % 10
    billetes_cinco = resto // 5
    resto = resto % 5
    billetes_uno = resto // 1
    resto = resto % 1
    











print("Para la cantidad de",cantidad_total,"se necesitan:")
print(billetes_mil,"billetes de 1000")
print(billetes_doscientos, "billetes de  200")
print(billetes_cien,"billetes de 100")
print(billetes_cincuenta, "billetes de  50")
print(billetes_diez,"billetes de 10")
print(billetes_cinco, "billetes de  5")
print(billetes_uno,"billetes de 1")