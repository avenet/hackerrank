n, k, q = map(
    int,
    input().strip().split(' ')
)

array = [
    int(a_temp)
    for a_temp
    in input().strip().split(' ')
]


def rotate_right_n(arr, k):
    array_length = len(arr)
    result = [None] * array_length

    for i, item in enumerate(arr):
        new_position = (i + k) % array_length
        result[new_position] = item

    return result


rotated_array = rotate_right_n(array, k)

for a0 in range(q):
    m = int(input().strip())
    print(rotated_array[m])
