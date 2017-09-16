def find_ocurrences(collection, item):
    result = []
    for i, word in enumerate(collection):
        if word == item:
            result.append(i + 1)
    return result


words_count, lookup_count = map(int, raw_input().split())

collection_items = []

for i in enumerate(xrange(words_count)):
    current_item = raw_input()
    collection_items.append(current_item)

for j in enumerate(xrange(lookup_count)):
    current_item = raw_input()
    ocurrences = map(str, find_ocurrences(collection_items, current_item))

    if ocurrences:
        print(' '.join(ocurrences))
    else:
        print('-1')
