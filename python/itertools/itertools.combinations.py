from itertools import combinations

word, k = input().split()

k = int(k)

word_chars = sorted(list(word))

for i in range(1, k+1):
    for word_combination in combinations(word_chars, i):
        print(''.join(word_combination))
