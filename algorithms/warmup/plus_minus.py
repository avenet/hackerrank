n = int(input())

numbers = map(
    int,
    input().split()
)

positive_count = len(
    [
        x
        for x
        in numbers
        if x > 0
    ]
)

negative_count = len(
    [
        x
        for x
        in numbers
        if x < 0
    ]
)

zeroes_count = len(
    [
        x
        for x
        in numbers
        if x == 0
    ]
)

print(
    round(
        float(positive_count) / float(n),
        3
    )
)

print(
    round(
        float(negative_count) / float(n),
        3
    )
)

print(
    round(
        float(zeroes_count) / float(n),
        3
    )
)
