"""
¿Está en Equilibrio la Alianza entre Reed Richards y Johnny Storm?

En el universo de los 4 Fantásticos, la unión y el equilibrio entre los poderes es fundamental para enfrentar cualquier desafío. En este problema, nos centraremos en dos de sus miembros:

Reed Richards (Mr. Fantastic), representado por la letra R.
Johnny Storm (La Antorcha Humana), representado por la letra J.

Objetivo:

Crea una función en Python que reciba una cadena de texto. Esta función debe contar cuántas veces aparece la letra R (para Reed Richards) y cuántas veces aparece la letra J (para Johnny Storm) en la cadena.

- Si la cantidad de R y la cantidad de J son iguales, se considera que la alianza entre la mente y el fuego está en equilibrio y la función debe retornar True.
- Si las cantidades no son iguales, la función debe retornar False.
- En el caso de que no aparezca ninguna de las dos letras en la cadena, se entiende que el equilibrio se mantiene (0 = 0), por lo que la función debe retornar True.
"""

# Módulo del sistema operativo
import os
_ = os.system("clear")

# Mi resolución
# def check_is_balanced(text: str):
#   result_letter_r = 0
#   result_letter_j = 0

#   text = text.upper()
#   letters = list(text)

#   for letter in letters:
#     if letter == "R":
#       result_letter_r += 1
#     if letter == "J":
#       result_letter_j += 1

#   if result_letter_r == result_letter_j:
#     return True
#   else:
#     return False

# result = check_is_balanced("Reed Richards jj")
# print(f"El equilibrio está {'correcto' if result else 'roto'}")

# La resolución de Midu
def check_is_balanced(text: str):
  text = text.upper()

  count_r = text.count("R")
  count_j = text.count("J")

  print(f"count_r: {count_r}. count_j: {count_j}")
  return count_r == count_j

print(check_is_balanced("RRJJ"))
print(check_is_balanced("RRJJJ"))
print(check_is_balanced("RRRJJ"))