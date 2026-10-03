###
# 03 - casting de types
# Transformar un tipo de un valor a otro
###

# Módulo del sistema operativo
import os
os.system("clear")

print("Conversion de tipos:")
print(int("100"))
print(type(int("100")), end="\n\n")

# print(2 + "10") # Error: porque python tiene un tipado estricto
print(2 + int("100")) # 102
print("100" + str(2)) # 1002
print(int(3.14)) # 3
print(float("3.14"), end="\n\n") # 3.14

print(bool(1)) # True
print(bool(0)) # False
print(bool(-1), end="\n\n") # True

print(bool("")) # False
print(bool(" ")) # True
print(bool("Hola"), end="\n\n") # True

print("Round:")
print(round(2.5)) # 2
print(round(3.5)) # 4 - Se redondea al par más cercano
