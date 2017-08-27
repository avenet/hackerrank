#!/bin/python3

camelcase_str = input().strip()


def count_uppercase(str_value):
    return len(
        [
            letter
            for letter
            in str_value
            if letter.isupper()
        ]
    )

print(
    1 + count_uppercase(
        camelcase_str
    )
)
