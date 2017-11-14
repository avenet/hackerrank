from math import floor, ceil, sqrt

s = input().strip().replace(' ', '')

items_count = sqrt(len(s))
row_count = floor(items_count)
column_count = ceil(items_count)

if row_count * column_count < len(s):
    row_count += 1

result = [''] * column_count

for i in range(row_count):
    begin = i * column_count
    end = (i + 1) * column_count
    current_str = s[begin:end]

    for j, char in enumerate(current_str):
        result[j] += char

print(' '.join(result))
