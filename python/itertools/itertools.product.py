from itertools import product

a_list = map(int, input().split())
b_list = map(int, input().split())

print(
    ' '.join(
        map(
            str,
            product(a_list, b_list)
        )
    )
)
