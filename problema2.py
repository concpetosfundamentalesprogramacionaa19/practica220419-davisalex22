"""
Problema '2'
"""
# Ingreso de datos por teclado
x = input("Ingrese el valor de la variable x: \n")
y = input("Ingrese el valor de la variable y: \n")
z = input("Ingrese el valor de la variable z: \n")
# Realizacion de los calculos pertinentes
part1 = float(x)+(float(y)/float(z))
part2 = float(x)-(float(y)/float(z))
m = float(part1)/float(part2)
# Muestra por pantalla del resultado
print("x= %s\n y= %s\n  z= %s\n da como resultado:\n m= %.2f\n"%(x,y,z,m))

