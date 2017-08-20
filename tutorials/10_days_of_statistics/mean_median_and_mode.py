n = int(input())

items = list(map(int, input().split()))

items.sort()

mean = round(float(sum(items)) / len(items), 1)

middle_position = int(n / 2)

middle_item = float(items[middle_position])

median = round((middle_item + items[middle_position - 1]) / 2, 1)

current_item = None
current_ocurrences = 0
max_ocurrences = 0
max_ocurrences_number = None

for item in items:
    if item == current_item:
        current_ocurrences += 1
    else:
        current_ocurrences = 1
        current_item = item

    if current_ocurrences > max_ocurrences:
        max_ocurrences = current_ocurrences
        max_ocurrences_number = item

print(mean)
print(median)
print(max_ocurrences_number)
