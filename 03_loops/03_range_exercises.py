###
# EJERCICIOS (range)
###

# Módulo del sistema operativo
import os
_ = os.system("clear")

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")
for num in range(1, 11):
  print(num)

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")
for num in range(1, 21):
  if num % 2 != 0:
    print(num)
# Otra forma:
# for i in range(1, 21, 2):  # El paso 2 asegura que solo se generen impares
#   print(i)

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")
for num in range(5, 51, 5):
  print(num)

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")
for num in range(10, 0, -1):
  print(num)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
sum = 0
for num in range(1, 101):
  sum += num
print(f"La suma de los números del 1 al 100 es: {sum}")

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")
num = int(input("Introduce un número entero positivo:\n"))
for i in range(1, 11):
  result = num * i
  print(f"{num} x {i} = {result}")
