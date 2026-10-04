###
# 02 - Bucles (for)
# Permiten ejecutar un bloque de código repetidamente mientras ITERA un iterable o una lista
###

# Módulo del sistema operativo
import os
_ = os.system("clear")

print("\nBucle for:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)

name = "Joaquin"
for letter in name:
  print(letter)

print("\nBucle for enumarate:")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
  print(f"El índice {index} es la fruta: {fruit}")

print("\nBucles anidados:")
letters = ["A", "B", "C"]
numbers = [1, 2, 3]

for letter in letters:
  for number in numbers:
    print(f"{letter}{number}")

print("\nBucles for with break:")
animals = ["Lion", "Tiger", "Bear", "Zebra", "Elephant", "Dog", "Cat", "Bird", "Fish", "Snake"]
for i, animal in enumerate(animals):
  print(animal)
  if animal == "Dog":
    print(f"El perro está escondido en el índice {i}")
    break

print("\nBucles for with continue:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for animal in animales:
  if animal == "loro": continue
  
  print(animal)

#Comprensión de listas (list comprehension)
print("\nComprensión de listas:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

numbers = [1, 2, 3, 4, 5, 6]
pares = [num for num in numbers if num % 2 == 0]
print(pares)