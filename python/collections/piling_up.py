POP_RIGHT = 1
POP_LEFT = 2

test_cases = int(input())

for test_case in range(test_cases):
    cube_count = int(input())
    cube_pile = list(map(int, input().split()))
    current_number = 2 ** 31
    i = 0
    j = cube_count - 1

    while i < j:
        left = cube_pile[i]
        right = cube_pile[j]

        action = POP_LEFT
        pop_item = left

        if right > left:
            action = POP_RIGHT
            pop_item = right

        if pop_item > current_number:
            break

        if action == POP_LEFT:
            i += 1
        else:
            j -= 1

        current_number = pop_item

    if i < j:
        print('No')
    else:
        print('Yes')
