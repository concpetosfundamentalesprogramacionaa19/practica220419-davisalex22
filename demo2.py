"""
             Ejemplo de lenguaje Python
    autor: @davidsalazar
"""


import sys

variable = sys.argv[0]
valor1 = sys.argv[1]
valor2 = sys.argv[2]
# transformarcion de cadena  a entero
resultado1 = int(valor1)+int(valor2) # En esta linea se realiza la suma de variables
resultado2 = int(valor1)*int(valor2) # En esta linea se realiza la multiplicación de varibles
# Mostrar resultados
print("La suma entre los valores:    %d" % resultado1)
print("La multiplicación es:    %d" % resultado2) 

