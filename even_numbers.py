def even_numbers(number):
    if int(number) % 2 == 0:
        return True
    else:
        return False


final_list = []
list_input = input().split(" ")

result = filter(even_numbers, list_input)
for num in result:
    final_list.append(int(num))

print(final_list)