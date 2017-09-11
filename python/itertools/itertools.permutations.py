from itertools import permutations

str_value, permutation_length = input().split()

permutation_length = int(permutation_length)

combine_chars = sorted(list(str_value))

all_permutations = permutations(
    combine_chars,
    permutation_length
)

for current_permutation in all_permutations:
    print(''.join(current_permutation))
