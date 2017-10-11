import numpy

array_shape = tuple(
    map(
        int,
        input().split()
    )
)

print(
    numpy.zeros(
        array_shape,
        dtype=numpy.int
    )
)

print(
    numpy.ones(
        array_shape,
        dtype=numpy.int
    )
)
