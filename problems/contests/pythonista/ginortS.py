def key_function(char):
    char_number = ord(char)
    if char.islower():
        return char_number
    elif char.isupper():
        return 100 + char_number
    elif char.isdigit():
        char_number = int(char)
        if char_number % 2 == 0:
            return 300 + char_number
        else:
            return 200 + char_number
    return 400 + char_number

print reduce(lambda x,y: x+y, sorted(raw_input(), key=key_function))