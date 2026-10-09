###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

# Módulo del sistema operativo
import os
_ = os.system("clear")

""" Definición de una función

def nombre_de_la_funcion(parametro1, parametro2, ...):
   # docstring
   # cuerpo de la función
   return valor_de_retorno # opcional

"""

print("\nEjemplo de una función:")
def saludar():
  print("Hola")

saludar()

print("\nEjemplo de una función con parámetro:")
def saludar_a(nombre: str):
  print(f"Hola, {nombre}")

saludar_a("Joaquín")

print("\nEjemplo de una función con varios parámetros:")
def sumar(a: int, b: int):
  return a + b

resultado = sumar(1, 2)
print(f"Resultado de la suma: {resultado}")

print("\nEjemplo de una función con docstring:")
def restar(a: int, b: int):
  """Resta dos números y devuelve el resultado"""
  return a - b

print("restar.__doc__:", restar.__doc__) # Muestra el docstring que le pasamos arriba
print(restar(4, 2))

print("\nEjemplo de una función con parámetros por defecto:")
def multiplicar(a: int, b: int = 2): # b = 2 es un parámetro por defecto
  return a * b

print("multiplicar(3):", multiplicar(3))
print("multiplicar(3, 4):", multiplicar(3, 4))

print("\nEjemplo de una función con argumentos por clave:")
def describir_persona(nombre: str, edad: int, sexo: str):
  print(f"Soy {nombre}, tengo {edad} años y soy {sexo}")

# Puedo enviar los argumentos sin orden específico
describir_persona(edad = 29, nombre = "Joaquín", sexo = "Masculino")

print("\nEjemplo de una función con argumentos de longitud variable (*args):")
def sumar_todos(*args: int):
  suma = 0
  for numero in args:
    suma += numero
  return suma

print("sumar_todos(1, 2, 3, 4, 5):", sumar_todos(1, 2, 3, 4, 5))

print("\nEjemplo de una función con argumentos de clave-valor de longitud variable (**kwargs):")
def mostrar_informacion_de(**kwargs: object):
  for key, value in kwargs.items():
    print(f"{key}: {value}")

mostrar_informacion_de(edad = 29, nombre = "Joaquín", sexo = "Masculino")