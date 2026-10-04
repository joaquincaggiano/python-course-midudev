###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Módulo del sistema operativo
import os
_ = os.system("clear")

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.
print("\nEjercicio 1:")
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.insert(2, 10)
numbers[0] = 0
print(numbers)

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().
print("\nEjercicio 2:")
list_a = [1, 2, 3]
list_b = [4, 5, 6, 1, 2]
list_a.extend(list_b)
print("List A extended with B:", list_a)
list_a.remove(1)
print("Remove first number 1 to find:", list_a)
deleted_element = list_a.pop(3)
print("Deleted element from list A at index 3:", deleted_element)
list_b.clear()
print("Clear list B:", list_b)


# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.
print("\nEjercicio 3:")
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del list[2:5]
print(list)

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.
print("\nEjercicio 4:")
list = [5, 2, 8, 1, 9, 4, 2]
list.sort()
print(list)
print("Number 2 count:", list.count(2))
print("Existe el número 7 en la lista?:", 7 in list)

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.
print("\nEjercicio 5:")
original = [1, 2, 3]
copia_1 = original[:]
copia_2 = original.copy()
referencia = original
referencia[0] = 10
print("Original:", original)
print("Copia 1:", copia_1)
print("Copia 2:", copia_2)
print("Referencia a la lista original:", referencia)

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
print("\nEjercicio 6:")
fruits = ["Manzana", "pera", "BANANA", "naranja"]
fruits.sort(key=str.lower)
print("Frutas ordenadas:", fruits)