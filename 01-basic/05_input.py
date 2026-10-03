###
# 05 - Entrada de usuario (input()) - Versión simplificada
# La función input() permite obtener datos del usuario a través de la consola.
###

# Módulo del sistema operativo
import os
_ = os.system("clear")

print("Hola, ¿cómo te llamas?")
name = input()
print(f"Hola, {name}!")

age = input("¿Cuántos años tienes?\n")
print(f"¡{age} años! en 5 años tendrás {int(age) + 5} años") # Lo que respondamos en el input siempre será un string, por lo que hay que convertirlo a int para poder hacer operaciones con él

# Obtener múltiples valores
country, city = input("¿En qué país y ciudad vives?\n").split() # Utilizamos split para separar en dos partes, tenemos que responder con dos valores separados por un espacio porque en el split no le pasamos ningún argumento
print(f"Vives en {country} y {city}")