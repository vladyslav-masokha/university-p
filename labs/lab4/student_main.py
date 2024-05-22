import functools
import math

def task1 (a, b, c):
  return max(a, b, c)

def task2 (arr):
  return sum(arr)

def task3 (arr):
	return functools.reduce(lambda a, b : a * b, arr)

def task4 (str):
  return str[::-1]

def task5 (n):
  if n < 0:
    return "Factorial is not defined for negative numbers"
  elif n == 0:
    return 1
  else:
    factorial = 1
    for i in range(1, n + 1):
      factorial *= i
    return factorial
  
def task6 (num):
  return 25 <= num <= 50

def task7 (str):
  upper_count = sum(1 for char in str if char.isupper())
  lower_count = sum(1 for char in str if char.islower())
  return upper_count, lower_count

def task8 (arr):
  return list(set(arr))

def task9(arr):
  return [num for num in arr if num % 2 == 0]

def task10 (row):
  return max(math.comb(row, k) for k in range(row + 1))
