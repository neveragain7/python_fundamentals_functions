def password_validation(password):
    is_password_valid = False

    digits = 0

    is_length_valid = False
    are_only_letters_and_digits_included = True
    are_digits_enough = False

    if 6 <= len(password) <= 10:
        is_length_valid = True

    for symbol in password:
        if not (symbol.isnumeric() or symbol.isalnum()):
            are_only_letters_and_digits_included = False
            break

    for symbol in password:
        if symbol.isnumeric():
            digits += 1
            if digits == 2:
                are_digits_enough = True
                break

    if not is_length_valid:
        print("Password must be between 6 and 10 characters")
    if not are_only_letters_and_digits_included:
        print("Password must consist only of letters and digits")
    if not are_digits_enough:
        print("Password must have at least 2 digits")

    if is_length_valid and are_only_letters_and_digits_included and are_digits_enough:
        print("Password is valid")


password_input = input()

password_validation(password_input)
