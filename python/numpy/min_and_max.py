import numpy

n, m = map(int, input().split())

items = []

for _ in range(n):
    items.append(
        list(
            map(
                int,
                input().split()
            )
        )
    )

axis_one_min = numpy.min(items, axis=1)

print(numpy.max(axis_one_min))
