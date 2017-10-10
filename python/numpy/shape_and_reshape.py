import numpy

array_items = list(
    map(
        int,
        input().split()
    )
)

np_array = numpy.array(array_items)
print(numpy.reshape(np_array, (3, 3)))
