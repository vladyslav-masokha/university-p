from itertools import combinations


def number_generator(numbers):
    for num in numbers:
        yield num


def even_number_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num


def odd_number_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            yield num


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_number_generator(limit):
    primes = []
    num = 2
    while num <= limit:
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            yield num
        num += 1


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def pre_order_traversal(root):
    if root:
        yield root.val
        yield from pre_order_traversal(root.left)
        yield from pre_order_traversal(root.right)


def in_order_traversal(root):
    if root:
        yield from in_order_traversal(root.left)
        yield root.val
        yield from in_order_traversal(root.right)


def post_order_traversal(root):
    if root:
        yield from post_order_traversal(root.left)
        yield from post_order_traversal(root.right)
        yield root.val


def dfs_traversal(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            yield node
            for neighbor in graph[node][::-1]:
                stack.append(neighbor)


def bfs_traversal(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    while queue:
        node = queue.pop(0)
        yield node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


def dict_keys_generator(d):
    for key in d:
        yield key


def dict_values_generator(d):
    for value in d.values():
        yield value


def dict_items_generator(d):
    for key, value in d.items():
        yield key, value


def file_lines_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


def file_words_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.strip().split():
                yield word


def string_chars_generator(string):
    for char in string:
        yield char


def unique_elements_generator(lst):
    seen = set()
    for elem in lst:
        if elem not in seen:
            seen.add(elem)
            yield elem


def reverse_list_generator(lst):
    for i in range(len(lst) - 1, -1, -1):
        yield lst[i]


def cartesian_product_generator(lst1, lst2):
    for item1 in lst1:
        for item2 in lst2:
            yield item1, item2


def permutations_generator(lst):
    if not lst:
        yield ()
    else:
        for i in range(len(lst)):
            elem = lst[i]
            remaining = lst[:i] + lst[i + 1:]
            for perm in permutations_generator(remaining):
                yield (elem,) + perm


def combinations_generator(lst):
    for i in range(1, len(lst) + 1):
        for comb in combinations(lst, i):
            yield comb


def tuple_list_generator(lst):
    for tup in lst:
        yield tup


def parallel_lists_generator(*lists):
    iterators = [iter(lst) for lst in lists]
    while True:
        values = []
        for it in iterators:
            try:
                values.append(next(it))
            except StopIteration:
                return
        yield tuple(values)


def flatten_list_generator(nested_list):
    for elem in nested_list:
        if isinstance(elem, list):
            yield from flatten_list_generator(elem)
        else:
            yield elem


def nested_dict_generator(nested_dict):
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            yield from nested_dict_generator(value)
        else:
            yield key, value


def powers_of_two_generator(n):
    power = 1
    for i in range(n + 1):
        yield power
        power *= 2


def powers_of_base_generator(base, limit):
    power = 1
    while power <= limit:
        yield power
        power *= base


def squares_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 2


def cubes_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 3


def factorials_generator(n):
    factorial = 1
    for i in range(n + 1):
        yield factorial
        if i > 0:
            factorial *= i


def collatz_sequence_generator(n):
    yield n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        yield n


def geometric_progression_generator(initial, common_ratio, limit):
    term = initial
    while term <= limit:
        yield term
        term *= common_ratio


def arithmetic_progression_generator(initial, common_diff, limit):
    term = initial
    while term <= limit:
        yield term
        term += common_diff


def running_sum_generator(lst):
    total = 0
    for num in lst:
        total += num
        yield total


def running_product_generator(lst):
    product = 1
    for num in lst:
        product *= num
        yield product
