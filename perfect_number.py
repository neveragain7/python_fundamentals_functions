def perfect_number(number):
    is_perfect = False
    total_sum = 0
    for current_number in range(1, number):
        if number % current_number == 0:
            total_sum += current_number

    if total_sum == number:
        is_perfect = True

    if is_perfect:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number_input = int(input())

result = perfect_number(number_input)
print(result)
