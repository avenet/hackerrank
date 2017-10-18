#!/bin/python3


def get_distribution_ways(chocolate_bar, desired_sum, desired_slices):
    if len(chocolate_bar) < desired_slices:
        return 0

    current_slice_sum = sum(
        chocolate_bar[:desired_slices]
    )

    result = 0

    i = desired_slices - 1

    while True:
        if current_slice_sum == desired_sum:
            result += 1

        if i + 1 >= len(chocolate_bar):
            break

        i += 1
        current_slice_sum += (
            chocolate_bar[i] - chocolate_bar[i - desired_slices]
        )

    return result


bar_length = int(input().strip())
choco_bar = list(map(int, input().strip().split(' ')))
day, month = input().strip().split(' ')
day, month = [int(day), int(month)]
print(get_distribution_ways(choco_bar, day, month))
