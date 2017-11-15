n, d = map(
    int,
    input().split()
)

numbers = list(
    map(
        int,
        input().split()
    )
)

numbers_map = {
    number: True
    for number
    in numbers
}

total_triplets = 0

for number in numbers:
    if number + d in numbers_map and number + 2 * d in numbers_map:
        total_triplets += 1

print(total_triplets)
