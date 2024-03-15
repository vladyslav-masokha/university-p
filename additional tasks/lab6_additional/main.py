def task1():
    tuple_of_strings = ("Hello", "World")
    return ''.join(tuple_of_strings)
  
print(task1())

def task2(*args):
    return len(args)
  
print(task2(1, 2, "three", 4.5)) 

def task3(numbers):
    sorted_tuple = sorted(numbers, reverse=True)
    return sorted_tuple[0]
  
print(task3((3, 9, 8, 1, 7)))

def task4(dictionary_tuple):
    dictionary = dictionary_tuple[0]
    return dictionary.get("назва")
  
print(task4(({'назва': 'Python'},)))

def task5(data):
    if not isinstance(data, tuple):
        return "Invalid input. Please provide a tuple."
    if not all(isinstance(item, tuple) for item in data):
        return "Invalid input. Please provide a tuple containing a list of tuples."
    sorted_data = sorted(data, key=lambda x: len(x[0]))
    return sorted_data[-1][0]

print(task5((("apple", "banana", "cherry"), ("orange", "grape"), ("kiwi", "pear", "plum", "melon"))))

def task6(list_of_lists):
    filtered_numbers = [num for lst in list_of_lists for num in lst if num % 2 == 0]
    product = 1
    for num in filtered_numbers:
        product *= num
    return product
  
print(task6([[1, 2, 3], [4, 5, 6]]))

def task7(tuple_of_tuples):
    return sum(second for _, second in tuple_of_tuples)
  
print(task7(((1, 2), (3, 4), (5, 6))))

def task8(people):
    max_age = float('-inf')
    oldest_person = None
    for name, age in people:
        if age > max_age:
            max_age = age
            oldest_person = name
    return oldest_person

print(task8([("Dima", 63), ("Bob", 44), ("Dasha", 18), ("Who", 1)]))

def task9(string, numbers):
    result = []
    for num in numbers:
        result.append(num + len(string))
    return result
  
print(task9('qwe', [1, 2, 3]))

def task10(tuple_of_lists):
    result = []
    for i, lst in enumerate(tuple_of_lists, start=0):
        result.append(sum(lst) * i)
    return result
  
print(task10(([1, 2, 3], [4, 5, 6])))