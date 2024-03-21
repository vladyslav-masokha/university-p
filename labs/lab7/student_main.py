def task1(age):
    try:
        age = int(age)
        return age
    except ValueError:
        return "Error: Please enter a valid numeric value for age."

def task2(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        return num1 * num2
    except ValueError:
        return "Error: Please enter valid numeric values for numbers."

def task3(input_str):
    try:
        if not isinstance(input_str, str):
            raise TypeError("Error: Please enter a string, not a numeric value.")
        else:
            return len(input_str)
    except TypeError as e:
        return str(e)

def task4(list):
    try:
        total = sum(list)
        return total
    except TypeError:
        return None

def task5(data):
    try:
        processed_data = []
        for item in data:
            name = item[0]
            grades = item[1]
            average_grade = sum(grades) / len(grades)
            processed_data.append((average_grade, name))
        return processed_data
    except Exception as e:
        return "List processing error!"