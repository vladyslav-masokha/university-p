def task1(arr):
  result = 0
  for num in arr:
    result += pow(num, 2)
  
  return result

def task2(arr):
  average = sum(arr) / len(arr)
  filtered = [num for num in arr if num >= average]
  return sum(filtered)

def task3(arr):
  frequency = {}
  result = []
  
  for num in arr:
    frequency[num] = frequency.get(num, 0) + 1
    
  sorted_frequency = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
    
  for num, count in sorted_frequency:
    result.extend([num] * count)
       
  return result
  
def task4(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    
    return expected_sum - actual_sum

def task5(arr):
    num_set = set(arr)
    max_length = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length

def task6(arr, num):
    num = num % len(arr)
    return arr[-num:] + arr[:-num]

def task7(arr):
    n = len(arr)
    left = [1] * n
    right = [1] * n
    
    for i in range(1, n):
        left[i] = left[i-1] * arr[i-1]
    
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * arr[i+1]
    
    result = []
    for i in range(n):
        result.append(left[i] * right[i])
    return result

def task8(arr):
    max_sum = arr[0]
    curr_sum = arr[0]
    for num in arr[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
        
    return max_sum

def task9(matrix):
    result = []
    if not matrix:
        return result
    
    rows, cols = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, rows-1, 0, cols-1
    
    while top <= bottom and left <= right:
        for col in range(left, right+1):
            result.append(matrix[top][col])
        top += 1
        
        for row in range(top, bottom+1):
            result.append(matrix[row][right])
        right -= 1
        
        if top <= bottom:
            for col in range(right, left-1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        
        if left <= right:
            for row in range(bottom, top-1, -1):
                result.append(matrix[row][left])
            left += 1
    
    return result

def task10(points, num):
    points.sort(key=lambda p: pow(p[0], 2) + pow(p[1], 2))
    return points[:num]