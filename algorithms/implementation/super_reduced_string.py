#!/bin/python3


def super_reduced_string(str_value):
    result = str_value

    while True:
        previous_length = len(result)
        unique_letters = set(result)

        for unique_letter in unique_letters:
            result = result.replace(
                unique_letter * 2,
                ''
            )

        if len(result) == previous_length:
            break

    if not result:
        return 'Empty String'

    return result

s = input().strip()

reduced_string = super_reduced_string(s)

print(reduced_string)
