###
# 02 - Meta caracteres
# Los metacaracteres son simbolos especiales con significados especificos en las expresiones regulares
###

# Módulo del sistema operativo
import os
_ = os.system("clear")

# Módulo de regex
import re

# El punto (.)
# Coincidir con cualquier caracter excepto una nueva linea
print("\nEl punto (.):")

text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = r"H.la" # Hola, H0la, H$la

found = re.findall(pattern, text)

if (found):
  print(found)
else:
  print("No se ha encontrado el patrón")


text = "casa caasa cosa cisa cesa causa"
pattern = r"c.sa" # el punto (.) es un metacaracter que coincide con cualquier caracter pero solo una vez

matches = re.findall(pattern, text)
print(matches)

# Buscar coincidencias que sean literalmente el punto "." utilizando la barra invertida (\)
print("\nBuscar coincidencias que sean literalmente el punto \".\":")
text = "Mi casa es blanca. Y el coche es negro."
pattern = r"\."

matches = re.findall(pattern, text)

print(matches)

# --------------------

# \d -> Coincidir con cualquier dígito (0-9)
print("\n\\d -> Coincidir con cualquier dígito (0-9):")
text = "Mi número de teléfono es 123456789"
found = re.findall(r"\d{9}", text)
print(found)

# Ejercicio: Detectar si hay un número de España en el texto gracias al prefijo +34
print("\nEjercicio 1: detectar si hay un número de España en el texto.")
text = "Mi número de teléfono es +34 688999999 apúntalo vale?"
pattern = r"\+34 \d{9}"
found_phone_number = re.search(pattern, text)
if found_phone_number: print(f"Encontré el número de teléfono {found_phone_number.group()}")

# --------------------

# \w: Coincide con cualquier caracter alfanumérico (a-z, A-Z, 0-9, _)
print("\n\\w coincidir cualquier caracter alfanumérico:")
text = "@@el_rubius_69$!"
pattern = r"\w"
found = re.findall(pattern, text)
print(found) # ['e', 'l', '_', 'r', 'u', 'b', 'i', 'u', 's', '_', '6', '9']

# --------------------

# \s: Coincide con cualqueir espacio en blanco (espacio, tabulación, salto de línea)
print("\n\\s coincidir con cualquier espacio en blanco:")
text = "Hola mundo\n¿Cómo estás?\t"
pattern = r"\s"
matches = re.findall(pattern, text)
print(matches)

# --------------------

# ^: Coincide con el principio de una cadena
print("\n^: Coincide con el principio de una cadena:")
username = "423_name%22" 
pattern = r"^\w" # validar nombre de usuario

valid = re.search(pattern, username)

if valid: print("El nombre de usuario es válido")
else: print("El nombre de usuario no es válido")

phone = "+34 688999999"
pattern = r"^\+\d{1,3} " # es importante el espacio al final, porque sino esto sería valido: +3412345

valid = re.search(pattern, phone)

if valid: print("El número de teléfono es válido")
else: print("El número de teléfono no es válido")

# --------------------

# $: Coincide con el final de una cadena
print("\n$: Coincide con el final de una cadena:")
text = "Hola mundo."
pattern = r"mundo$"

valid = re.search(pattern, text)

if valid: print("La cadena es válida")
else: print("La cadena no es válida")

# --------------------

# EJERCICIO 1
# Valida que un correo sea de gmail
print("\nEjercicio 1: Valida que un correo sea de gmail")
text = "midudev@gmail.com"
pattern = r"^\w+@gmail.com$"
valid = re.search(pattern, text)

if valid: print("El correo es válido")
else: print("El correo no es válido")

# --------------------

# EJERCICIO 2:
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
print("\nEjercicio 2: saber los nombres de los ficheros con extension .txt")
files = "file1.txt file2.pdf midu-of.webp secret.txt"
pattern = r"\w+\.txt"
valid_files = re.findall(pattern, files)
print(f"Archivos .txt: {valid_files}")

# --------------------

# \b: Coincide con el principio o final de una palabra
print("\n\\b: Coincide con el principio o final de una palabra:")
text = "casa casada cosa cosas casado casa"
pattern = r"\bc.sa\b"

found = re.findall(pattern, text)
print(found)

# |: Coincidr con una opción u otra
print("\n|: Coincidr con una opción u otra:")
fruits = "platano, piña, manzana, aguacate, palta, pera, aguacate, aguacate"
pattern = r"palta|aguacate|p..a|\b\w{7}\b"

matches = re.findall(pattern, fruits)
print(matches)