# Limpiar la terminal
import subprocess
_ = subprocess.run(["clear"], check=False)

# Módulo de regex
import re

# [: Coincide con cualquier caracter dentro de los corchetes.
print("\n[]: Coincide con cualquier caracter dentro de los corchetes.")
username = "rub.ius_69+"
pattern = r"^[\w._%+-]+$"

match = re.search(pattern, username)
if match:
  print(f"El usuario es válido: {match.group()}")
else:
  print("El usuario no es válido")

# Buscar todas las vocales de una palabra
print("\nBuscar todas las vocales de una palabra:")
text = "Hola mundo"
pattern = r"[aeiou]"

matches = re.findall(pattern, text)
print(matches)

# Una regex para encontrar las palabras man, fan y ban, pero que ignore el resto
print("\nUna regex para encontrar las palabras man, fan y ban, pero que ignore el resto:")
text = "man fan ban ran ñam omniman fanatico bandana"
pattern = r"\b[mfb]an\b"

matches = re.findall(pattern, text)
print(matches)

# [^]: Coincide con cualquier caracter que no esté dentro de los corchetes
print("\n[^]: Coincide con cualquier caracter que no esté dentro de los corchetes:")
text = "Hola mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches)