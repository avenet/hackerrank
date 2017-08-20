staircase_length = int(input())

for i in range(1, staircase_length + 1):
    print(
        ' ' * (staircase_length - i) + ('#' * i)
    )
