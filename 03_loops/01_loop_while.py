###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
###

# Módulo del sistema operativo
import os
_ = os.system("clear")

print("\nBucle while")
counter = 0
while counter <= 5:
  print(counter)
  counter += 1

print("\nBucle while con break")
counter = 0

while True:
  print(counter)
  counter += 1
  if counter == 5:
    break

# El continue, lo que hace es saltar esa iteración en concreto y continuar con el bucle
print("\nBucle con continue")
counter = 0
while counter < 10:
  counter += 1
  if counter % 2 == 0: 
    continue
  print(counter)

# else, esta condición cuando se ejecuta?
# Cuando el bucle termina normalmente, es decir, cuando la condición es False
# No se ejecuta si el bucle termina con un break
print("\nBucle while con else:")
counter = 0
while counter < 5:
  print(counter)
  counter += 1
else:
  print("El bucle ha terminado")

# Pedirle al usuario un número que tiene que ser positivo en un bucle
# Utilizamos try y except para manejar el error en caso de que no introduzca un número
print("\nPedirle al usuario información en un bucle:")
number = -1
while number < 0:
  try:
    number = int(input("Escribe un número positivo: "))
    if number < 0:
      print("El número debe ser positivo. Intenta otra vez.")
  except:
    print("Debes introducir un número. Intenta otra vez.")

print(f"El número que has introducido es {number}")
