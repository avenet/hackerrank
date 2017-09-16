from collections import defaultdict


def get_key(item):
    return item[1], -ord(item[0])


if __name__ == "__main__":
    s = input().strip()
    word_counter = defaultdict(int)

    for char in s:
        word_counter[char] += 1

    top_three_char_matches = sorted(
        word_counter.items(),
        key=get_key,
        reverse=True,
    )[:3]

    for char, char_matches in top_three_char_matches:
        print('{} {}'.format(char, char_matches))
