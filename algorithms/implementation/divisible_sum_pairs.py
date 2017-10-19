def divisible_sum_pairs(factor, int_list):
    divisible_pairs_count = 0
    array_length = len(int_list)

    for i in range(array_length):
        for j in range(i + 1, array_length):
            possible_divisor = int_list[i] + int_list[j]
            if possible_divisor % factor == 0:
                divisible_pairs_count += 1

    return divisible_pairs_count


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]

integer_list = list(
    map(
        int,
        input().strip().split(' ')
    )
)

print(
    divisible_sum_pairs(
        k,
        integer_list
    )
)
