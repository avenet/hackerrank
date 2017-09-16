from collections import namedtuple
mark_count, tupleitems = int(input()), input()
total = sum([int(namedtuple('Student', tupleitems)(*input().split()).MARKS) for _ in range(mark_count)])
print(round(total/float(mark_count), 2))
