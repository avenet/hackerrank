#!/bin/python3
s_len = int(input().strip())
s = input().strip()

unique_letters = list(
    set(s)
)


def get_alternating_length(
    str_value,
    first_letter,
    second_letter
):
    previous_letter = None
    counter = 0

    for char_value in str_value:
        if (
            char_value in [first_letter, second_letter] and
            previous_letter != char_value
        ):
            previous_letter = char_value
            counter += 1
        elif previous_letter == char_value:
            return 0

    return counter


max_alternating_str_length = 0

for i in range(len(unique_letters)):
    for j in range(i + 1, len(unique_letters)):
        first_unique_letter = unique_letters[i]
        second_unique_letter = unique_letters[j]

        max_alternating_str_length = max(
            get_alternating_length(
                s,
                first_unique_letter,
                second_unique_letter
            ),
            max_alternating_str_length
        )

print(max_alternating_str_length)
