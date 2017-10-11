import numpy

rows, columns = map(int, input().split())

print(numpy.eye(rows, columns, k=0))
