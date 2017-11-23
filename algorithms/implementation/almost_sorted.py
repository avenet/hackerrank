import sys

_ = input()
numbers = [int(x) for x in input().split()]


def swap(items, i, j):
    items[i], items[j] = items[j], items[i]


def swap_range(items, i, j):
    swapped_elements = items[i: j + 1][::-1]
    swap_index = 0

    for i in range(i, j + 1):
        items[i] = swapped_elements[swap_index]
        swap_index += 1


def find_greater_index(numbers, item):
    i = 0

    for number in numbers:
        if number > item:
            return i
        i += 1

    return -1


def is_sorted(items):
    prev = -1

    for item in items:
        if item < prev:
            return False
        prev = item

    return True


decreasing_indexes = []

for i in range(1, len(numbers)):
    if numbers[i] < numbers[i - 1]:
        decreasing_indexes.append(i)

if not decreasing_indexes:
    print('yes')
    sys.exit(0)

last_decreasing_index = decreasing_indexes[-1]

first_item_index_greater = find_greater_index(
    numbers,
    numbers[last_decreasing_index],
)

if first_item_index_greater != -1:
    swap(
        numbers,
        first_item_index_greater,
        last_decreasing_index
    )

    if is_sorted(numbers):
        print('yes')
        print(
            'swap {} {}'.format(
                first_item_index_greater + 1,
                last_decreasing_index + 1
            )
        )

        sys.exit(0)

    swap(
        numbers,
        first_item_index_greater,
        last_decreasing_index
    )

decreasing = False
decreasing_range = []

for i in range(1, len(numbers)):
    if numbers[i] < numbers[i - 1]:
        if not decreasing:
            decreasing = True
            decreasing_range.append(i - 1)
    elif decreasing:
        decreasing = False
        decreasing_range.append(i - 1)
        break

if decreasing:
    decreasing_range.append(i)

if decreasing_range:
    ini, end = decreasing_range
    swap_range(numbers, ini, end)

    if is_sorted(numbers):
        print('yes')
        print(
            'reverse',
            ini + 1,
            end + 1,
        )
        sys.exit(0)

print('no')
