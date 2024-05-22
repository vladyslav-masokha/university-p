import re
import numpy as np

def interpolate_missing(nums):
    interpolated = []
    for i, num in enumerate(nums):
        if num is None:
            leftind = i - 1
            rightind = i + 1
            leftval = None
            rightval = None
            while leftind >= 0:
                if nums[leftind] is not None:
                    leftval = nums[leftind]
                    break
                leftind -= 1
            while rightind < len(nums):
                if nums[rightind] is not None:
                    rightval = nums[rightind]
                    break
                rightind += 1

            if leftval is not None and rightval is not None:
                distance = rightind - leftind
                interpolatedval = leftval + ((rightval - leftval) / distance) * (i - leftind)
                interpolated.append(round(interpolatedval))
            elif leftval is not None:
                interpolated.append(leftval)
            elif rightval is not None:
                interpolated.append(rightval)
            else:
                interpolated.append(None)
        else:
            interpolated.append(num)
    return interpolated

def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b

def process_batches(nums, size):
    max_values = []

    for i in range(0, len(nums), size):
        batch = nums[i:i + size]
        max_values.append(max(batch))

    return max_values

def encode_string(string):
    if not string:
        return ""
    
    encoded = ""
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            encoded += (str(count) if count > 1 else '') + string[i - 1]
            count = 1
    encoded += (str(count) if count > 1 else '') + string[-1]
    return encoded

def decode_string(encoded):
    decoded = ""
    count = ""
    for char in encoded:
        if char.isdigit():
            count += char
        else:
            decoded += char * int(count or 1)
            count = ""
    return decoded

def rotate_matrix(matrix):
    n = len(matrix)
    rotated = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = matrix[i][j]
    return rotated

def regex_search(strs, pattern):
    reg = re.compile(pattern)
    return [str for str in strs if reg.search(str)]

def merge_sorted_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:] or arr2[j:])
    return merged

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def group_by_key(data, key):
    grouped = {}
    for item in data:
        key_value = item[key]
        if key_value in grouped:
            grouped[key_value].append(item['value'])
        else:
            grouped[key_value] = [item['value']]
    return grouped


def remove_outliers(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    return [x for x in data if mean - 2 * std_dev <= x <= mean + 2 * std_dev]
