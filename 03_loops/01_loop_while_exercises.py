###
# EJERCICIOS (while)
###

# Módulo del sistema operativo
import os
_ = os.system("clear")

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
counter = 10
while counter > 0:
  print(counter)
  counter -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
counter = 1
result = 0
while counter <= 20:
  if counter % 2 == 0:
    result += counter
  counter += 1
print(f"La suma de los números pares hasta 20 es: {result}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")
number = int(input("Introduce un número entero positivo:\n"))
factorial = 1
counter = 1
while counter <= number:
  factorial *= counter
  counter += 1
print(f"El factorial de {number} es {factorial}")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")
password = ""
while len(password) < 8:
  password = input("Introduce tu contraseña:\n")
  if len(password) < 8:
    print("La contraseña debe tener al menos 8 caracteres. Inténtalo de nuevo.")

print("Contraseña válida")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")
number = int(input("Introduce un número entero positivo:\n"))
multiplier = 1
while multiplier <= 10:
  result = number * multiplier
  print(f"{number} * {multiplier} = {result}")
  multiplier += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")
n = int(input("Introduce un número entero positivo:\n"))
number = 2

while number <= n:
  divisor = 2
  is_prime = True
  while divisor < number:
    if number % divisor == 0:
      is_prime = False
      break
    divisor += 1
  if is_prime:
    print(number)
  number += 1