def loading_bar(value):
    symbol = "%"
    symbol_total = symbol * (int(value / 10))
    if value < 100:
        dots = int((100 - value) / 10)
        dots_total = "." * dots
        result = f'{value}{symbol} [{symbol_total}{dots_total}]\nStill loading...'
    else:
        result = f'{value}{symbol} Complete!\n[{symbol_total}]'
    return result


number_input = int(input())
loading_string = loading_bar(number_input)
print(loading_string)
