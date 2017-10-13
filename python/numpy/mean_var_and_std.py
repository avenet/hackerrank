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

print(numpy.mean(items, axis=1))
print(numpy.var(items, axis=0))
print(numpy.std(items, axis=None))
