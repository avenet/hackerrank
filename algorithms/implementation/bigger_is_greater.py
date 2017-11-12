n = int(input())


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


for t in range(n):
    word = input()

    k = None

    for i in range(len(word) - 1):
        if word[i] < word[i+1]:
            k = i

    if k is None:
        print('no answer')
        continue

    word_chars = list(word)

    for l in range(len(word) - 1, -1, -1):
        if word[l] > word[k]:
            swap(word_chars, l, k)
            break

    word_chars[
        k+1: len(word_chars)
    ] = word_chars[
        k+1: len(word_chars)
    ][::-1]

    print(''.join(word_chars))
