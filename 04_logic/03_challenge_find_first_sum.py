"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

# Módulo del sistema operativo
import os
_ = os.system("clear")

def find_first_sum(nums: list[int], goal: int):
  for i, num in enumerate(nums):
    for j in range(i + 1, len(nums)):
      if num + nums[j] == goal:
        return [i, j]
  
  return None


print(find_first_sum([4, 5, 7, 7], 14))