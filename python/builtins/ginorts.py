def get_ginort_char_key(char):
    char_ordinal = ord(char)
    if char.islower():
        return 100 + char_ordinal
    elif char.isupper():
        return 500 + char_ordinal
    elif char.isdigit():
        char_digit = int(char)
        if char_digit % 2 == 1:
            return 700 + char_ordinal
        else:
            return 900 + char_ordinal


print(
    *sorted(
        input(),
        key=get_ginort_char_key
    ),
    sep=""
)
