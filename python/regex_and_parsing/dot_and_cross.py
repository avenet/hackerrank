import numpy

n = int(input())

a_matrix = []
b_matrix = []

for _ in range(n):
    a_matrix.append(
        list(
            map(
                int,
                input().split()
            )
        )
    )
    
for _ in range(n):
    b_matrix.append(
        list(
            map(
                int,
                input().split()
            )
        )
    )

a_matrix = numpy.array(a_matrix)
b_matrix = numpy.array(b_matrix)

print(a_matrix.dot(b_matrix))
