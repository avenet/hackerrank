from itertools import combinations_with_replacement

word, number = input().split()

number = int(number)

word_chars = list(sorted(word))

for combination in combinations_with_replacement(
    word_chars,
    number
):
    print(''.join(combination))
