from itertools import combinations

_ = raw_input()
letters = ''.join(raw_input().split())
combine_length = int(raw_input())

all_combinations = combinations(letters, combine_length)
total_cases = 0.0
cases = 0

for combination in all_combinations:
    if 'a' in combination:
        cases += 1
    total_cases += 1

print round(cases/total_cases, 4)