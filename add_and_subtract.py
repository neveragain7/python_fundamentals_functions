def sum_numbers(number_1, number_2):
    total = number_1 + number_2
    return total


entered_number_1 = int(input())
entered_number_2 = int(input())
entered_number_3 = int(input())

result_1 = sum_numbers(entered_number_1, entered_number_2)


def subtract(number_3):
    return result_1 - number_3


result_2 = subtract(entered_number_3)
print(result_2)
