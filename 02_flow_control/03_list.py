###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###

# Módulo del sistema operativo
import os
_ = os.system("clear")

print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5] # Lista de enteros
lista2 = ["manzana", "pera", "uva"] # Lista de strings
lista3 = [1, "manzana", True, 3.14] # Lista de diferentes tipos
lista_vacia = []
lista_de_listas = [[1, 2], [3, 4]]

print("\nAcceso a elementos por índice")
print(lista2[0]) # manzana
print(lista2[1]) # pera
print(lista2[-1]) # uva
print(lista2[-2]) # pera
print(lista_de_listas[1][0]) # 3

print("\nSlicing:")
print(lista1[1:4]) # [2, 3, 4]
print(lista1[:3]) # [1, 2, 3]
print(lista1[3:]) # [4, 5]
print(lista1[:]) # [1, 2, 3, 4, 5] - Copia completa de la lista

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista1[::2]) # [1, 3, 5, 7, 9] - Step de 2
print(lista1[::3]) # [1, 4, 7, 10] - Step de 3
print(lista1[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] - Invertido

print("\nModificar una lista:")
lista1[0] = 20
print(lista1) # [20, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista1[100] = 20 Si inventas un índice que no existe dará error

print("\nAñadir elementos a una lista:")
lista1 = [1, 2, 3]
lista1 = lista1 + [4, 5, 6] # Concatena las listas - Forma larga
lista1 += [7, 8, 9] # Concatena las listas - Forma corta
print(lista1) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\nRecuperar longitud de una lista:")
print("Longitud de la lista:", len(lista1)) # 9