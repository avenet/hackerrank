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

sum_result = numpy.sum(items, axis=0)

print(numpy.product(sum_result))
