def q2(items):
    items_length = len(items)

    if items_length % 2 == 1:
        return items[int(items_length / 2)]
    
    upper_middle_pos = int(items_length / 2)
    lower_middle_pos = upper_middle_pos - 1
    
    return int(
        (
            items[upper_middle_pos] + items[lower_middle_pos]
        ) / 2
    )


def q1(items):
    items_length = len(items)

    return q2(
        items[0: int(items_length / 2)]
    )


def q3(items):
    items_length = len(items)

    lower = int(items_length / 2)

    if items_length % 2 == 1:
        lower += 1

    items = items[lower:]

    return q2(items)

length = int(input())

numbers = map(
    int,
    input().split()
)

frequencies = map(
    int,
    input().split()
)

number_frequencies = list(
    zip(
        numbers,
        frequencies
    )
)

number_frequencies.sort(key=lambda x: x[0])

expanded_numbers = []

for number, freq in number_frequencies:
    expanded_numbers += [number] * freq


print(
    round(
        float(
            q3(expanded_numbers) - q1(expanded_numbers)
        ),
        1
    )
)
