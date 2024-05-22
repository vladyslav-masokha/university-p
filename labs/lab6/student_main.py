def task1(nums):
    if len(nums) != 2:
        raise ValueError("Вхідний кортеж повинен містити рівно два числа")
    return sum(nums)

def task2(items):
    return len(items)

def task3(nums):
    sorted_nums = sorted(nums, reverse=True)
    return sorted_nums[0]

def task4(tuple_with_dict):
    if not isinstance(tuple_with_dict, tuple) or not isinstance(tuple_with_dict[0], dict):
        raise ValueError("Вхідні дані повинні бути кортежем, що містить один словник")
    return tuple_with_dict[0].get("name")
  
print(task4(({"name": "test"},)))

def task5(input_list):
    sorted_tuples = sorted(input_list, key=lambda x: len(x[0]))
    return sorted_tuples[-1][-1]
  
print(task5([("apple", "banana"), ("pear", "orange","kiwi"), ("grape",)]))

def task6(lists):
    odd_numbers = [number for sublist in lists for number in sublist if number % 2 != 0]
    if not odd_numbers:
        return 0
    product = 1
    for num in odd_numbers:
        product *= num
    return product

def task7(tuple_of_tuples):
    return sum(second_element for _, second_element in tuple_of_tuples)
