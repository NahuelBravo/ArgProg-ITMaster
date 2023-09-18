"""
Escribir un programa para un negocio de venta de granos que desea controlar las ventas realizadas. 
De cada venta ingresa el importe total y un código que indica la forma de pago. Los códigos puede ser:

C: cheque, 20% de recargo.
E: efectivo, 10% de descuento.
T: con tarjeta, 12% de recargo.
Se debe ingresar una F para finalizar el día de venta y arrojar los siguientes totales.

| Forma de Pago    | Total     |
| ---------------- | --------- | 
| Efectivo en Caja | $ xxxx.xx |
| Tarjeta Crédito  | $ xxxx.xx |
| Cheques          | $ xxxx.xx |
| Total de Venta   | $ xxxx.xx |
| Importe del IVA  | $ xxxx.xx |
"""

def ventas():
    importe = float(input("Ingrese el importe total de laventa => "))
    forma_de_pago = input("Ingrese forma de pago => ")
    
    ventas = []
    validador = True
    
    while validador:
        if importe == 0:
            print("importe ingresado invalido, intente nevamente")
            importe= float(input("Ingrese el importe total de laventa => "))
        elif forma_de_pago == 'F':
            print("finalizado")
            validador = False
        elif forma_de_pago == "C" or forma_de_pago == "c":
            venta = (forma_de_pago, importe)
            ventas.append(venta)
            importe = float(input("Ingrese el importe total de laventa => "))
            forma_de_pago = input("Ingrese forma de pago => ")
        elif forma_de_pago == "E" or forma_de_pago == "e":
            venta = (forma_de_pago, importe)
            ventas.append(venta)    
            importe = float(input("Ingrese el importe total de laventa => "))
            forma_de_pago = input("Ingrese forma de pago => ")
        elif forma_de_pago == "T" or forma_de_pago == "t":
            venta = (forma_de_pago, importe)
            ventas.append(venta) 
            importe = float(input("Ingrese el importe total de laventa => "))
            forma_de_pago = input("Ingrese forma de pago => ")
        else:
            print("forma de pago invalida, intente nuevamente")
            forma_de_pago = input("Ingrese forma de pago => ")     
    calcular_importes(ventas)
   
def calcular_importes(ventas):
    ventas_pago_cheque = 0
    ventas_pago_efectivo = 0
    ventas_pago_tarjeta = 0
    for i in range(len(ventas)):
        if ventas[i][0] == "C" or ventas[i][0] == "c":
           ventas_pago_cheque += (ventas[i][1] + (ventas[i][1] * 0.20))
        elif ventas[i][0] == "E" or ventas[i][0] == "e":
           ventas_pago_efectivo += (ventas[i][1] - (ventas[i][1] * 0.10))
        elif ventas[i][0] == "T" or ventas[i][0] == "t":
           ventas_pago_tarjeta += (ventas[i][1] + (ventas[i][1] * 0.12))
    importes_totales = ventas_pago_cheque + ventas_pago_efectivo + ventas_pago_tarjeta
    importe_IVA = importes_totales +(importes_totales * 0.21)
    print(f"| Forma de Pago    | Total     |\n| ---------------- | --------- |\n| Efectivo en Caja | $ {ventas_pago_efectivo} |\n| Tarjeta Crédito  | $ {ventas_pago_tarjeta} |\n| Cheques          | $ {ventas_pago_cheque} |\n| Total de Venta   | $ {importes_totales} |\n| Importe del IVA  | $ {importe_IVA} |")
ventas()