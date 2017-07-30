n, t = map(int, raw_input().split())

lanes = map(int, raw_input().split())

for testcase in xrange(t):
    ini, end = map(int, raw_input().split())
    min_width = min(lanes[ini: end+1])
    print min_width