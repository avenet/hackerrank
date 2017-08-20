import math

n = int(input())

numbers = list(
    map(
        int,
        input().split()
    )
)

mean = sum(numbers) / n

squared_distance = sum(
    [
        (x - mean) ** 2
        for x
        in numbers
    ]
)

standard_deviation = math.sqrt(
    squared_distance / n
)

print(
    round(
        standard_deviation,
        1,
    )
)
