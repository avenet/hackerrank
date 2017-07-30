import re
row_count, col_count = map(int, raw_input().split())

rows = []

for row in xrange(row_count):
    rows.append(raw_input())
    
input_str = ''

for i in xrange(col_count):
    for row in rows:
        input_str += row[i]
        
print(re.sub("(?<=\w)[\W|\s]+(?=[a-zA-Z0-9])", ' ', input_str))