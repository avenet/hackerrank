n, k = map(int, raw_input().split())

numbers = set(map(int, raw_input().split()))

result = len(numbers)

for i in xrange(1, n+1):
    if i not in numbers and i+1 not in numbers and i-1 not in numbers:
        result += 1
        numbers.add(i)

print len(numbers)