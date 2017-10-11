import numpy

n, p, m = map(int, input().split())

n_arrays = []
p_arrays = []

for i in range(n):
    current_array = list(map(int, input().split()))
    n_arrays.append(current_array)

for j in range(p):
    current_array = list(map(int, input().split()))
    p_arrays.append(current_array)

n_array = numpy.array(n_arrays)
p_array = numpy.array(p_arrays)

print(
    numpy.concatenate(
        (n_array, p_array),
        axis=0
    )
)
