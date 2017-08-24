num, den = map(float, input().split())
inspections = int(input())

p = num / den
q = 1 - p

print(round(q**(inspections - 1) * p, 3))
