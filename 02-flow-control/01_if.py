###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

# Módulo del sistema operativo
import os
os.system("clear")

print("\nSentencia simple condicional")

age = 18
if age >= 18:
  print("Eres mayor de edad")

print("\nSentencia condicional con else")
edad = 15
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")

print("\nSentencia condicional con elif")
note = 9
if note >= 9:
  print("Sobresaliente!")
elif note >= 7:
  print("Notable!")
elif note >= 5:
  print("Aprobado!")
else:
  print("No has aprobado")

print("\nCondiciones múltiples")
age = 25
has_carnet = True

if age >= 18 and has_carnet:
  print("Puedes conducir")
else:
  print("Policia!")

if age >= 18 or has_carnet:
  print("Puedes conducir en el pueblo")
else:
  print("Pagale al policia y te deja conducir en el pueblo")

it_is_weekend = True
if not it_is_weekend:
  print("Hay que ir a trabajar")
else:
  print("Hoy es fin de semana, puedes ir a la playa")

# No es buena práctica anidar condicionales, se debe evitar.
print("\nAnidar condicionales")
age = 20
has_money = True
if age >= 18:
  if has_money:
    print("Puedes ir a la discoteca")
  else:
    print("Quédate en casa")
else:
  print("No puedes entrar a la discoteca")