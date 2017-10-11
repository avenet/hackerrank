import numpy

n, m = map(int, input().split())

first_array = []
second_array = []

for _ in range(n):
    first_array.append(list(map(int, input().split())))

for _ in range(n):
    second_array.append(list(map(int, input().split())))

first_array = numpy.array(first_array)
second_array = numpy.array(second_array)

print(first_array + second_array)
print(first_array - second_array)
print(first_array * second_array)
print(first_array // second_array)
print(first_array % second_array)
print(first_array ** second_array)
