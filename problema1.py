"""
Problema 1
"""
# Ingreso de datos por teclado
horas = input("Ingrese el número de horas de trabajo: \n")
costo = input("Ingrese el costo por horas oficial de trabajo: \n")
# Realizacion de los calculos pertinentes
sueldo = float(horas)*float(costo)
descuento = float(sueldo)*0.10
sueldoMensual = float(sueldo)-float(descuento)
# Muestra por pantalla del resultado
print("El valor mensual a pagar de un trabajador es:%s\n"%sueldoMensual)


