def sort_the_list(list_result):
    final_list = []
    for number in list_result:
        final_list.append(int(number))
    return final_list


list_input = input().split(" ")
integer_list = []
for num in list_input:
    integer_list.append(int(num))

sorted_list = sorted(integer_list)
result = sort_the_list(sorted_list)
print(result)