from itertools import combinations

def task9(dicts):
    result = {}
    for key, values in dicts.items():
        result[key] = sum(values) / len(values)
    return result
  
# check_task9 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
# print(task9(check_task9))
  
def task10(arr1, arr2):
    return list(set(arr1) & set(arr2))
  
# check_task10 = [1, 2, 3, 4, 5], [3, 4, 5, 6, 7]
# print(task10(*check_task10))
  
def task11(dicts):
    return dict(sorted(dicts.items(), key=lambda item: item[1]))

# check_task11 = {'A': 3, 'B': 1, 'C': 2}
# print(task11(check_task11))
  
def task12(array):
    return array[::-1]
  
# check_task12 = [1, 2, 3, 4, 5]
# print(task12(check_task12))
  
def task13(lst):
    return sum(sum(comb) for r in range(1, len(lst) + 1) for comb in combinations(lst, r))
  
# check_task13 = [1, 2, 3]
# print(task13(check_task13))
  
def task14(list, key):
    return [{k: v for k, v in d.items() if k != key} for d in list]
  
# check_task14 = [{'A': 1, 'B': 2}, {'A': 3, 'C': 4}, {'B': 5, 'D': 6}]
# print(task14(*check_task14))
  
def task15(arr1, arr2):
    return sorted(arr1 + arr2)
  
# check_task15 = [5, 3, 7], [1, 8, 2]
# print(task15(*check_task15))

def task16(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] = value
    return result

# check_task16 = {'A': 1, 'B': 2}, {'B': 3, 'C': 4}
# print(task16(*check_task16))