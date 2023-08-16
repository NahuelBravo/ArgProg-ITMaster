"""
Definición del problema: Una inmobiliaria paga a sus vendedores un salario base, 
más una comisión fija por cada venta realizada, 
más el 5% del valor de esas ventas. 

Realizar un programa que imprima el nombre del vendedor y el salario que le corresponde en un determinado mes.
Se leen por teclado el nombre del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.

¿Sobran datos? ¿Qué datos sobran?

<<< Sobra el dato de la comision fija por cada venta, ya que se tiene una comision por el valor de la venta >>>
"""

vendedor = {'nombre': input("Ingrese el nombre del vendedor: "), 'cant_ventas': int(input("Ingrese la cantidad de ventas ")),'valor_total_ventas': int(input("Ingrese el valor total de ventas "))}
SUELDO_BASE = 200000 + int(input("Ingresar cantdad que aumento o disminuyo el sueldo fijo => "))
comision = 0.05
sueldo_del_mes = SUELDO_BASE +(vendedor['valor_total_ventas']*comision)
print(f"El vendedor {vendedor['nombre']}, le corresponde un sueldo de ${sueldo_del_mes} el corriente mes")