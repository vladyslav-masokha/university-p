def task1(str):
    return len(str)

def task2(num1, opt, num2):
    if opt == '+':
        return num1 + num2
    elif opt == '-':
        return num1 - num2
    elif opt == '*':
        return num1 * num2
    elif opt == '/':
        return num1 / num2
    else:
        return 'Operator undefined'


def task3(input_list):
    if len(input_list) == 0:
        return "List is empty"
    return max(input_list)
