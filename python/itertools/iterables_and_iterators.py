from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

a_indexes = set()

for i, char in enumerate(letters):
    if char == 'a':
        a_indexes.add(
            i+1
        )

index_combinations = combinations(
    range(1, n+1),
    k
)

total_combinations = 0
contain_letter_a = 0

for index_combination in index_combinations:
    total_combinations += 1

    if a_indexes.intersection(index_combination):
        contain_letter_a += 1

print(
    round(
        contain_letter_a / total_combinations,
        3
    )
)
