def task4(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def task5(input_list):
    return list(set(input_list))

def task6(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def task7(input_list):
    n = len(input_list) + 1
    full_list = set(range(1, n))
    missing_numbers = sorted(list(full_list - set(input_list)))
    print(missing_numbers)
    return missing_numbers

task7( [1, 2, 4, 6, 7, 9])
