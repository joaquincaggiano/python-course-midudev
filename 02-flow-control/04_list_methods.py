###
# 04 - Listas Métodos
# Los métodos más importantes para trabajar con listas
###

# Módulo del sistema operativo
import os
_ = os.system("clear")

list1 = ["a", "b", "c", "d"]

print("\nAñadir o insertar elementos a una lista:")
list1.append("e") # Añade un elemento al final de la lista
print(list1)
list1.insert(1, "@") # Inserta un elemento en una posición específica
print(list1)
list1.extend(["f", "g", "h"]) # Añade varios elementos al final de la lista
print(list1)

print("\nEliminar elementos de una lista:")
list1.remove("@") # Elimina el primer elemento que coincide con el valor
print(list1)
last_element = list1.pop() # Elimina el último elemento de la lista y te devuelve el valor
print("last_element:", last_element)
print(list1)
list1.pop(1) # Elimina el elemento en la posición 1. También podemos enviar índices negativos
print(list1)
del list1[1] # Elimina el elemento en la posición 1. También podemos enviar índices negativos
print(list1)
list1.clear() # Elimina todos los elementos de la lista
print(list1)
list1 = ["a", "b", "c", "d"]
print("Nueva lista:", list1)
del list1[1:3] # Elimina los elementos en las posiciones 1 y 2
print(list1)

print("\nOrdenar elementos de una lista modificando la lista original:")
numbers = [4, 1, 5, 9, 2, 6, 3]
numbers.sort() # Ordena los elementos de la lista, no devuelve una lsita nueva
print(numbers)

print("\nOrdenar elementos de una lista creando una nueva lista:")
numbers = [4, 1, 5, 9, 2, 6, 3]
sorted_numbers = sorted(numbers) # Ordena los elementos de la lista y crea una nueva lista
print("sorted_numbers:", sorted_numbers)
print("numbers:", numbers)

print("\nOrdenar una lista de cadenas de texto (todo minúscula)")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("\nOrdenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)
print(frutas)

print("\nCosas útiles sobre listas:")
animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals)) # Tamaño de la listas -> 4
print(animals.count('🐶')) # Cuantas veces aparece el elemento '🐶' -> 2
print('🐼' in animals) # Comprueba si hay un '🐼' en la lista -> True
print('🐹' in animals) # -> False