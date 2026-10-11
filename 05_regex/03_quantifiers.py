###
# 03 - Quantifiers
# Los cuantificadores se utilizan para especificar cuántas ocurrencias de un carácter o grupo de caracteres se deben encontrar en una cadena.
###

# Limpiar la terminal
import subprocess
_ = subprocess.run(["clear"], check=False)

# Módulo de regex
import re

# *: Puede aparecer 0 o más veces
print("\n*: Puede aparecer 0 o más veces")
text = "aaaba"
pattern = "a*"
matches = re.findall(pattern, text)
print(matches) # ['aaa', '', 'a', '']

# +: Una a más veces
print("\n+: Una a más veces")
text = "dddd aaa ccc a bb aa casa"
pattern = "a+"
matches = re.findall(pattern, text)
print(matches) # ['aaa', 'a', 'aa', 'a', 'a']

# ?: Cero o una vez
print("\n?: Cero o una vez")
text = "aaabacb"
pattern = "a?b"
matches = re.findall(pattern, text)
print(matches) # ['ab', 'b']

# Ejercicio 1: Haz opcional que aparezca un +34 en el siguiente texto
print("\nEjercicio 1: Haz opcional que aparezca un +34 en el siguiente texto")
phone = "+34 688999999"
# phone = "688999999"
pattern = r"(\+34 )?\d{9}"
found = re.search(pattern, phone)
if found: print(f"El teléfono {phone} es válido")
else: print(f"El teléfono {phone} no es válido")

# {n}: Exactamente n veces
print("\n{n}: Exactamente n veces")
text = "aaaaaa         aa   aaaa"
pattern = "a{3}"
matches = re.findall(pattern, text)

print(matches) # ['aaa', 'aaa', 'aaa']

# {n, m}: De n a m veces
text = "u uu uuu u"
pattern = r"\w{2,3}"
matches = re.findall(pattern, text)
print(matches) # ['uu', 'uuu']

# Ejercicio 2:
# Encuentra las palabras de 4 a 6 letras en el siguiente texto
print("\nEjercicio 2: Encuentra las palabras de 4 a 6 letras en el siguiente texto")
words = "ala casa árbol león cinco murcielago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, words)
print(matches) # ['casa', 'árbol', 'león', 'cinco']


# Ejercicio 3
# Encuentra las palabras de más de 6 letras
print("\nEjercicio 3: Encuentra las palabras de más de 6 letras en el siguiente texto")
words = "ala fantastico casa árbol león cinco murcielago"
pattern = r"\b\w{6,}\b"
matches = re.findall(pattern, words)
print(matches) # ['fantastico', 'murcielago']