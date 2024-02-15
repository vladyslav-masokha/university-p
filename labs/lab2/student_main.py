def task1(number1, option ,number2):
  if option == '>':
    return number1 > number2
  elif option == '<':
    return number1 < number2
  elif option == '>=':
    return number1 >= number2
  elif option == '<=':
    return number1 <= number2
  elif option == '!=':
    return number1 == number2
  elif option == '!=':
    return number1 != number2

def task2(text, number):
  if len(text) > number:
    return len(text)

print(task2('qwe', 2))
  
def task3(number1, number2, number3):
  if number1 == number2 == number3:
    return number1 == number2 == number3
  else:
    return False