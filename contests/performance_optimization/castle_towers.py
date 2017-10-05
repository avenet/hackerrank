def castleTowers(n, ar):
    occurrences_map = {}
    max_item = -1

    for item in ar:
        if item > max_item:
            max_item = item

        if item in occurrences_map:
            occurrences_map[item] += 1
        else:
            occurrences_map[item] = 1

    return occurrences_map[max_item]


if __name__ == "__main__":
    n = int(input().strip())
    ar = map(int, input().strip().split(' '))
    result = castleTowers(n, ar)
    print(result)
