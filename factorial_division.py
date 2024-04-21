def factorial_1(value):
    calculation = 1
    for number in range(value, 0, -1):
        calculation *= number
    return calculation


def factorial_2(value):
    calculation = 1
    for number in range(value, 0, -1):
        calculation *= number
    return calculation


def factorial_division(value1, value2):
    total = f'{int(value1 / value2)}.00'
    return total


number1_input = int(input())
number2_input = int(input())

result = factorial_division(factorial_1(number1_input), factorial_2(number2_input))
print(result)