n = int(input().strip())

items = [
    int(A_temp)
    for A_temp
    in input().strip().split(' ')
]

items_map = {}
result = None

for i, item in enumerate(items):
    if item not in items_map:
        items_map[item] = [i]
    else:
        items_map[item].append(i)

for _, item_indexes in items_map.items():
    items_indexes_length = len(item_indexes)

    if items_indexes_length > 1:
        for i in range(items_indexes_length):
            for j in range(i + 1, items_indexes_length):
                diff = item_indexes[j] - item_indexes[i]

                if result is None:
                    result = diff
                elif diff < result:
                    result = diff

print(result if result else -1)
