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