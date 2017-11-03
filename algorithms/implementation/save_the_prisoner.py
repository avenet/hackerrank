#!/bin/python3


def save_the_prisoner(
    total_prisoners,
    sweets,
    starting_prisoner
):
    result = (starting_prisoner + sweets - 1) % total_prisoners

    if not result:
        return total_prisoners

    return result


t = int(input().strip())

for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    warned_prisoner_id = save_the_prisoner(n, m, s)
    print(warned_prisoner_id)
