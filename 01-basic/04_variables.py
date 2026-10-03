##
# 04 - Variables
# Las variables sirven para guardar datos en memoria.
# Python es un lenguaje de tipado dinámico y de tipado fuerte.
###

# Módulo del sistema operativo
import os
_ = os.system("clear")

my_name = "Joaquín"
print(my_name)

age = 28
print(age)

age = 29
print(age)

# Tipado dinámico: el tipo de dato se determina en tiempo de ejecución.
name = "Joaquín"
print(type(name))
name = 123
print(type(name))

# Tipado fuerte: Python no realizar conversiones de tipos automáticamente.
# print(10 + "2") # Error de tipo
print(f"Me llamo {my_name}, y tengo {age} años", end="\n\n")

# Forma no recomendada de asignar variables:
country, city, postal_code = "España", "Madrid", "28001"
print(country, city, postal_code)

# Convenciones de nombres de variables:
mi_variable = "ok" # Snake_case
MiVariable = "ko" # PascalCase - no es buena convención en python
MI_CONSTANTE = "ok" # se suele utilizar para cosntantes, pero tener en cuenta que en python no hay constantes
#mi-variable = "ko" # Error de sintaxis

# Palabras reservadas en Python (no se pueden usar como nombres de variables)

# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']

# Anotaciones de tipo (opcional, para mayor claridad en el código)
is_user_logged_in: bool = True # Indica que la variable es un booleano
print(is_user_logged_in)

# is_user_logged_in = 42 # Error de tipo, pero funcionaría igual porque el tipado es dinámico