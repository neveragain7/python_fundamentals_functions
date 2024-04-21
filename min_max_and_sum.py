def min_number(list_of_numbers):
    result = min(list_of_numbers)
    return result


def max_number(list_of_numbers):
    result = max(list_of_numbers)
    return result


def sum_numbers(list_of_numbers):
    result = sum(list_of_numbers)
    return result


list_input = input().split(" ")
integers_list = []
for num in list_input:
    integers_list.append(int(num))

min_result = min_number(integers_list)
max_result = max_number(integers_list)
sum_result = sum_numbers(integers_list)
print(f"The minimum number is {min_result}")
print(f"The maximum number is {max_result}")
print(f'The sum number is: {sum_result}')
