def palindrome(positive_numbers_list):
    for number in positive_numbers_list:
        if number == number[::-1]:
            print("True")
        else:
            print("False")


list_input = input().split(", ")

palindrome(list_input)
