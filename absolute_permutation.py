#!/bin/python3


def get_permutation(n, k):
    if k == 0:
        return ' '.join(map(str, range(1, n+1)))

    if k >= n:
        return '-1'

    result = [None] * n
    used_numbers = {}

    position = n - 1

    while position:
        real_number = position + 1
        if real_number + k > n and real_number - k > 0:
            used_numbers[real_number - k] = True
            result[position] = str(real_number - k)
        else:
            break

        position -= 1
    
    success = False
        
    for i, item in enumerate(result):
        if item:
            success = True
            break

        lower_guess = i + 1 - k
        upper_guess = i + 1 + k

        if lower_guess > 0 and lower_guess not in used_numbers:
            result[i] = str(lower_guess)
            used_numbers[lower_guess] = True
        elif 0 < upper_guess <= n and upper_guess not in used_numbers:
            result[i] = str(upper_guess)
            used_numbers[upper_guess] = True
        else:
            break

    if not success:
        return '-1'

    return ' '.join(result)

t = int(input().strip())

for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    print(get_permutation(n, k))
