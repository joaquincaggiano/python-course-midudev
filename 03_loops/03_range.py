###
# 03 - range()
# Permite crear una secuencia de números. Puede ser útil para for, pero no solo para eso
###

# Módulo del sistema operativo
import os
_ = os.system("clear")

print("\nRange:")
print("\nRange desde 0 a 9:")
nums = range(10) # No genera una lista, sino un objeto range
print(nums)
for num in nums:
  print(num)

nums = range(5, 10)
print("\nRange desde 5 a 10:")
for num in nums:
  print(num)

nums = range(2, 10, 2)
print("\nRange desde 0 a 10 con step 2:")
for num in nums:
  print(num)

print("\nRange desde -5 a 0:")
nums = range(-5, 0)
for num in nums:
  print(num)

print("\nRange de 10 a 0 con step -1:")
nums = range(10, 0, -1)
for num in nums:
  print(num)

print("\nCrear una lista a partir de un range:")
nums = list(range(10))
print(nums)

print("\nUtilizar range para hacer cierta cantidad de veces algo:")
for _ in range(5):
  print("Se ejecuta 5 veces")