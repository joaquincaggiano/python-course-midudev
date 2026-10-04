###
# EJERCICIOS
###

# Módulo del sistema operativo
import os
_ = os.system("clear")

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
# number_a, number_b = input("Escribe 2 números cualquiera\n").split()
# number_a_cast = int(number_a)
# number_b_cast = int(number_b)

# if number_a_cast == number_b_cast:
#   print("El número A es igual al número B")
# elif number_a_cast > number_b_cast:
#   print("El número A es mayor al número B")
# else:
#   print("El número B es mayor al número A")


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
# num_a = float(input("Escribe el primer número\n"))
# num_b = float(input("Escribe el segundo número\n"))
# operation = input("Escribe la operación mátemática que quieras realizar (+, -, *, /):\n")

# if operation == "+":
#   print(num_a + num_b)
# elif operation == "-":
#   print(num_a - num_b)
# elif operation == "*":
#   print(num_a * num_b)
# elif operation == "/":
#   if num_b == 0:
#     print("No se puede dividir por 0")
#   else:
#     print(num_a / num_b)
# else:
#   print("Operación no válida")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
# year = int(input("Introduce un año para saber si es bisiesto:\n"))

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#   print("Es un año bisiesto")
# else:
#   print("No es un año bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)
age = int(input("Introduce una edad para saber en que categoría entra:\n"))

if age >= 65:
  print("Adulto mayor")
elif age >= 18 and age <= 64:
  print("Adulto")
elif age >= 13 and age <= 17:
  print("Adolescente")
elif age >= 3 and age <= 12:
  print("Niño")
elif age >= 0 and age <= 2:
  print("Bebé")
else:
  print("Edad no válida")

# Otra forma de hacerlo más simple:
age = int(input("Introduce una edad para saber en que categoría entra:\n"))
if age < 0:
  print("Edad no válida")
elif age <= 2:
  print("Bebé")
elif age <= 12:
  print("Niño")
elif age <= 17:
  print("Adolescente")
elif age <= 64:
  print("Adulto")
else:
  print("Adulto mayor")