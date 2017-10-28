from collections import deque

_ = int(input().strip())

numbers = [
    int(a_temp)
    for a_temp
    in input().strip().split(' ')
]

numbers.sort()

picked_numbers = deque()
max_set_length = 0

for current_number in numbers:
    while picked_numbers:
        if current_number - picked_numbers[0] <= 1:
            break

        picked_numbers.popleft()

    picked_numbers.push(current_number)

    max_set_length = max(
        len(picked_numbers),
        max_set_length
    )

print(max_set_length)
