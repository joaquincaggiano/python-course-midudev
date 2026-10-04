###
# EJERCICIOS
###

# Módulo del sistema operativo
import os
_ = os.system("clear")

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
print("\nEjercicio 1:")
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
mensaje_secreto = mensaje[7:]
print(mensaje_secreto)

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
print("\nEjercicio 2:")
numbers = [10, 20, 30, 40, 50]
numbers[0] = 50
numbers[-1] = 10
# numeros[0], numeros[-1] = numeros[-1], numeros[0] # Intercambio en una sola línea.
print(numbers)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
print("\nEjercicio 3:")
bread = ["pan arriba"]
ingredients = ["jamón", "queso", "tomate"]
bread_down = ["pan abajo"]
sandwich = bread + ingredients + bread_down
print(sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
print("\nEjercicio 4:")
list = [1, 2, 3]
list_duplicated = list + list
print(list_duplicated)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30
print("\nEjercicio 5:")
list = [10, 20, 30, 40, 50]
# center = len(list) // 2 # -> divide y se queda solo con la parte entera, sin decimales
center = int(len(list) / 2)
print(list[center])

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
print("\nEjercicio 6:")
list = [1, 2, 3, 4, 5, 6]
center = len(list) // 2
first_half = list[:center]
second_half = list[center:]
print("Primera mitad:", first_half)
print("Segunda mitad:", second_half)
first_half_reversed = first_half[::-1]
print("Primera mitad revierta:", first_half_reversed)
result_list = first_half_reversed + second_half
print("Resultado:",result_list)
