def check_truth(a, b, c):
    return (a and b) or c
  
def logical_equivalence(a, b):
    return (not a and not b) or (a and b)

def xor(a, b):
    return (a and not b) or (not a and b)

def greet(condition):
    if condition: return "Hello, World!"
    else: return "Goodbye, World!"

def nested_condition(x, y, z):
    if x == y == z: return "All same"
    elif x != y and x != z and y != z: return "All different"
    else: return "Neither"

def count_true(booleans):
    count = 0
    for value in booleans:
        if value: count += 1
    return count

def parity(n):
    binary = bin(n)[2:]
    ones_count = binary.count('1')
    return ones_count % 2 == 0

def majority_vote(a, b, c):
    true_count = count_true([a, b, c])
    return true_count > 1

def switch(condition):
    return not condition

def ternary_check(condition, true_result, false_result):
    if condition: return true_result
    else: return false_result

def validate(x, y, z):
    return x or (y and z)

def chain_check(a, b, c):
    if a < b < c: return "Increasing"
    elif a > b > c: return "Decreasing"
    else: return "Neither"

def filter_true(booleans):
    result = []
    for value in booleans:
        if value:
            result.append(value)
    return result

def multiplexer(a, b, c, x):
    if a: return x * 2
    elif b: return x * 3
    elif c: return x - 5
    else: return x