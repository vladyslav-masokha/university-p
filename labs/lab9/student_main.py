import re

def task1(str):
    pattern = r'^([a-z0-9][a-z0-9])+$'
    return bool(re.match(pattern, str))

# print('Task1', task1('hello123'))
  
def task2(str):
  pattern = r'[A-Z]'
  return bool(re.match(pattern, str))

print('Task2', task2('Hello'))

def task3(str):
  pattern = r'^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'
  return bool(re.match(pattern, str))

# print('Task3', task3('192.168.1.1'))

def task4(str):
  pattern = r'^([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$'
  return bool(re.match(pattern, str))

# print('Task4', task4('0:34:59'))

def task5(str):
  pattern = r'^\d{5}(?:[-\s]\d{4})?$'
  return bool(re.match(pattern, str))

# print('Task5', task5('12345-6789'))

def task6(str):
  pattern = r'^[a-z0-9_-]{6,12}$'
  return bool(re.match(pattern, str))

# print('Task6', task6('john_doe-123'))

def task7(str):
    pattern = r"^(4|5|6)\d{3}(-|\s)?\d{4}(-|\s)?\d{4}(-|\s)?\d{4}$"
    return bool(re.match(pattern, str))

def task8(str):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(pattern, str))

def task9(str):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{8,}$'
    return bool(re.match(pattern, str))

def task10(str):
    pattern = r"^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    return bool(re.match(pattern, str))
  