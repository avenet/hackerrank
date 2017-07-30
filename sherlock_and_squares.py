from math import sqrt, floor, ceil

test_cases = int(raw_input())

for test_case in xrange(test_cases):
    left, right = map(int, raw_input().split())
    print int(floor(sqrt(right)) - ceil(sqrt(left)) + 1)