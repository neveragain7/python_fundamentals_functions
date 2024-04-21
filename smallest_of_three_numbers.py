def find_min_number(num_1, num_2, num_3):
    return min(num_1, num_2, num_3)


enter_number_1 = int(input())
enter_number_2 = int(input())
enter_number_3 = int(input())

result = find_min_number(enter_number_1, enter_number_2, enter_number_3)
print(result)
