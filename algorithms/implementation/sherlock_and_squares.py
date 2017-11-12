from math import sqrt, floor, ceil

test_cases = int(input())

for test_case in range(test_cases):
    left, right = map(int, input().split())

    print(
        int(
            floor(
                sqrt(right)
            ) - ceil(
                sqrt(left)
            ) + 1
        )
    )
