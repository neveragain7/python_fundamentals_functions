def sum_of_even_and_odd_digits(number):
    number_as_string = str(number)
    even_sum = 0
    odd_sum = 0

    for letter in number_as_string:
        digit = int(letter)

        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number_input = int(input())

result = sum_of_even_and_odd_digits(number_input)
print(result)
