import numpy

items_array = []

line_count, _ = map(int, input().split())

for line_index in range(line_count):
    current_list = list(
        map(
            int,
            input().split()
        )
    )

    items_array.append(current_list)

items_array = numpy.array(items_array)

print(numpy.transpose(items_array))
print(items_array.flatten())
