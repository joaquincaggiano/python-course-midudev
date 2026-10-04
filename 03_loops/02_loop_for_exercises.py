###
# EJERCICIOS (for)
###

# Módulo del sistema operativo
import os
_ = os.system("clear")

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for num in numbers:
  if num % 2 == 0:
    print(num)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
numbers = [10, 20, 30, 40, 50]
sum = 0
for num in numbers:
  sum += num
result = sum / len(numbers)
print("Media:", result)

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
numbers = [15, 5, 25, 10, 20]
max_value = numbers[0]
for num in numbers:
  if num > max_value:
    max_value = num
print(f"El número máximo es: {max_value}")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")
words = ["casa", "arbol", "sol", "elefante", "luna"]
words_filtered = [word for word in words if len(word) > 5]
print(f"Palabras con más de 5 caracteres: {words_filtered}")

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")
words = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
initial_letter = input("Introduce una letra:\n").lower()
counter = 0

for word in words:
  letter = word[0].lower()
  # if word.lower().startswith(initial_letter):
  if initial_letter == letter:
    counter +=1

print(f"Hay {counter} palabras que empiezan con '{initial_letter}'")