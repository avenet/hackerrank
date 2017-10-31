lowercase_letters = map(
    chr,
    range(97, 123)
)

lowercase_letter_heights = map(
    int,
    input().strip().split(' ')
)

height_map = dict(
    zip(
        lowercase_letters,
        lowercase_letter_heights
    )
)

word = input().strip()

word_heights = [
    height_map.get(character)
    for character
    in word
]

max_word_height = max(word_heights)

print(max_word_height * len(word))
