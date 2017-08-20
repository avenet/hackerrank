#!/bin/python3

arr = list(
    map(
        int,
        input().strip().split(' ')
    )
)

arr.sort()

min_sum = sum(arr[:4])
max_sum = sum(arr[-4:])

print('{} {}'.format(min_sum, max_sum))
