from array import array

def task1(list_of_dicts):
    merged_dict = {}
    for d in list_of_dicts:
        merged_dict.update(d)
    return merged_dict

def task2(string):
    arr = array('i')
    arr.frombytes(bytes.fromhex(string))
    return arr

def task3(array):
    return list(set(array))

def task4(array):
    full_range = set(range(10, 21))
    return list(full_range - set(array))[0]

def task5(data):
    unique_values = set()
    for d in data:
        unique_values.update(d.values())
    return list(unique_values)

def task6(dictionaries):
    total_combinations = 1
    for d in dictionaries:
        total_combinations *= len(d)
    return total_combinations

def task7(dictionary):
    sorted_keys = sorted(dictionary.keys(), reverse=True)
    return sorted_keys[:3]

def task8(list_of_dicts):
    combined_values = {}
    for d in list_of_dicts:
        item = d['item']
        amount = d['amount']
        combined_values[item] = combined_values.get(item, 0) + amount
    return combined_values