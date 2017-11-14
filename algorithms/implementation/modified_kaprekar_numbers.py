from math import floor

p = int(input())
q = int(input())


def is_kaprekar(n):
    if n == 1:
        return True
    
    number_squared = n ** 2
    str_squared_number = str(number_squared)
    
    digits = len(str_squared_number)
    
    half = floor(digits / 2)
    
    left_part = int(str_squared_number[:half] or '0')
    right_part = int(str_squared_number[half:] or '0')
    
    return left_part + right_part == n


kaprekar_numbers = [
    str(number)
    for number
    in range(p, q + 1)
    if is_kaprekar(number)
]

if kaprekar_numbers:
    print(' '.join(kaprekar_numbers))
else:
    print('INVALID RANGE')
