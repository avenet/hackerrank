#!/bin/python3


def contains_string(
    str_value,
    expected_str='hackerrank'
):
    i = 0

    for char in str_value:
        if char == expected_str[i]:
            i += 1

        if i == len(expected_str):
            return True

    return False

q = int(input().strip())

for a0 in range(q):
    s = input().strip()

    if contains_string(s):
        print('YES')
    else:
        print('NO')
