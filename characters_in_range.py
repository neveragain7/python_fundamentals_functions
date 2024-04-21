def ascii_string(char_1, char_2):
    num_1 = ord(char_1)
    num_2 = ord(char_2)
    ascii_list = []
    final_string = ""

    for index in range(num_1 + 1, num_2):
        ascii_list.append(str(chr(index)))

    for symbol in ascii_list:
        symbol = str(symbol)
        final_string += symbol

    return " ".join(final_string)


character_input_1 = input()
character_input_2 = input()

result = ascii_string(character_input_1, character_input_2)
print(result)
