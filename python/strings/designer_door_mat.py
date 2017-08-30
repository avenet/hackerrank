N, M = map(int, input().split())


def get_upper_width(k):
    return (M - 3 - (3 * (2 * ((k - 1) // 2)))) // 2


def get_middle_width(k):
    return 2 * ((k - 1) // 2)


def get_down_width(k):
    return (M - 3 - (3 * (2 * ((k - 1) // 2)))) // 2

for i in range(1, N, 2):
    print(
        '{}{}{}'.format(
            '-' * get_upper_width(i),
            '.' + '|..' * get_middle_width(i) + '|' + '.',
            '-' * get_down_width(i)
        )
    )

print(
    '{}{}{}'.format(
        '-' * ((M - 7) // 2),
        'WELCOME',
        '-' * ((M - 7) // 2)
    )
)

for i in range(N-2, -1, -2):
    print(
        '{}{}{}'.format(
            '-' * get_upper_width(i),
            '.' + '|..' * get_middle_width(i) + '|' + '.',
            '-' * get_down_width(i)
        )
    )
