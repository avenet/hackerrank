from collections import defaultdict

word_count = int(input())

words_repetitions = defaultdict(int)

unique_words = []

for i in range(word_count):
    current_word = input()

    if current_word not in words_repetitions:
        unique_words.append(current_word)

    words_repetitions[current_word] += 1

print(len(unique_words))
print(
    ' '.join(
        [
            str(
                words_repetitions[word]
            )
            for word
            in unique_words
        ]
    )
)
