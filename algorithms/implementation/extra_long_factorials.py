from functools import reduce

number = int(input())

print(
    reduce(
        lambda x, y: x * y,
        range(1, number+1)
    )
)
