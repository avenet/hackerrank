from itertools import product

k, m = map(int, input().split())


def compute_f(items):
    return sum(items) % m


items_list = []

for i in range(k):
    items_list.append(
        [
            int(x) ** 2
            for x
            in input().split()[1:]
        ]
    )

print(
    max(
        map(
            compute_f,
            product(*items_list)
        )
    )
)
