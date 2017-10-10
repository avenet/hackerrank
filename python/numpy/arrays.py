import numpy


def arrays(items):
    return numpy.array(items[::-1], float)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
