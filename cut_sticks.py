def make_cut(l):
    smallest = min(l)
    return [x - smallest for x in l if x - smallest > 0]

length = int(raw_input())
current = map(int, raw_input().split())

while current:
    print len(current)
    current = make_cut(current)