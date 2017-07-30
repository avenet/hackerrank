n, m = map(int, raw_input().split())

result = 0

for i in xrange(n, 0, -1):
    if m >= i:
        m -= i
        result += 1
    
    if not m:
        break

print -1 if m else result