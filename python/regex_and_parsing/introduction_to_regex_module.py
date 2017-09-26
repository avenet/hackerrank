import re

testcases = int(input())

for i in range(testcases):
    possible_number = input()
    print(
        bool(
            re.match(
                r'^[+-]?\d*\.\d*$',
                possible_number
            )
        )
    )
