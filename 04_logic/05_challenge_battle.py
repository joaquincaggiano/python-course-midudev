"""
Tienes dos listas de números, lista_a y lista_b, ambas de la misma longitud. 

Cada número en lista_a se "enfrenta" al número en la misma posición en lista_b.

- Si el número en lista_a es mayor, su valor se suma al siguiente número en lista_a.
- Si el número en lista_b es mayor, su valor se suma al siguiente número en lista_b.
- Si los dos números son iguales, ambos se eliminan y no afectan al siguiente par.

Debes simular estos enfrentamientos y devolver el resultado final:
- Si al final queda un número en lista_a, devuelve ese número seguido de la letra "a" (por ejemplo, "3a").
- Si al final queda un número en lista_b, devuelve ese número seguido de la letra "b" (por ejemplo, "2b").
- En caso de empate, devuelve la letra "x".

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]

resultado = battle(lista_a, lista_b)  # -> "2b"

# Explicación:
# - 2 vs 3: gana 3 (+1)
# - 4 vs 3+1: empate
# - 2 vs 4: gana 4 (+2)
# Resultado: "2b"

lista_a = [4, 4, 4]
lista_b = [2, 8, 2]

resultado = battle(lista_a, lista_b)  # -> "x"

# Explicación:
# - 4 vs 2: gana 4 (+2)
# - 4+2 vs 8: gana 8 (+2)
# - 4 vs 2+2: empate
# Resultado: "x"
"""

# Módulo del sistema operativo
import os
_ = os.system("clear")

def battle(list_a: list[int], list_b: list[int]):
  points_a = sum(list_a)
  points_b = sum(list_b)
  return f"{points_a - points_b}a" if points_a > points_b else f"{points_b - points_a}b" if points_b > points_a else "x"

def battle_v2(list_a: list[int], list_b: list[int]):
  if len(list_a) != len(list_b):
    return "Las listas no tienen la misma longitud"

  carry_a = 0
  carry_b = 0

  for i in range(len(list_a)):
    current_a = list_a[i] + carry_a
    current_b = list_b[i] + carry_b
    carry_a = 0
    carry_b = 0

    if current_a > current_b:
      carry_a = current_a - current_b
    elif current_b > current_a:
      carry_b = current_b - current_a

  if carry_a > 0:
    return f"{carry_a}a"
  if carry_b > 0:
    return f"{carry_b}b"
  return "x"

list_a = [4, 1, 4]
list_b = [2, 8, 2]

winner = battle(list_a, list_b)
print(f"Winner: {winner}")

winner_v2 = battle_v2(list_a, list_b)
print(f"Winner v2: {winner_v2}")
