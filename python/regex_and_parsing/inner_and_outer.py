import numpy

first_array = numpy.array(
    list(
        map(
            int,
            input().split()
        )
    )
)

second_array = numpy.array(
    list(
        map(
            int,
            input().split()
        )
    )
)

print(numpy.inner(first_array, second_array))
print(numpy.outer(first_array, second_array))
