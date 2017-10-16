import numpy

matrix = []

n = int(input())

for _ in range(n):
    matrix.append(
        list(
            map(
                float,
                input().split()
            )
        )
    )

print(numpy.linalg.det(matrix))
